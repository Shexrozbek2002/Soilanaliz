# Register your models here.
from django.contrib import admin

# Register your models here.
# from core.refs.models import Country, Region
from coredata.models import District, Region, Reference, User, SamplesSniffer
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


class UsersAdmin(DjangoUserAdmin):
    list_display = ('pk', 'username', 'first_name', 'last_name', 'email')
    model = User
    fieldsets = DjangoUserAdmin.fieldsets + (
        (None, {
            'fields': ('user_role', 'district', 'region', 'status'),
        }),
    )
    list_display_links = ('username',)


admin.site.register(User, UsersAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_local', 'region')
    list_display_links = ('name_local',)
    search_fields = ('name_local', 'name_ru', 'name_en')
    list_select_related = ('region',)


admin.site.register(District, DistrictAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_uz', 'coefficient')
    list_display_links = ('name_uz',)
    search_fields = ('name_uz', 'name_ru', 'name_en')


admin.site.register(Region, RegionAdmin)


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_uz', 'type')
    list_display_links = ('pk', 'name_uz',)
    ordering = ('-added_at',)


admin.site.register(Reference, ReferenceAdmin)


class SamplesSnifferAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_uz', 'limit', 'added_at')
    list_display_links = ('name_uz',)
    ordering = ('-added_at',)


admin.site.register(SamplesSniffer, SamplesSnifferAdmin)
