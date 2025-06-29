# Background Removal Project

A web application for removing backgrounds from images using Python (Flask) for the backend and HTML + Tailwind CSS for the frontend.

---

## Project Structure

```
background-removal-project/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── images/
│   │   └── ... (uploaded and processed images)
│   └── utils/
│       ├── background_removal.py
│       └── __pycache__/
├── frontend/
│   ├── index.html
│   ├── styles.css
│   ├── tailwind.config.js
│   └── static/
│       └── ... (processed images for download)
└── README.md
```

---

## Backend

- **`app.py`**  
  Main Flask application. Handles image upload, background removal requests, and serves the frontend.

- **`requirements.txt`**  
  Python dependencies for the backend.

- **`images/`**  
  Temporary storage for uploaded and processed images (not tracked by git).

- **`utils/background_removal.py`**  
  Contains the `remove_background(image_path)` function using `rembg` to process images.

---

## Frontend

- **`index.html`**  
  Main HTML file for the web interface.

- **`styles.css`**  
  Custom styles (optional, extends Tailwind).

- **`tailwind.config.js`**  
  Tailwind CSS configuration.

- **`static/`**  
  Folder for processed images to be served/downloaded by users.

---

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd background-removal-project
   ```

2. **Set up the backend:**
   ```sh
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the backend server:**
   ```sh
   python app.py
   ```

4. **Open the frontend:**
   - Open `frontend/index.html` in your browser, or
   - Access via `http://127.0.0.1:5000` if using Flask's static serving.

---

## Usage

- Upload an image via the web interface.
- The backend processes the image and returns a background-removed version.
- Download the processed image from the frontend.

---

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

---