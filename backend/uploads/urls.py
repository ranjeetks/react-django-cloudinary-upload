from django.urls import path
from .views import CloudinaryUploadView

urlpatterns = [
    path("upload/", CloudinaryUploadView.as_view(), name="cloudinary-upload"),
]
