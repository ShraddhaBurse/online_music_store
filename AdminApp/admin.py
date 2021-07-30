from django.contrib import admin

from AdminApp.models import Category,Song

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name')

class SongAdmin(admin.ModelAdmin):
    list_display = ('id','sname','artist','movie','imageurl','audio_file','duration')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Song,SongAdmin) 