from django.contrib import admin

from .models import App


class AppAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'created_on']

    fields = ['name', 'slug', 'description', 'created_on']


admin.site.register(App, AppAdmin)