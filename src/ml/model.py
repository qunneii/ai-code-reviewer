import joblib

model = joblib.load("src/ml/model.joblib")
vectorizer = joblib.load("src/ml/vectorizer.joblib")


def predict_smell(code: str) -> bool:
    vec = vectorizer.transform([code])
    prediction = model.predict(vec)
    return bool(prediction[0])
