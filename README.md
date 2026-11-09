# AI-Based Lung Cancer Detection System Using Deep Learning

An intelligent medical diagnostic desktop application that assists healthcare professionals in detecting lung cancer from chest CT and MRI scans using Deep Learning (Convolutional Neural Networks with Transfer Learning).

---

## 📌 Project Overview

Lung cancer is one of the leading causes of cancer-related mortality globally. Early and accurate detection significantly improves patient survival rates. This project provides an automated, AI-powered diagnostic tool with a graphical user interface (GUI) designed for medical practitioners. 

Doctors can securely log into the system, upload patient CT/MRI scans, and receive an instant prediction (**Normal** vs. **Tumor Detected**) along with a **confidence score**, **risk level**, and automated clinical recommendations.

---

## 🚀 Key Features

* **Secure Medical Authentication:** Restricted-access login portal for verified medical personnel.
* **Transfer Learning Architecture:** Utilizes **MobileNetV2** pre-trained on ImageNet, fine-tuned with custom classification and dropout layers.
* **High Diagnostic Accuracy:** Achieved **~98.8% validation accuracy** on the test dataset.
* **Interactive Desktop GUI:** Built with **Tkinter**, featuring scan preview, dynamic progress indicators, and patient diagnosis reporting.
* **Automated Risk Stratification:** Categorizes detected cases into **High**, **Medium**, or **Low** risk levels to guide immediate clinical action.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.9+
* **Deep Learning Framework:** TensorFlow 2.x / Keras
* **Base Architecture:** MobileNetV2 (Transfer Learning)
* **Computer Vision:** OpenCV (`opencv-python`), Pillow (`PIL`)
* **Numerical Processing:** NumPy, Scikit-learn
* **GUI / Frontend:** Tkinter

---

## 📂 Project Structure

```text
├── dataset/                        # Image dataset categorized into cancer and normal
│   ├── cancer/                     # CT/MRI scans showing malignancy
│   └── normal/                     # Healthy lung CT/MRI scans
├── test_images/                    # Sample CT/MRI scans for quick testing
├── lung_cancer_model.h5            # Pre-trained deep learning model (~98.8% accuracy)
├── login.py                        # Entry point: Medical Login Portal GUI
├── lcd_cnn.py                      # Main Application: Diagnostic GUI & Prediction Engine
├── train.py                        # Model training script with MobileNetV2
├── test.py                         # Model evaluation script
├── requirements.txt                # Python package dependencies
├── Lung_Cancer_Project_Report.docx # Comprehensive academic project documentation
└── README.md                       # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sairaj565/lung-cancer-detection-ai.git
cd lung-cancer-detection-ai
```

### 2. Create and Activate a Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🖥️ How to Run the Application

1. **Launch the Login Portal:**
   ```bash
   python login.py
   ```
2. **Enter Credentials:**
   * **Username:** `admin`
   * **Password:** `1234`
3. **Analyze Scan:**
   * Click **"Predict MRI / CT Image"**
   * Select a scan from the `test_images/` folder
   * View the instant classification, confidence bar, and patient diagnosis report.

---

## 📊 Model Training & Methodology

1. **Preprocessing & Augmentation:** Input scans are resized to `224x224x3` and normalized (`rescale=1./255`). Data augmentation includes rotation, zoom, shear, and horizontal flips to prevent overfitting.
2. **Transfer Learning:** The feature extractor leverages pre-trained MobileNetV2 base weights (`include_top=False`).
3. **Classification Head:**
   * Global Average Pooling 2D
   * Dense Layer (128 units, ReLU activation)
   * Dropout (0.5 rate)
   * Output Dense Layer (1 unit, Sigmoid activation for binary classification)
4. **Optimization:** Trained using the Adam optimizer (`learning_rate=0.0001`) with Binary Cross-Entropy loss over 15 epochs.

---

## 📜 Academic Acknowledgment
Developed as an academic capstone project at **Gokula Krishna College of Engineering** to demonstrate the real-world application of Convolutional Neural Networks in healthcare diagnostics.
