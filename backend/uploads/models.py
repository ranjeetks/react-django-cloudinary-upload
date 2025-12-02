from django.db import models
from django.conf import settings

class UploadedFile(models.Model):
    original_filename = models.CharField(max_length=512)
    public_id = models.CharField(max_length=512, db_index=True)   # Cloudinary public_id
    url = models.URLField(max_length=2000)                        # direct HTTP URL
    secure_url = models.URLField(max_length=2000, blank=True, null=True)
    resource_type = models.CharField(max_length=32, blank=True, null=True)
    file_format = models.CharField(max_length=32, blank=True, null=True)
    bytes = models.PositiveIntegerField(default=0)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_filename} ({self.public_id})"