from flask import Flask, request, jsonify # type: ignore 
import numpy as np # type: ignore
import pandas as pd # type: ignore 
from sklearn.model_selection import train_test_split # type: ignore 
from sklearn.ensemble import RandomForestClassifier # type: ignore
from sklearn.linear_model import LogisticRegression # type: ignore 
from flask_cors import CORS # type: ignore
from sklearn.metrics import classification_report, accuracy_score # type: ignore

app = Flask(__name__)
CORS(app)

# Load and preprocess data 
try:
    data = pd.read_csv("student_data_balanced.csv")
    numeric_cols = data.columns.drop('Student Name')
    data[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors='coerce')  # Handle non-numeric values gracefully

    # Check for missing values (optional, consider imputation if necessary)
    if data.isnull().sum().any():
        print("Warning: Missing values found in the dataset. Consider imputation techniques.")

except FileNotFoundError:
    print(f"Error: CSV file 'student_marks.csv' not found.")
    exit()
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# Split data into features (X) and target variable (y)
X = data[['English', 'Maths', 'ML', 'AI', 'OS', 'Python']]
y = data['Result']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train models (Random Forest and Logistic Regression)
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)

# Evaluate models on the test set
rf_predictions = rf_model.predict(X_test)
lr_predictions = lr_model.predict(X_test)

# Calculate accuracy for both models
rf_accuracy = accuracy_score(y_test, rf_predictions)
lr_accuracy = accuracy_score(y_test, lr_predictions)

# Generate classification reports for both models
rf_report = classification_report(y_test, rf_predictions, output_dict=True)
lr_report = classification_report(y_test, lr_predictions, output_dict=True)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        required_keys = ['English', 'Maths', 'ML', 'AI', 'OS', 'Python']
        if not all(key in data for key in required_keys):
            return jsonify({"error": f"Missing required keys: {required_keys}"}), 400

        # Convert JSON data to a NumPy array (reshape for prediction)
        subjects = np.array([data[key] for key in required_keys]).reshape(1, -1)

        # Make predictions using both models
        rf_prediction = rf_model.predict(subjects)[0]
        lr_prediction = lr_model.predict(subjects)[0]

        # Debug print statements for predictions
        print(f"Random Forest Prediction: {rf_prediction}")
        print(f"Logistic Regression Prediction: {lr_prediction}")

        # Use Random Forest prediction for simplicity (simplified logic)
        final_prediction = rf_prediction  # Directly use Random Forest prediction

        return jsonify({
            "Result": "Pass" if final_prediction == 1 else "Fail",
            "RandomForestAccuracy": rf_accuracy,
            "LogisticRegressionAccuracy": lr_accuracy,
            
        })

    except (ValueError, TypeError) as e:
        return jsonify({"error": f"Invalid input data: {e}"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500


@app.route('/evaluate', methods=['GET'])
def evaluate():
    return jsonify({
        "RandomForestAccuracy": rf_accuracy,
        "LogisticRegressionAccuracy": lr_accuracy,

    })

if __name__ == '__main__':
    app.run(debug=True)