from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
import cloudinary.uploader

class CloudinaryUploadView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Cloudinary upload
            resp = cloudinary.uploader.upload(
                uploaded_file,
                folder="react_uploads",
                resource_type="auto",
            )
        except Exception as e:
            return Response(
                {"error": "Cloudinary upload failed", "detail": str(e)},
                status=status.HTTP_502_BAD_GATEWAY
            )

        # Minimal clean response for FREE version
        return Response({
            "message": "Upload successful",
            "image_url": resp.get("secure_url")
        }, status=status.HTTP_201_CREATED)
