from flask import Flask, request, jsonify
import numpy as np
import pickle
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
diabetes_model = pickle.load(open("diabetes.pkl", "rb"))
heart_model = pickle.load(open("heart.pkl", "rb"))
@app.route('/')
def home():
    return "Health Predictor API Running ✅"
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        disease = data['disease']
        features = data['features']
        features = np.array(features).reshape(1, -1)
        if disease == "Diabetes":
            model = diabetes_model
        elif disease == "Heart":
            model = heart_model
        else:
            return jsonify({'error': 'Invalid disease type'})

       prediction = model.predict(features)[0]

        
        try:
            probability = model.predict_proba(features)[0][1]
        except:
            probability = None

        return jsonify({
            'prediction': int(prediction),
            'probability': float(probability) if probability is not None else None
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })
if __name__ == "__main__":
    app.run(debug=True)