from django.contrib import admin
from .models import Blog,BlogType

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display=('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('id','title','blog_type','content','author','get_read_time','created_time','last_updated_time')

'''@admin.register(ReadTime)
class ReadTimeAdmin(admin.ModelAdmin):
    list_display=('read_time','blog')
    '''
