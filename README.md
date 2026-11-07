# AI-Based Chest X-ray Image Classification

## 1. Project Overview

This project is an AI-based web application that uses Deep Learning to classify chest X-ray images into two categories:

- **Normal**
- **Abnormal**

The system uses a Convolutional Neural Network (CNN) with MobileNetV2 transfer learning. A Flask web application provides an interface where users can upload chest X-ray images and view the model's prediction.

This project is developed for educational and research purposes only. It is not intended for medical diagnosis.

## 2. Objectives

- Develop a deep learning model for chest X-ray image classification.
- Apply transfer learning using MobileNetV2.
- Build a web interface for image uploading and prediction.
- Integrate the trained model with Flask.
- Evaluate model performance using standard classification metrics.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| TensorFlow / Keras | Deep learning |
| MobileNetV2 | Transfer learning |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Model evaluation |
| Flask | Backend web framework |
| HTML, CSS, JavaScript | Frontend development |

## 4. Project Structure

```text
chest-xray-classification/
├── dataset/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── model_training.ipynb
├── models/
│   ├── best_chest_xray_model.keras
│   └── chest_xray_model.keras
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 5. Model Information

- Architecture: MobileNetV2
- Learning approach: Transfer Learning
- Input image size: 224 × 224
- Number of classes: 2
- Output activation: Sigmoid
- Loss function: Binary Crossentropy
- Optimizer: Adam

## 6. Installation and Setup

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd chest-xray-classification
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Ensure the trained model is available inside the `models/` directory.

Run the application:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

## 7. Application Workflow

1. User opens the web application.
2. User uploads a chest X-ray image.
3. Flask receives and validates the image.
4. The image is resized and passed to the trained MobileNetV2 model.
5. The model predicts Normal or Abnormal.
6. The prediction is displayed on the web interface.

## 8. Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Add the actual test-set evaluation results here after reviewing the training notebook.

## 9. Limitations

- The model is trained on a limited dataset.
- Performance may vary with images from different sources.
- The classification categories are limited to Normal and Abnormal.
- The model has not been validated for clinical use.
- The data split is image-based and may not guarantee patient-level separation.

## 10. Disclaimer

This application is an educational and research prototype. Its predictions are not medical diagnoses and must not be used for clinical decision-making.

## 11. Dataset Attribution

Include the original dataset source, author attribution, and applicable CC BY 4.0 license information here. Refer to the original dataset page for attribution details.
