# Loan Outcome Prediction

## Project Overview
This assignment aimed to predict loan outcomes (default or repayment) using user behavioral and financial attributes. I have leveraged simple EDA and the Random Forest machine learning model to do so. The dataset included features such as user age, cash inflow, GPS data, and application timestamps to train and evaluate the model.

## How to Run the Code

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/loan-prediction.git
cd loan-prediction
```

### 2. Install Dependencies
Make sure Python is installed (version >= 3.8). Install required packages:
```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application
```bash
python app.py
```
Access the app locally at `http://127.0.0.1:5000`.

### 4. Prediction Endpoint
Use the `/predict` endpoint to make predictions. Example (via cURL):
```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"age": 25, "cash_incoming_30days": 15000, "gps_fix_count": 200}' \
     http://127.0.0.1:5000/predict
```

## Features Used
- **Age**: Captures user demographic
- **Cash Incoming (30 Days)**: Represents the user's recent financial behavior
- **GPS Fix Count and Accuracy**: Provides insights into user's mobility and consistency
- **Most Common Provider (GPS and Network)**: Tracks user connectivity patterns
- **Application Timestamp**: Allows time-based analysis
- **Derived Time Features**: Extracted from timestamps (hour, weekday, etc.) to improve temporal understanding

## Model Performance Summary
- **Accuracy**: 76%
- **Precision**: 83%
- **Recall**: 70%

## Confusion Matrix
|                    | Predicted Defaulted | Predicted Repaid |
|--------------------|-------------------:|------------------:|
| **Actual Defaulted** |                  3 |               16 |
| **Actual Repaid**    |                  1 |               30 |

## Feature Importance
1. Application Timestamp
2. Age
3. Cash Incoming (30 Days)
4. GPS Fix Count
5. Average GPS Accuracy
