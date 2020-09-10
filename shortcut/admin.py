from django.contrib import admin
from .models import URL


# Register your models here.
@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('user', 'url_id', 'link', 'usage', 'created')
    list_filter = ('created', )
