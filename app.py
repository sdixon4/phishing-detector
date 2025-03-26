from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
classifier = pipeline("text-classification")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    email = data.get("email", "")

    if not email:
        return jsonify({"error": "Missing 'email' in request body"}), 400

    result = classifier(email)[0]
    return jsonify({
        "email": email,
        "label": result["label"],
        "confidence": round(result["score"], 4)
    })

@app.route("/", methods=["GET"])
def home():
    return "<h3>Phishing Detector API is running ✅</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
