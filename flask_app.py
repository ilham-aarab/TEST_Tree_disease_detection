from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    image_file = request.files['image']
    files = {'image': image_file}
    response = requests.post('http://localhost:8000/predict', files=files)
    prediction = response.json()
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
