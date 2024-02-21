# Use the official Python image as a base
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files into the container
COPY flask_app.py .
COPY index.html templates/

# Expose the port where the Flask app will run
EXPOSE 5000

# Run the Flask app when the container starts
CMD ["python", "flask_app.py"]
