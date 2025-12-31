# app.py
import json
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model/model.pkl")
model = joblib.load(MODEL_PATH)

def lambda_handler(event, context):
    """
    AWS Lambda handler for ML inference.
    
    Expected input format:
    {
        "body": "{\"value\": 30}"
    }
    
    Returns:
    {
        "statusCode": 200,
        "body": "{\"input\": 30, \"prediction\": 1}"
    }
    """
    try:
        # Parse request body
        body = json.loads(event["body"])
        value = body["value"]
        
        # Make prediction
        prediction = model.predict([[value]])[0]
        
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "input": value,
                "prediction": int(prediction)
            })
        }
    except KeyError as e:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": f"Missing required field: {str(e)}"
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }
