from django.contrib import admin
from django.forms import Textarea
from django.db import models
from tethys_config.models import SettingsCategory, Setting


class SettingInline(admin.TabularInline):
    fields = ('name', 'content', 'date_modified')
    readonly_fields = ('name','date_modified')
    model = Setting
    extra = 0

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 65})},
    }

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class SettingCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    readonly_fields = ('name',)
    inlines = [SettingInline]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(SettingsCategory, SettingCategoryAdmin)