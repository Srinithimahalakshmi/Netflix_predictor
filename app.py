# app.py

from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load('netflix_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        release_year = int(request.form['release_year'])
        runtime = int(request.form['runtime'])
        imdb_score = float(request.form['imdb_score'])
        imdb_votes = int(request.form['imdb_votes'])

        # Prepare input for model
        input_data = pd.DataFrame([{
            'release_year': release_year,
            'runtime': runtime,
            'imdb_score': imdb_score,
            'imdb_votes': imdb_votes
        }])

        # Make prediction
        prediction = model.predict(input_data)[0]
        result = "SHOW" if prediction == 1 else "MOVIE"

        return render_template('index.html', prediction=result)

    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
