from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import UploadSerializer, UploadedFileSerializer
from .models import UploadedFile
import cloudinary.uploader

class CloudinaryUploadView(APIView):
    # production: restrict to IsAuthenticated
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uploaded_file = serializer.validated_data["file"]

        try:
            # Use cloudinary.uploader.upload. Server-side credentials are used (signed).
            # We set folder to your preset folder; you can also pass upload_preset if desired.
            resp = cloudinary.uploader.upload(
                uploaded_file,
                folder="react_uploads",           # matches your preset folder (optional)
                resource_type="auto",              # auto detect (image, raw, video)
                use_filename=True,
                unique_filename=False,
                overwrite=False,
                # upload_preset="secure_upload",   # optional. Since server is signed, not required
            )
        except Exception as e:
            return Response({"detail": "Cloudinary upload failed", "error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)

        # resp contains many fields including public_id, url, secure_url, bytes, format, resource_type, width, height
        obj = UploadedFile.objects.create(
            original_filename=uploaded_file.name,
            public_id=resp.get("public_id"),
            url=resp.get("url"),
            secure_url=resp.get("secure_url"),
            resource_type=resp.get("resource_type"),
            file_format=resp.get("format"),
            bytes=resp.get("bytes") or 0,
            width=resp.get("width"),
            height=resp.get("height"),
            uploaded_by=request.user if request.user.is_authenticated else None,
        )
        out = UploadedFileSerializer(obj)
        return Response(out.data, status=status.HTTP_201_CREATED)