from django.contrib import admin
from contents.models import Content, Image, FollowRelation


# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image
    
class ContentAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('user', 'created_at','text')
    
admin.site.register(Content, ContentAdmin)

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Image, ImageAdmin)

class FollowRelationAdmin(admin.ModelAdmin):
    pass

admin.site.register(FollowRelation, FollowRelationAdmin)