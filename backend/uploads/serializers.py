from rest_framework import serializers
from .models import UploadedFile

# class CloudinarySignatureSerializer(serializers.Serializer):
#     timestamp = serializers.IntegerField()
#     signature = serializers.CharField()
#     cloud_name = serializers.CharField()
#     api_key = serializers.CharField()
#     upload_preset = serializers.CharField()
#     folder = serializers.CharField()


ALLOWED_EXTENSIONS = {"jpg","jpeg","png","gif","webp","pdf"}  # update as needed
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

class UploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, f):
        # size validation
        if f.size > MAX_FILE_SIZE:
            raise serializers.ValidationError("File too large. Max 10 MB.")
        # extension validation
        name = f.name.lower()
        if "." in name:
            ext = name.rsplit(".",1)[1]
        else:
            ext = ""
        if ext not in ALLOWED_EXTENSIONS:
            raise serializers.ValidationError(f"Unsupported file type: .{ext}")
        return f

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = "__all__"