import pickle
import numpy as np
from flask import Flask, render_template, request

# Load model
model = pickle.load(open('model_svc.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input values from form
        features = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal'])
        ]

        final_features = np.array([features])
        prediction = model.predict(final_features)[0]

        result = "❤️ No Heart Disease Detected" if prediction == 0 else "⚠️ High Chance of Heart Disease"

        return render_template("result.html", prediction=result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
