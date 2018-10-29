from django.contrib import admin
from .models import ReadTime,ReadDetail

@admin.register(ReadTime)
class ReadTimeAdmin(admin.ModelAdmin):
    list_display=('read_time','content_object')

@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display=('date','read_time','content_object')
