import tensorflow as tf
import cv2
import numpy as np

# Load trained model
model = tf.keras.models.load_model("lung_cancer_model.h5")

IMG_SIZE = 224

def predict_image(path):

    img = cv2.imread(path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.reshape(img, (1, IMG_SIZE, IMG_SIZE, 3))

    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        print("✅ Normal_No Disease")
    else:
        print("✅ Tumor Detected")

# Test image
predict_image("test_images/Normal case (3).jpg")