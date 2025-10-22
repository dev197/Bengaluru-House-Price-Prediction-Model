from flask import Flask, request, jsonify, send_from_directory
from server import util
import os

# Tell Flask where your frontend files are
app = Flask(__name__, static_folder='../client', template_folder='../client')

# Load model artifacts once at startup
util.load_saved_artifacts()

# Serve frontend (HTML, CSS, JS)
@app.route('/')
def home():
    return send_from_directory('../client', 'app.html')

# Serve any static files (like JS, CSS)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('../client', path)

# API: Get all location names
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# API: Predict house price
@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print('Starting Flask server for Bengaluru House Price Prediction...')
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
