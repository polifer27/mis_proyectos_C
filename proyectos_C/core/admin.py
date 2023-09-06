from django.contrib import admin
from .models import Project, FilesAdmin

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')



admin.site.register(Project, ProjectAdmin)
admin.site.register(FilesAdmin)