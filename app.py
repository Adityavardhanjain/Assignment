import flask
from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open('loan_outcome_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]
    response = {
        "loan_outcome": "Repaid" if prediction == 1 else "Defaulted",
        "probability": model.predict_proba(input_df).tolist()[0]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
