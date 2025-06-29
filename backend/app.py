from flask import Flask, request, jsonify, send_from_directory
from utils.background_removal import remove_background
import os

app = Flask(__name__, static_folder='../frontend/static', static_url_path='/static')

# memastikan direktori gambar ada
os.makedirs("images", exist_ok=True)

@app.route('/remove-background', methods=['POST'])
def remove_background_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    image_path = f"images/{image.filename}"
    image.save(image_path)
    print(f"Image saved at: {image_path}")

    try:
        output_image_path = remove_background(image_path)
        print(f"Processed image saved at: {output_image_path}")
        
        # Ensure the static folder exists
        static_folder = os.path.abspath("../frontend/static")
        os.makedirs(static_folder, exist_ok=True)
        
        # Move the processed image to the static folder
        static_image_path = os.path.join(static_folder, os.path.basename(output_image_path))
        os.rename(output_image_path, static_image_path)
        print(f"Image moved to static folder: {static_image_path}")
        
        return jsonify({'processed_image_url': f"/static/{os.path.basename(static_image_path)}"}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    return send_from_directory('../frontend', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)