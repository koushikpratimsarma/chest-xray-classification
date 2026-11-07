
from pathlib import Path

import numpy as np
import tensorflow as tf

from flask import Flask, request, jsonify, render_template
from PIL import Image, UnidentifiedImageError
from werkzeug.utils import secure_filename
from io import BytesIO


# Initialize Flask application
app = Flask(__name__)

# Maximum upload size: 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

# Project paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "chest_xray_model.keras"

# Image configuration
IMAGE_SIZE = (224, 224)

# Load trained model
model = tf.keras.models.load_model(MODEL_PATH)

print("Chest X-ray model loaded successfully!")


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():

    # Check whether image was uploaded
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "Please select an image"}), 400

    # Validate file extension
    filename = secure_filename(file.filename)

    allowed_extensions = {".jpg", ".jpeg", ".png"}

    if Path(filename).suffix.lower() not in allowed_extensions:
        return jsonify({"error": "Only JPG and PNG images are allowed"}), 400

    try:
        # Read and preprocess image
        image = Image.open(BytesIO(file.read())).convert("RGB")
        image = image.resize(IMAGE_SIZE)

        image_array = np.array(image, dtype=np.float32)
        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(image_array, verbose=0)[0][0]

        print("Raw model prediction:", prediction)
        print("Raw model prediction:", prediction)
        # Our training label mapping:
        # 0 = Abnormal
        # 1 = Normal

        if prediction >= 0.5:
            predicted_class = "Normal"
            model_score = float(prediction)
        else:
            predicted_class = "Abnormal"
            model_score = float(1 - prediction)

        return jsonify({
            "prediction": predicted_class,
            "model_score": round(model_score * 100, 2),
            "message": "Educational research output only. Not a medical diagnosis."
        })

    except (UnidentifiedImageError, OSError):
        return jsonify({"error": "The uploaded file is not a valid image"}), 400

    except Exception:
        app.logger.exception("Prediction failed")
        return jsonify({"error": "Unable to process the image"}), 500


# Handle oversized uploads
@app.errorhandler(413)
def file_too_large(error):
    return jsonify({"error": "Image size must be less than 5 MB"}), 413


if __name__ == "__main__":
    app.run(debug=True)
