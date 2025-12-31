# app.py
import json
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model/model.pkl")
model = joblib.load(MODEL_PATH)

def lambda_handler(event, context):
    """
    AWS Lambda handler for ML inference.
    Handles both GET (documentation) and POST (prediction) requests.
    """
    http_method = event.get("httpMethod", "POST")
    
    # Handle GET request - show API documentation
    if http_method == "GET":
        return get_documentation()
    
    # Handle POST request - make prediction
    return make_prediction(event)


def get_documentation():
    """Return HTML documentation for the API."""
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 ML Inference API</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh;
            color: #e4e4e4;
            padding: 40px 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 10px;
            background: linear-gradient(90deg, #00d9ff, #00ff88);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            text-align: center;
            color: #888;
            margin-bottom: 40px;
        }
        .card {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }
        .card h2 {
            color: #00d9ff;
            margin-bottom: 15px;
            font-size: 1.3rem;
        }
        .status {
            display: inline-block;
            background: linear-gradient(90deg, #00ff88, #00d9ff);
            color: #1a1a2e;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.9rem;
        }
        code {
            background: rgba(0, 217, 255, 0.1);
            padding: 3px 8px;
            border-radius: 4px;
            color: #00d9ff;
            font-family: 'Consolas', monospace;
        }
        pre {
            background: #0d1117;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 15px 0;
            border: 1px solid #30363d;
        }
        pre code {
            background: none;
            padding: 0;
            color: #e4e4e4;
        }
        .method {
            display: inline-block;
            background: #238636;
            color: white;
            padding: 3px 10px;
            border-radius: 4px;
            font-weight: bold;
            font-size: 0.8rem;
            margin-right: 10px;
        }
        .endpoint {
            color: #00d9ff;
            font-family: 'Consolas', monospace;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        th {
            color: #00d9ff;
        }
        .try-it {
            background: linear-gradient(90deg, #00d9ff, #00ff88);
            color: #1a1a2e;
            border: none;
            padding: 12px 30px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            font-size: 1rem;
            transition: transform 0.2s;
        }
        .try-it:hover { transform: scale(1.05); }
        #result {
            margin-top: 20px;
            padding: 15px;
            background: #0d1117;
            border-radius: 8px;
            display: none;
            border: 1px solid #30363d;
        }
        input[type="number"] {
            background: #0d1117;
            border: 1px solid #30363d;
            color: #e4e4e4;
            padding: 12px;
            border-radius: 8px;
            width: 150px;
            font-size: 1rem;
            margin-right: 10px;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #666;
        }
        .footer a {
            color: #00d9ff;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 ML Inference API</h1>
        <p class="subtitle">Serverless Machine Learning on AWS Lambda</p>
        
        <div class="card">
            <span class="status">✓ API Online</span>
            <h2 style="margin-top: 20px;">API Endpoint</h2>
            <p><span class="method">POST</span><span class="endpoint">/predict</span></p>
        </div>
        
        <div class="card">
            <h2>📝 Request Format</h2>
            <pre><code>{
    "value": 30
}</code></pre>
        </div>
        
        <div class="card">
            <h2>📤 Response Format</h2>
            <pre><code>{
    "input": 30,
    "prediction": 1
}</code></pre>
        </div>
        
        <div class="card">
            <h2>🔬 Model Behavior</h2>
            <table>
                <tr><th>Input Range</th><th>Prediction</th></tr>
                <tr><td>value &lt; 27.5</td><td>0</td></tr>
                <tr><td>value ≥ 27.5</td><td>1</td></tr>
            </table>
        </div>
        
        <div class="card">
            <h2>🧪 Try It Now</h2>
            <p style="margin-bottom: 15px;">Enter a value and click to test the API:</p>
            <input type="number" id="inputValue" value="30" placeholder="Enter value">
            <button class="try-it" onclick="testAPI()">Make Prediction</button>
            <div id="result"></div>
        </div>
        
        <div class="card">
            <h2>💻 Code Examples</h2>
            <p><strong>PowerShell:</strong></p>
            <pre><code>Invoke-RestMethod -Uri "YOUR_API_URL" -Method POST -ContentType "application/json" -Body '{"value": 30}'</code></pre>
            <p><strong>cURL:</strong></p>
            <pre><code>curl -X POST YOUR_API_URL -H "Content-Type: application/json" -d '{"value": 30}'</code></pre>
        </div>
        
        <div class="footer">
            <p>Built with ❤️ using AWS Lambda & scikit-learn</p>
            <p><a href="https://github.com/berserk3142-max/Serverless-Model-Deployment-on-AWS-Lambda" target="_blank">View on GitHub</a></p>
        </div>
    </div>
    
    <script>
        async function testAPI() {
            const value = document.getElementById('inputValue').value;
            const resultDiv = document.getElementById('result');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '<span style="color: #00d9ff;">Loading...</span>';
            
            try {
                const response = await fetch(window.location.href, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ value: parseFloat(value) })
                });
                const data = await response.json();
                resultDiv.innerHTML = '<span style="color: #00ff88;">✓ Response:</span><br><pre style="margin-top: 10px;"><code>' + JSON.stringify(data, null, 2) + '</code></pre>';
            } catch (error) {
                resultDiv.innerHTML = '<span style="color: #ff6b6b;">✗ Error:</span> ' + error.message;
            }
        }
    </script>
</body>
</html>
"""
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html",
            "Access-Control-Allow-Origin": "*"
        },
        "body": html
    }


def make_prediction(event):
    """Handle POST request to make a prediction."""
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
