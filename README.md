# 📤 React + Django File Upload (Cloudinary)

![React](https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?logo=vite&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?logo=cloudinary&logoColor=white)

A minimal full-stack micro-demo showing how to upload an image to **Cloudinary** using a simple **Django REST API** and preview it in a **React (Vite + Tailwind)** frontend.

This **version** includes the core upload + preview flow with **no database**, making it lightweight and perfect for beginners.

---

## 🚀 Live Demo

- **Frontend:** https://react-django-cloudinary-upload.vercel.app
- **Backend API:** https://react-django-cloudinary-upload-production.up.railway.app/api/upload/
- **GitHub Repo:** https://github.com/ranjeetks/react-django-cloudinary-upload

---

## ⭐ Features

- Select and preview an image locally  
- Upload to Django backend  
- Store file on Cloudinary  
- Clean JSON response containing `image_url`  
- Simple UI using TailwindCSS  
- No database required  

---

## 🛠 Tech Stack

**Frontend:** React (Vite), TypeScript, Tailwind CSS  
**Backend:** Django REST Framework, Cloudinary SDK, Gunicorn  

---

## 📁 Folder Structure

```
react-django-cloudinary-upload/
│
├── backend/
│   ├── project/
│   ├── uploads/
│   │   ├── views.py
│   │   └── urls.py
│   ├── manage.py
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── App.tsx
    │   ├── components/
    │   │   └── FileUpload.tsx
    │   └── index.css
    ├── vite.config.ts
    └── package.json
```

---

# 🖥 Backend Setup (Django + Cloudinary)

### 1️⃣ Install backend dependencies
```
pip install -r requirements.txt
```

### 2️⃣ Add Cloudinary config to `settings.py`
```python
CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
```

### 3️⃣ Start backend
```
python manage.py runserver
```

_No migrations needed — this version uses no database._

---

# 🎨 Frontend Setup (React + Vite + Tailwind)

### 1️⃣ Install dependencies
```
npm install
```

### 2️⃣ Add `.env`
```
VITE_API_URL=https://your-backend-domain.up.railway.app
```

### 3️⃣ Start frontend
```
npm run dev
```

---

# 🔗 API Endpoint

### **POST /api/upload/**  
Uploads an image to Cloudinary.

#### Request
```
file: <image>
```

#### Success Response
```json
{
  "message": "Upload successful",
  "image_url": "https://res.cloudinary.com/.../image.jpg"
}
```

---

# 🎁 Features

✔ Minimal Django upload API  
✔ Cloudinary integration  
✔ Local file preview  
✔ Simple Tailwind UI  
✔ Working full-stack demo  
✔ No database required  


---

## 👨‍💻 Author  
Made with ❤️ by **Ranjeet Singh**  
GitHub: https://github.com/ranjeet-singh

---

# 📄 License  
Free to use for learning and portfolio.
