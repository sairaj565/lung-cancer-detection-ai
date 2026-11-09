# ============================================
# Lung Cancer Detection System (FINAL VERSION)
# ============================================

import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
import cv2

# ==============================
# LOAD TRAINED MODEL
# ==============================
model = tf.keras.models.load_model("lung_cancer_model.h5")

IMG_SIZE = 224
MODEL_ACCURACY = "98.8%"

# ==============================
# MAIN WINDOW
# ==============================
root = tk.Tk()
root.title("Lung Cancer Detection System")
root.geometry("1000x700")
root.resizable(True, True)

# ==============================
# BACKGROUND IMAGE
# ==============================
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((1000, 700))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

root.bg_photo = bg_photo  # Prevent garbage collection

# ==============================
# TITLE
# ==============================
title = tk.Label(
    root,
    text="Lung Cancer Detection Using Deep Learning",
    font=("Arial", 20, "bold"),
    bg="black",
    fg="white"
)
title.pack(pady=10)

# ==============================
# IMAGE DISPLAY
# ==============================
img_label = tk.Label(root, bg="black")
img_label.pack(pady=5)

# ==============================
# RESULT TEXT
# ==============================
result_label = tk.Label(
    root,
    text="Upload CT / MRI Image",
    font=("Arial", 16, "bold"),
    bg="black",
    fg="cyan"
)
result_label.pack(pady=10)

# ==============================
# CONFIDENCE BAR
# ==============================
progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=400,
    mode="determinate"
)
progress.pack(pady=5)

confidence_label = tk.Label(
    root,
    text="Confidence : 0%",
    font=("Arial", 12),
    bg="black",
    fg="white"
)
confidence_label.pack()

# ==============================
# DIAGNOSIS PANEL
# ==============================
diagnosis_label = tk.Label(
    root,
    text="Diagnosis Report",
    font=("Arial", 12),
    bg="black",
    fg="yellow",
    justify="left"
)
diagnosis_label.pack(pady=10)

# ==============================
# MODEL INFO
# ==============================
model_info = tk.Label(
    root,
    text=f"Model Accuracy : {MODEL_ACCURACY}",
    font=("Arial", 12, "bold"),
    bg="black",
    fg="lime"
)
model_info.pack(side="bottom", pady=10)


# ==============================
# RESET UI FUNCTION
# ==============================
def reset_ui():
    result_label.config(text="Upload CT / MRI Image", fg="cyan")
    progress["value"] = 0
    confidence_label.config(text="Confidence : 0%")
    diagnosis_label.config(text="Diagnosis Report")
    img_label.config(image="")
    img_label.image = None


# ==============================
# PREDICTION FUNCTION
# ==============================
def predict_image(path):

    result_label.config(text="Analyzing Scan...", fg="white")
    root.update()

    img = cv2.imread(path)

    if img is None:
        result_label.config(text="Invalid Image!", fg="red")
        return

    img_resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img_norm = img_resized / 255.0
    img_input = np.reshape(img_norm, (1, IMG_SIZE, IMG_SIZE, 3))

    prediction = model.predict(img_input)[0][0]

    # ======================
    # RESULT + CONFIDENCE
    # ======================
    if prediction > 0.5:
        result = "NORMAL"
        color = "lime"
        disease = "No Cancer Detected"
        confidence = round(prediction * 100, 2)
    else:
        result = "TUMOR DETECTED"
        color = "red"
        disease = "Possible Lung Cancer"
        confidence = round((1 - prediction) * 100, 2)

    # ======================
    # RISK LEVEL LOGIC
    # ======================
    if result == "TUMOR DETECTED":
        if confidence > 85:
            risk = "HIGH"
        elif confidence > 60:
            risk = "MEDIUM"
        else:
            risk = "LOW"
    else:
        risk = "LOW"

    # ======================
    # UPDATE GUI
    # ======================
    result_label.config(text=result, fg=color)
    progress["value"] = confidence
    confidence_label.config(text=f"Confidence : {confidence}%")

    diagnosis_text = f"""
Patient Diagnosis Report
--------------------------------
Prediction : {disease}
Confidence : {confidence} %
Risk Level : {risk}

Recommendation :
✔ Consult Radiologist
✔ Further CT Analysis Suggested
"""

    diagnosis_label.config(text=diagnosis_text)

    # Display Image
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_pil = img_pil.resize((250, 250))

    imgtk = ImageTk.PhotoImage(img_pil)
    img_label.configure(image=imgtk)
    img_label.image = imgtk

    root.focus_set()  # Remove button focus highlight


# ==============================
# IMAGE UPLOAD
# ==============================
def upload_image():
    reset_ui()  # Clear previous result

    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )

    if file_path:
        predict_image(file_path)


# ==============================
# BUTTON
# ==============================
btn = tk.Button(
    root,
    text="Predict MRI / CT Image",
    command=upload_image,
    font=("Arial", 14, "bold"),
    bg="white",
    fg="black"
)
btn.pack(pady=15)

# ==============================
# START APP
# ==============================
root.mainloop()