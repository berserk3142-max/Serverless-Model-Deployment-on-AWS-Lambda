# train_model.py
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Training data
X = [[20], [25], [30], [35]]
y = [0, 0, 1, 1]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Create model directory if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, "model/model.pkl")
print("Model trained and saved to model/model.pkl")
