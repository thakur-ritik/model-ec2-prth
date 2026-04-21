from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("model.joblib")

@app.route("/")
def home():
    return "ML Model API is running 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["input"]
        prediction = model.predict([data])
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
