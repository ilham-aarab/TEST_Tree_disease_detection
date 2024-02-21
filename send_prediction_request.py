from PIL import Image
import requests
import io

# URL of the image you want to download and send for prediction
image_url = 'https://people.math.sc.edu/Burkardt/data/tif/venus2.tif'

# Download the image
response = requests.get(image_url)

# Check if the request was successful
if response.status_code == 200:
    # Read the image from the response content
    img = Image.open(io.BytesIO(response.content))
    
    # Convert the image to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='TIFF')
    
    # Reset the buffer position to the beginning
    img_bytes.seek(0)
    
    # URL of the FastAPI server endpoint
    url = 'http://127.0.0.1:8000/predict'
    
    # Send the image for prediction to the FastAPI server
    response = requests.post(url, files={"image_file": img_bytes})
    
    # Print the prediction response
    print(response.json())
else:
    print("Failed to download image")
