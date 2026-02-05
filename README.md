# AI Code Reviewer

**Hybrid AI-assisted Python Code Review Tool**  
This project combines static analysis and a simple machine learning model to detect potential code smells in Python code. It provides a REST API using FastAPI.

---

## Features

- **Static Analysis**: Detects common Python code smells using AST:
  - Long functions
  - Unused variables
  - Deeply nested code
- **Machine Learning Prediction**: Uses TF-IDF features and Logistic Regression to predict potential code smells.
- **REST API**: Submit Python code and get back structured feedback (`static_issues` + `ml_prediction`).

---

## Project Structure

ai-code-review/
├── src/
│ ├── api/ # FastAPI endpoints
│ ├── engine/ # Static analysis engine
│ ├── ml/ # ML model and vectorizer
│ └── smells/ # Individual code smell analyzers
├── README.md
├── requirements.txt
└── Procfile


---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/qunneii/ai-code-reviewer.git
cd ai-code-reviewer

2. Create a Python virtual environment

It's recommended to use a virtual environment to manage dependencies:

python3 -m venv venv
source venv/bin/activate   # macOS / Linux
# OR
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

Running the API locally
PYTHONPATH=src uvicorn api.main:app --reload


Open your browser and go to http://127.0.0.1:8000/docs
 to see the Swagger UI.

Submit Python code to /analyze endpoint and get results.

Notes

Do not commit the venv/ folder to GitHub. Add it to .gitignore.

Make sure the ML model (model.joblib) and vectorizer (vectorizer.joblib) are in src/ml/.

Example Request
POST /analyze
{
  "code": "def test():\n    x = 10\n    for i in range(3):\n        if i > 0:\n            print(i)\n    return 5"
}


Example Response:

{
  "static_issues": ["Long function detected", "Deep nesting detected"],
  "ml_prediction": "code_smell"
}

Deployment

The project can be deployed using Railway, Render, or Docker.

The Procfile specifies how to run the FastAPI server.

License

MIT License
