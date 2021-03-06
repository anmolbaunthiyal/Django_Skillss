from django.contrib import admin
from .models import Features


class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'interest')


admin.site.register(Features, FeaturesAdmin)
