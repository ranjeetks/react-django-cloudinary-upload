import { useState, useRef } from "react";

export default function FileUpload() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [progress, setProgress] = useState<number>(0);
  const [uploadedUrl, setUploadedUrl] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);
  const dropRef = useRef<HTMLDivElement | null>(null);

  const handleFileSelect = (file: File) => {
    setSelectedFile(file);
    setUploadedUrl(null);
    setMessage(null);
    setProgress(0);
    setPreview(URL.createObjectURL(file));
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    if (file) handleFileSelect(file);
    dropRef.current?.classList.remove("border-blue-500");
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    dropRef.current?.classList.add("border-blue-500");
  };

  const handleDragLeave = () => {
    dropRef.current?.classList.remove("border-blue-500");
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setMessage("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch("http://127.0.0.1:8000/api/upload/", {
        method: "POST",
        body: formData,
      });

      setProgress(100);

      const data = await response.json();
      setUploadedUrl(data.secure_url);
      setMessage("Upload successful!");
    } catch {
      setMessage("Upload failed.");
    }
  };

  return (
    <div className="min-h-screen flex justify-center items-center bg-gray-50 p-4">
      <div className="w-full max-w-xl bg-white shadow-md rounded-xl p-8 border border-gray-200">

        {/* Title */}
        <h1 className="text-xl font-semibold text-gray-800 text-center mb-6">
          File Upload with Preview
        </h1>

        {/* Drag & Drop Zone */}
        <div
          ref={dropRef}
          onDrop={handleDrop}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          className="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center cursor-pointer bg-gray-50 hover:bg-gray-100 transition"
        >
          <input
            type="file"
            className="hidden"
            id="fileInput"
            onChange={(e) =>
              e.target.files?.[0] && handleFileSelect(e.target.files[0])
            }
          />

          <label htmlFor="fileInput" className="cursor-pointer select-none">
            <p className="text-gray-700 font-medium">Select a file</p>
            <p className="text-sm text-gray-500 mt-1">
              or drag and drop here
            </p>
          </label>
        </div>

        {/* Preview */}
        {preview && (
          <div className="mt-6">
            <p className="font-medium text-gray-700 mb-2">Preview:</p>
            <div className="w-full h-64 bg-gray-100 rounded-lg flex items-center justify-center overflow-hidden border">
              <img
                src={preview}
                alt="preview"
                className="w-full h-full object-cover"
              />
            </div>
          </div>
        )}

        {/* Upload Button */}
        <button
          onClick={handleUpload}
          disabled={!selectedFile}
          className="mt-6 w-full bg-blue-600 text-white py-3 rounded-lg font-medium hover:bg-blue-700 transition disabled:bg-gray-400"
        >
          Upload File
        </button>

        {/* Progress Bar */}
        {progress > 0 && (
          <div className="w-full bg-gray-200 rounded-full h-3 mt-4">
            <div
              style={{ width: `${progress}%` }}
              className="bg-blue-600 h-3 rounded-full transition-all"
            ></div>
          </div>
        )}

        {/* Status Message */}
        {message && (
          <p className="mt-4 text-center font-medium text-gray-700">
            {message}
          </p>
        )}

        {/* View File */}
        {uploadedUrl && (
          <a
            href={uploadedUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="block mt-4 text-center text-blue-700 font-medium hover:underline"
          >
            View Uploaded File
          </a>
        )}
      </div>
    </div>
  );
}