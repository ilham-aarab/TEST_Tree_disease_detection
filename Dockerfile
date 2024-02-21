# Use the official Python image as a base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app files into the container
COPY app.py .
COPY preprocessing.py .
COPY VGG16.onnx .

# Expose the port where the FastAPI app will run
EXPOSE 8000

# Run the FastAPI app when the container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]