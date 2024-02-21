from fastapi import FastAPI, UploadFile, File
from PIL import Image
import numpy as np
import io
import pickle
import onnxruntime as rt

app = FastAPI()

# Load ONNX model
onnx_model_path = "C:\Users\USER\Desktop\APP_Test\VGG16.onnx"
onnx_session = rt.InferenceSession(onnx_model_path)

# Define preprocess function
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224))  # Resize image if necessary
    img_array = np.array(img)
    return img_array

# Define endpoint for model inference
@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    try:
        image_bytes = await image.read()
        processed_image = preprocess_image(image_bytes)
        
        # Perform inference using ONNX model
        input_name = onnx_session.get_inputs()[0].name 
        output_name = onnx_session.get_outputs()[0].name
        input_data = {input_name: np.expand_dims(processed_image, axis=0)}
        result = onnx_session.run([output_name], input_data)[0]
        
        # Return prediction result
        return {"prediction": result.tolist()}
    except Exception as e:
        return {"error": str(e)}
