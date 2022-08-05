import xlwt
from django.db.models import Sum
from django.http import HttpResponse
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from coredata.permissions import PaidServicePermission
from .models import Sample
from .serializers import SampleSerializer


class SampleStatistics(views.APIView):
    permission_classes = (IsAuthenticated, PaidServicePermission,)

    def get(self, request):
        type = request.query_params.get("type")
        calculation_region = request.query_params.get("calculation_region")
        calculation_district = request.query_params.get("calculation_district")
        requested_all = Sample.objects.all()
        user = self.request.user
        if user.region is not None:
            requested_all = Sample.objects.filter(calculation_region=user.region)
        if type is None:
            return response.Response({}, status=status.HTTP_400_BAD_REQUEST)
        if calculation_region is not None:
            requested_all = Sample.objects.filter(calculation_region__pk=calculation_region)
            if user.region is not None:
                requested_all = Sample.objects.filter(calculation_region=user.region)
                if type == "potassium":
                    lowest_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.lowest,
                                                                 calculation_region=user.region)
                    low_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.low,
                                                              calculation_region=user.region)
                    highest_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.highest,
                                                                  calculation_region=user.region)
                    high_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.high,
                                                               calculation_region=user.region)
                    normal_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.normal,
                                                                 calculation_region=user.region)
                if type == "phosphorus":
                    lowest_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.lowest,
                                                                 calculation_region=user.region)
                    low_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.low,
                                                              calculation_region=user.region)
                    highest_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.highest,
                                                                  calculation_region=user.region)
                    high_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.high,
                                                               calculation_region=user.region)
                    normal_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.normal,
                                                                 calculation_region=user.region)
                if type == "humus":
                    lowest_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.lowest,
                                                                 calculation_region=user.region)
                    low_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.low,
                                                              calculation_region=user.region)
                    highest_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.highest,
                                                                  calculation_region=user.region)
                    high_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.high,
                                                               calculation_region=user.region)
                    normal_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.normal,
                                                                 calculation_region=user.region)
            else:
                if type == "potassium":
                    lowest_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.lowest,
                                                                 calculation_region__pk=calculation_region)
                    low_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.low,
                                                              calculation_region__pk=calculation_region)
                    highest_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.highest,
                                                                  calculation_region__pk=calculation_region)
                    high_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.high,
                                                               calculation_region__pk=calculation_region)
                    normal_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.normal,
                                                                 calculation_region__pk=calculation_region)
                if type == "phosphorus":
                    lowest_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.lowest,
                                                                 calculation_region__pk=calculation_region)
                    low_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.low,
                                                              calculation_region__pk=calculation_region)
                    highest_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.highest,
                                                                  calculation_region__pk=calculation_region)
                    high_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.high,
                                                               calculation_region__pk=calculation_region)
                    normal_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.normal,
                                                                 calculation_region__pk=calculation_region)
                if type == "humus":
                    lowest_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.lowest,
                                                                 calculation_region__pk=calculation_region)
                    low_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.low,
                                                              calculation_region__pk=calculation_region)
                    highest_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.highest,
                                                                  calculation_region__pk=calculation_region)
                    high_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.high,
                                                               calculation_region__pk=calculation_region)
                    normal_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.normal,
                                                                 calculation_region__pk=calculation_region)
        else:
            if user.region is not None:
                if type == "potassium":
                    lowest_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.lowest, calculation_region=user.region)
                    low_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.low, calculation_region=user.region)
                    highest_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.highest, calculation_region=user.region)
                    high_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.high, calculation_region=user.region)
                    normal_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.normal, calculation_region=user.region)
                if type == "phosphorus":
                    lowest_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.lowest, calculation_region=user.region)
                    low_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.low, calculation_region=user.region)
                    highest_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.highest, calculation_region=user.region)
                    high_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.high, calculation_region=user.region)
                    normal_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.normal, calculation_region=user.region)
                if type == "humus":
                    lowest_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.lowest, calculation_region=user.region)
                    low_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.low, calculation_region=user.region)
                    highest_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.highest, calculation_region=user.region)
                    high_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.high, calculation_region=user.region)
                    normal_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.normal, calculation_region=user.region)
            else:
                if type == "potassium":
                    lowest_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.lowest)
                    low_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.low)
                    highest_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.highest)
                    high_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.high)
                    normal_requested_all = Sample.objects.filter(provided_level_potassium=Sample.Status.normal)
                if type == "phosphorus":
                    lowest_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.lowest)
                    low_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.low)
                    highest_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.highest)
                    high_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.high)
                    normal_requested_all = Sample.objects.filter(provided_level_phosphorus=Sample.Status.normal)
                if type == "humus":
                    lowest_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.lowest)
                    low_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.low)
                    highest_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.highest)
                    high_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.high)
                    normal_requested_all = Sample.objects.filter(provided_level_humus=Sample.Status.normal)
        if calculation_district is not None:
            lowest_requested_all = lowest_requested_all.filter(calculation_district__pk=calculation_district)
            low_requested_all = low_requested_all.filter(calculation_district__pk=calculation_district)
            highest_requested_all = highest_requested_all.filter(calculation_district__pk=calculation_district)
            high_requested_all = high_requested_all.filter(calculation_district__pk=calculation_district)
            normal_requested_all = normal_requested_all.filter(calculation_district__pk=calculation_district)

        return response.Response({
            'requested_all': requested_all.aggregate(Sum('area'))['area__sum'],
            'lowest_requested_all': lowest_requested_all.aggregate(Sum('area'))['area__sum'],
            'low_requested_all': low_requested_all.aggregate(Sum('area'))['area__sum'],
            'highest_requested_all': highest_requested_all.aggregate(Sum('area'))['area__sum'],
            'high_requested_all': high_requested_all.aggregate(Sum('area'))['area__sum'],
            'normal_requested_all': normal_requested_all.aggregate(Sum('area'))['area__sum']
        }, status=status.HTTP_200_OK)


class SampleListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, PaidServicePermission)
    queryset = Sample.objects.all().order_by('-id')
    serializer_class = SampleSerializer
    filter_fields = ('crop_type', 'outline_number', 'calculation_region', 'calculation_district',)

    def get_queryset(self):
        user = self.request.user
        samples = Sample.objects.all().order_by('-id')
        if user.region is not None:
            samples = Sample.objects.filter(calculation_region=user.region).order_by('-id')
        return samples

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class SampleDetailsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, PaidServicePermission,)
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer


provided_levels = {
    'LOWEST': {
        'color': 'yellow',
        'text': 'Жуда кам'
    },
    'LOW': {
        'color': 'red',
        'text': 'Кам'
    },
    'NORMAL': {
        'color': 'light_blue',
        'text': 'Ўртача'
    },
    'HIGH': {
        'color': 'blue',
        'text': 'Юқори'
    },
    'HIGHEST': {
        'color': 'green',
        'text': 'Жуда юқори'
    }
}


class SampleExcel(views.APIView):
    # permission_classes = (IsAuthenticated, PaidServicePermission,)
    permission_classes = []

    def getStatusColor(self, row, col_num):
        style = xlwt.XFStyle()
        borders = xlwt.Borders()
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        style.borders = borders
        style.font.bold = True
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = xlwt.Style.colour_map[provided_levels[row[col_num]]['color']]
        style.pattern = pattern
        return style

    def get(self, request):
        calculation_region = request.query_params.get("calculation_region")
        crop_type = request.query_params.get("crop_type")
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Tuproq tahlili.xls"'

        wb = xlwt.Workbook(encoding='utf-8', style_compression=2)
        ws = wb.add_sheet('Натижалар')

        # Sheet header, first row
        row_num = 0
        excel_row_num = 0
        columns = ['ID', 'Киритилган сана',
                   'Вилоять', 'Туман',
                   'Ҳудуд номи',
                   'Қатлам қалинлиги',
                   'Хўжалик номи',
                   'ИНН ёки ПИНФЛ',
                   'Контур рақами',
                   'Намуна идентификацион рақами',
                   'Майдони', 'Экин тури',
                   'РН нейтрал (pH =7)', 'NO3  (мг/кг ҳисобида)', 'Коэффициент', 'Таъминланганлик даражаси',
                   'Ҳаракатчан P2O5  (мг/кг ҳисобида)',
                   'Коэффициент', 'Таъминланганлик даражаси', 'Алмашинувчан K20 (мг/кг ҳисобида)',
                   'Коэффициент', 'Таъминланганлик даражаси', 'Гумус % ҳисобида', 'Таъминланганлик даражаси', '',
                   '1 ц - N',
                   '1 ц - P', '1 ц - K',
                   'Жами - N', 'Жами - P', 'Жами - K']
        columns_attributes = ['pk',  # 0
                              'added_at',  # 1
                              'calculation_region__name_uz',  # 2
                              'calculation_district__name_local',  # 3
                              'area_name',  # 0
                              'layer_width',  # 0
                              'farm_name',  # 0
                              'inn_or_pinfl',  # 0
                              'outline_number',  # 4
                              'sample_number',  # 5
                              'area',  # 6
                              'crop_type__name_uz',  # 7
                              'given_phosphorus',  # 8
                              'given_nitrogen',  # 9
                              'coefficient_nitrogen',  # 10
                              'provided_level_nitrogen',  # 11
                              'given_phosphorus',  # 12
                              'coefficient_phosphorus',  # 13
                              'provided_level_phosphorus',  # 14
                              'given_potassium',  # 15
                              'coefficient_potassium',  # 16
                              'provided_level_potassium',  # 17
                              'given_humus',  # 18
                              'provided_level_humus',  # 19
                              'usage_per_centner_nitrogen',  # 20
                              'usage_per_centner_phosphorus',  # 21
                              'usage_per_centner_potassium']  # 22
        header_style = xlwt.XFStyle()
        header_style.font.bold = True
        for col_num in range(len(columns)):
            ws.write(excel_row_num, col_num, columns[col_num], style=header_style)
        if calculation_region:
            rows = Sample.objects.filter(calculation_region__pk=calculation_region).order_by(
                '-added_at', '-calculation_district', '-outline_number').values_list(*columns_attributes)
        elif crop_type:
            rows = Sample.objects.filter(crop_type__pk=crop_type).order_by('-added_at', '-calculation_district',
                                                                           '-outline_number').values_list(
                *columns_attributes
            )
        else:
            rows = Sample.objects.all().order_by('-added_at', '-calculation_district', '-outline_number').values_list(
                *columns_attributes)
        unique_identifier = f"{str(rows[0][1])}{rows[0][3]}{rows[0][4]}"
        usage_per_centner_nitrogen = 0
        usage_per_centner_phosphorus = 0
        usage_per_centner_potassium = 0
        all_usage_per_centner_nitrogen = 0
        all_usage_per_centner_phosphorus = 0
        all_usage_per_centner_potassium = 0
        usage_per_centner_humus = 0
        area = 0

        row_style = xlwt.XFStyle()
        borders = xlwt.Borders()
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        row_style.borders = borders

        bold_text_row_style = xlwt.XFStyle()
        borders = xlwt.Borders()
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        bold_text_row_style.borders = borders
        bold_text_row_style.font.bold = True
        for row in rows:
            row_num += 1
            excel_row_num += 1
            if unique_identifier != f"{str(row[1])}{row[3]}{row[8]}":
                unique_identifier = f"{str(row[1])}{row[3]}{row[8]}"
                ws.write(excel_row_num, 10, area, bold_text_row_style)
                ws.write(excel_row_num, 25, usage_per_centner_nitrogen, bold_text_row_style)
                ws.write(excel_row_num, 26, usage_per_centner_phosphorus, bold_text_row_style)
                ws.write(excel_row_num, 27, usage_per_centner_potassium, bold_text_row_style)
                ws.write(excel_row_num, 28, all_usage_per_centner_nitrogen, bold_text_row_style)
                ws.write(excel_row_num, 29, all_usage_per_centner_phosphorus, bold_text_row_style)
                ws.write(excel_row_num, 30, all_usage_per_centner_potassium, bold_text_row_style)
                usage_per_centner_nitrogen = row[24]
                usage_per_centner_phosphorus = row[25]
                usage_per_centner_potassium = row[26]
                all_usage_per_centner_nitrogen = row[24] * row[10]
                all_usage_per_centner_phosphorus = row[25] * row[10]
                all_usage_per_centner_potassium = row[26] * row[10]
                area = row[10]
                excel_row_num += 1
                for col_num in range(len(row)):
                    if col_num == 15 or col_num == 18 or col_num == 21 or col_num == 23:
                        try:
                            ws.write(excel_row_num, col_num, provided_levels[row[col_num]]['text'],
                                     self.getStatusColor(row, col_num))
                        except KeyError as e:
                            ws.write(excel_row_num, col_num, "Кўрсатилмаган")
                    elif col_num == 24:
                        ws.write(excel_row_num, col_num + 1, row[col_num], row_style)
                        ws.write(excel_row_num, col_num + 2, row[col_num + 1], row_style)
                        ws.write(excel_row_num, col_num + 3, row[col_num + 2], row_style)
                        ws.write(excel_row_num, col_num + 4, row[24] * row[10], row_style)
                        ws.write(excel_row_num, col_num + 5, row[25] * row[10], row_style)
                        ws.write(excel_row_num, col_num + 6, row[26] * row[10], row_style)
                        break
                    elif col_num == 1:
                        ws.write(excel_row_num, col_num, f"{row[1]}", row_style)
                    else:
                        ws.write(excel_row_num, col_num, row[col_num], row_style)
                # usage_per_centner_humus = 0
            else:
                usage_per_centner_nitrogen += row[24]
                usage_per_centner_phosphorus += row[25]
                usage_per_centner_potassium += row[26]
                all_usage_per_centner_nitrogen += row[24] * row[10]
                all_usage_per_centner_phosphorus += row[25] * row[10]
                all_usage_per_centner_potassium += row[26] * row[10]
                # usage_per_centner_humus += row[20]
                area += row[10]
                for col_num in range(len(row)):
                    if col_num == 15 or col_num == 18 or col_num == 21 or col_num == 23:
                        try:
                            ws.write(excel_row_num, col_num, provided_levels[row[col_num]]['text'],
                                     self.getStatusColor(row, col_num))
                        except KeyError as e:
                            ws.write(excel_row_num, col_num, "Кўрсатилмаган")
                    elif col_num == 24:
                        ws.write(excel_row_num, col_num + 1, row[col_num], row_style)
                        ws.write(excel_row_num, col_num + 2, row[col_num + 1], row_style)
                        ws.write(excel_row_num, col_num + 3, row[col_num + 2], row_style)
                        ws.write(excel_row_num, col_num + 4, row[24] * row[10], row_style)
                        ws.write(excel_row_num, col_num + 5, row[25] * row[10], row_style)
                        ws.write(excel_row_num, col_num + 6, row[26] * row[10], row_style)
                        break
                    elif col_num == 1:
                        ws.write(excel_row_num, col_num, f"{row[1]}", row_style)
                    else:
                        ws.write(excel_row_num, col_num, row[col_num], row_style)
        wb.save(response)
        return response
