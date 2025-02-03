import React, { useState } from 'react';
import './App.css';

function App() {
    const [formData, setFormData] = useState({
        name: '',
        regNumber: '',
        english: '',
        maths: '',
        ml: '',
        ai: '',
        os: '',
        python: '',
    });
    const [result, setResult] = useState('');
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false); // Add loading state
    const [rfAccuracy, setRfAccuracy] = useState(null);
    const [lrAccuracy, setLrAccuracy] = useState(null);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setIsLoading(true); // Set loading to true

        try {
            const response = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    English: Number(formData.english),
                    Maths: Number(formData.maths),
                    ML: Number(formData.ml),
                    AI: Number(formData.ai),
                    OS: Number(formData.os),
                    Python: Number(formData.python),
                }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            setResult(data.Result);
            setRfAccuracy(data.RandomForestAccuracy);
            setLrAccuracy(data.LogisticRegressionAccuracy);
        } catch (err) {
            console.error("Error fetching prediction:", err);
            setError(err.message || "An error occurred during prediction.");
        } finally {
            setIsLoading(false); // Set loading back to false
        }
    };

    return (
        <div className="app-container">
            <form onSubmit={handleSubmit} className="prediction-form">
                <h1>Student Performance Analysis</h1>
                <input type="text" name="name" placeholder="Name" value={formData.name} onChange={handleChange} required />
                <input type="text" name="regNumber" placeholder="Registration Number" value={formData.regNumber} onChange={handleChange} required />
                <input type="number" name="english" placeholder="English" value={formData.english} onChange={handleChange} required />
                <input type="number" name="maths" placeholder="Maths" value={formData.maths} onChange={handleChange} required />
                <input type="number" name="ml" placeholder="ML" value={formData.ml} onChange={handleChange} required />
                <input type="number" name="ai" placeholder="AI" value={formData.ai} onChange={handleChange} required />
                <input type="number" name="os" placeholder="OS" value={formData.os} onChange={handleChange} required />
                <input type="number" name="python" placeholder="Python" value={formData.python} onChange={handleChange} required />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? "Predicting..." : "Predict"} {/* Loading indicator */}
                </button>
            </form>

            {result && <h2 className="result-message">Prediction: {result}</h2>}

            {rfAccuracy !== null && lrAccuracy !== null && (
                <div className="accuracy-info">
                    <h3>Model Accuracies:</h3>
                    <p><strong>Random Forest Accuracy:</strong> {rfAccuracy}</p>
                    <p><strong>Logistic Regression Accuracy:</strong> {lrAccuracy}</p>
                </div>
            )}

            {error && <p className="error-message">{error}</p>}
        </div>
    );
}

export default App;