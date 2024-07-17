from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    MODEL = tf.keras.models.load_model(r"D:\vs code files new\2024\project\h5format\model_fixed.h5")
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")

CLASS_NAMES = ['bacterial_blight', 'curl_virus', 'fussarium_wilt', 'healthy']

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    try:
        image = np.array(Image.open(BytesIO(data)))
        print("Image read successfully")
        return image
    except Exception as e:
        print(f"Error reading image: {e}")
        return None

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    try:
        image = read_file_as_image(await file.read())
        if image is None:
            return {"error": "Invalid image"}
        
        img_batch = np.expand_dims(image, 0)
        print("Image batch created")

        predictions = MODEL.predict(img_batch)
        print(f"Predictions: {predictions}")

        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])
        return {
            'class': predicted_class,
            'confidence': float(confidence)
        }
    except Exception as e:
        print(f"Error in prediction: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
