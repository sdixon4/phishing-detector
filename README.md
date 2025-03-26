# 🛡️ Phishing Detection Tool

This is an AI-powered Flask web application that uses **Natural Language Processing (NLP)** to classify emails as either phishing or safe. It leverages Hugging Face Transformers to make real-time predictions.

---

## 🚀 Features

- ⚙️ **NLP Model**: Fine-tuned transformer model (e.g., BERT or DistilBERT)
- 🌐 **Flask Web App**: User-friendly interface for inputting and analyzing email content
- ⚡ **Real-Time Inference**: Instantly classifies emails as phishing or legitimate
- 🧪 **Interactive API Testing**: Route available for direct JSON-based requests
- 💡 **Clear Feedback**: Shows probability/confidence score for each classification

---

## 💻 Demo

Paste your email text and get results instantly using the web UI.

---

## 📡 API Usage

Send a POST request to `/predict`:

```bash
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"email": "Urgent! Your account has been compromised. Click this link..."}'

