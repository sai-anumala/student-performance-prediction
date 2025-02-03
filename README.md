Student Performance Prediction

This project analyzes student performance based on various subjects using machine learning models: Random Forest and Logistic Regression. The frontend is built with React, and the backend is built using Flask with pre-trained machine learning models for prediction.

Table of Contents
	1.	Overview
	2.	Frontend
	3.	Backend
	4.	Setup Instructions
	5.	Usage
	6.	Technologies Used
	7.	Contributing

Overview

This application allows users to input student marks for several subjects (English, Maths, ML, AI, OS, Python) and get a prediction of whether the student will pass or fail based on machine learning models. It also displays the accuracy of the models.
	•	Frontend: React app where the user enters student data.
	•	Backend: Flask API where the predictions are made using pre-trained models.

Frontend

The frontend is a simple React app that consists of a form for users to input student data and a button to submit the data for prediction.

Features:
	•	User inputs student marks in the form fields.
	•	On submitting the form, a POST request is made to the Flask backend.
	•	Displays prediction (“Pass” or “Fail”) and model accuracies (Random Forest and Logistic Regression).
	•	Includes a loading indicator during prediction.

File: App.js
	•	Handles form data input and submission.
	•	Sends POST request to Flask API.
	•	Displays prediction result and model accuracies.

Key Dependencies:
	•	React
	•	Axios (for API calls)

Backend

The backend is built using Flask. The backend loads a CSV file with historical student performance data, trains two machine learning models (Random Forest and Logistic Regression), and serves predictions based on the input data.

Endpoints:
	1.	POST /predict:
	•	Accepts student marks (English, Maths, ML, AI, OS, Python) in JSON format and returns a prediction (“Pass” or “Fail”) along with model accuracies.
	2.	GET /evaluate:
	•	Returns the accuracy of both models.

File: app.py
	•	Loads the dataset and trains the models.
	•	Provides prediction and evaluation endpoints.

Key Libraries:
	•	Flask
	•	scikit-learn (for Random Forest and Logistic Regression models)
	•	Pandas (for data handling)
	•	Flask-CORS (for handling cross-origin requests)
	•	NumPy (for data manipulation)

Setup Instructions

Prerequisites

Ensure you have the following installed:
	•	Python 3.x
	•	Node.js
	•	npm or yarn

Backend Setup:
	1.	Clone the repository and navigate to the backend folder:

git clone https://github.com/sai-anumala/student-performance-prediction.git
cd student-performance-prediction/backend


	2.	Install dependencies:

pip install -r requirements.txt


	3.	Make sure the student_data_balanced.csv file is present in the project directory.
	4.	Start the Flask server:

python app.py



Frontend Setup:
	1.	Navigate to the frontend folder:

cd frontend


	2.	Install dependencies:

npm install


	3.	Start the React app:

npm start



Usage
	1.	Open the React app in your browser (http://localhost:3000).
	2.	Enter the student’s marks in the form fields.
	3.	Click the “Predict” button to get the prediction and model accuracies.

Technologies Used
	•	Frontend: React
	•	Backend: Flask
	•	Machine Learning: scikit-learn (Random Forest, Logistic Regression)
	•	Data Handling: Pandas, NumPy
	•	CORS Handling: Flask-CORS

