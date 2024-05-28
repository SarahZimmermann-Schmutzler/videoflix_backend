from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from videoflix.models import Video

# Register your models here.
admin.site.register(Video)

# class VideoResource(resources.ModelResource):
#     class Meta:
#         model = Video

# class VideoAdmin(ImportExportModelAdmin):
#     pass

# admin.site.register(Video, VideoAdmin)