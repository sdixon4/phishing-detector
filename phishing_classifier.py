from transformers import pipeline

# Load a sentiment-analysis model (we'll repurpose it for phishing)
classifier = pipeline("text-classification")

# Sample emails
emails = [
    "Your account has been suspended. Click here to verify your login.",
    "Hey Shelby, just checking in to see how your projects are going!",
    "We've noticed unusual activity in your bank account. Act now to avoid closure.",
    "Don't forget our group study session this Friday."
]

for email in emails:
    result = classifier(email)[0]
    print(f"\nEMAIL: {email}")
    print(f"Prediction: {result['label']} (confidence: {round(result['score'], 2)})")
