from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load trained model
model = load_model("my_model.keras")

# Class labels
classes = ["Early Blight", "Late Blight", "Healthy"]

# Remedies
remedies = {
    "Healthy": "Your plant is healthy. No action needed.",
    "Early Blight": "Use neem oil spray and remove affected leaves.",
    "Late Blight": "Apply fungicide and avoid overwatering."
}

# Load test image
img = image.load_img("test.jpg", target_size=(224,224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0

# Predict
prediction = model.predict(img_array)
result = classes[np.argmax(prediction)]

print("Disease:", result)
print("Solution:", remedies[result])