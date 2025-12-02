from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ("original_filename", "public_id", "resource_type", "file_format", "bytes", "created_at", "uploaded_by")
    search_fields = ("original_filename", "public_id")