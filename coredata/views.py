# Create your views here.
from django.http import Http404
from django.utils import timezone, dateformat
from rest_framework import mixins, views, generics, response, status, permissions
from rest_framework.generics import get_object_or_404

from coredata.models import Region, District, Reference, ItemType, User
from coredata.permissions import PaidServicePermission
from coredata.serializers import RegionSerializer, DistrictSerializer, ReferenceSerializer, UserSerializer, \
    UserPasswordChangeSerializer, UserCreateSerializer


class RegionList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, PaidServicePermission]
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DistrictList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, PaidServicePermission]
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    pagination_class = None
    filterset_fields = ['region', ]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ExpensetList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, PaidServicePermission]
    queryset = Reference.objects.filter(type=ItemType.EXPENSE)
    pagination_class = None
    serializer_class = ReferenceSerializer
    filterset_fields = ['code', 'type']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PotassiumCoefficientAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, PaidServicePermission]
    serializer_class = ReferenceSerializer

    def get_object(self, code):
        try:
            return Reference.objects.get(code=code, type=ItemType.POTASSIUM_COEFFICIENT)
        except Reference.DoesNotExist:
            raise Http404

    def get(self, request, code, format=None):
        coefficient = self.get_object(code)
        serializer = self.serializer_class(coefficient)
        return response.Response(serializer.data)


class PhosphorusCoefficientAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, PaidServicePermission]
    serializer_class = ReferenceSerializer

    def get_object(self, code):
        try:
            return Reference.objects.get(code=code, type=ItemType.PHOSPHORUS_COEFFICIENT)
        except Reference.DoesNotExist:
            raise Http404

    def get(self, request, code, format=None):
        coefficient = self.get_object(code)
        serializer = self.serializer_class(coefficient)
        return response.Response(serializer.data)


class ExpenseCoefficientAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, PaidServicePermission]
    serializer_class = ReferenceSerializer

    def get_object(self, pk):
        try:
            return Reference.objects.get(pk=pk)
        except Reference.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reference = self.get_object(pk)
        serializer = self.serializer_class(reference)
        return response.Response(serializer.data)


class CurrentUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, PaidServicePermission]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return response.Response(serializer.data)

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request):
        self.object = self.get_object()
        serializer = UserPasswordChangeSerializer(data=request.data)
        user_info_serializer = UserSerializer(request.user)
        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return response.Response(
                    {
                        "old_password": ["Wrong password."]
                    },
                    status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return response.Response(user_info_serializer.data, status=status.HTTP_200_OK)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(views.APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, status=True, pk=pk)
        # checking user role
        if request.user.user_role == 0 or (
                (request.user.user_role == 1 and user.user_role == 2) and request.user.region == user.region):
            return response.Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return response.Response({"error": "You can see only collectors' of own region"},
                                 status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        users = User.objects.filter(region=request.user.region, status=True) \
            .exclude(pk=request.user.pk) \
            .exclude(pk=user.pk)
        # user can not edit yourself
        if request.user == user:
            return response.Response({"error": "You can not edit yourself. To edit contact to Admins."},
                                     status=status.HTTP_400_BAD_REQUEST)
        serializer = UserCreateSerializer(user, data=request.data)
        district = get_object_or_404(District, pk=request.data.get('district'))
        if serializer.is_valid():
            # if user is not admin and user is manager
            if request.user.user_role == 1 and user.user_role == 2 and request.user.region == user.region:
                # checking district by region
                if request.user.user_role == 1 and district.region != request.user.region:
                    return response.Response({"error": 'District not found'}, status=status.HTTP_400_BAD_REQUEST)
                # checking district's collector
                for u in users:
                    if u.district.id == district.id:
                        return response.Response(
                            {"error": 'This district is currently have collector. '},
                            status=status.HTTP_400_BAD_REQUEST)
                user.user_role = 2
                user.region = request.user.region
                serializer.save(region=request.user.region)
                return response.Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            # if user is admin
            elif request.user.user_role == 0:
                serializer.save()
                return response.Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            return response.Response({"error": "You can manage only collectors' of own region."},
                                     status=status.HTTP_400_BAD_REQUEST)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk, status=True)
        # user can not delete yourself
        if request.user == user:
            return response.Response({"error": "You can not delete yourself. To delete contact to Admins."},
                                     status=status.HTTP_400_BAD_REQUEST)
        # checking user's privileges
        if request.user.user_role == 0 or (
                request.user.user_role == 1 and user.user_role == 2 and request.user.region == user.region):
            user.status = False
            today = dateformat.format(timezone.now(), 'd-m-Y')
            user.username = f"{user.username}_removed_at_{today}"
            user.save()
            return response.Response({'status': 'success'}, status=status.HTTP_204_NO_CONTENT)
        return response.Response({"error": "You can manage only collectors' of own region."},
                                 status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(views.APIView):
    def get(self, request):
        # getting only own collectors
        users = User.objects.filter(region=request.user.region, status=True).exclude(pk=request.user.pk)
        return response.Response(UserSerializer(users, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserCreateSerializer(data=request.POST)
        # getting only own collectors
        users = User.objects.filter(region=request.user.region, status=True).exclude(pk=request.user.pk)
        if serializer.is_valid() and request.user.status:
            data = serializer.validated_data
            district = data.get('district')
            # checking district by region
            if request.user.user_role == 1 and district.region != request.user.region:
                return response.Response({"error": 'District not found'}, status=status.HTTP_400_BAD_REQUEST)
            # checking district's collector
            for u in users:
                if u.district.id == district.id:
                    return response.Response(
                        {"error": 'This district is currently have collector.'},
                        status=status.HTTP_400_BAD_REQUEST)
            password = data.pop('password')
            user = User.objects.create(**data)
            if request.user.user_role == 1:
                user.user_role = 2
                user.region = request.user.region
            if password is not None:
                user.set_password(password)
            user.save()
            return response.Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
