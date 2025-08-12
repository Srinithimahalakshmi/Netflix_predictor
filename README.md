
# Netflix Prediction Using Random Forest Algorithm

This project leverages the Random Forest algorithm to predict user ratings for Netflix movies. By analyzing user preferences and movie attributes, the model aims to recommend movies that a user is likely to enjoy, enhancing the personalized viewing experience.

## 📂 Project Structure

```
Netflix_Prediction/
│
├── data/
│   └── netflix_data.csv       # Dataset containing user ratings and movie attributes
│
├── notebooks/
│   └── model_training.ipynb   # Jupyter notebook for data preprocessing, model training, and evaluation
│
└── app.py                     # Flask application for deploying the model as a web service
```

## 📊 Dataset Overview

The `netflix_data.csv` dataset includes the following features:

- **user_id**: Unique identifier for each user
- **movie_id**: Unique identifier for each movie
- **rating**: Rating given by the user to the movie
- **genre**: Genre of the movie
- **release_year**: Year the movie was released

## ⚙️ Random Forest Algorithm

The Random Forest algorithm is an ensemble learning method that constructs multiple decision trees during training and outputs the mode of the classes (classification) or mean prediction (regression) of the individual trees. It is widely used for classification and regression tasks due to its robustness and accuracy.

### Key Concepts:

- **Ensemble Learning**: Combining multiple models to improve performance.
- **Bootstrap Aggregating (Bagging)**: Training each decision tree on a random subset of the data.
- **Feature Randomness**: Selecting a random subset of features for each split in the decision tree.

### Advantages:

- High accuracy and robustness to overfitting.
- Handles large datasets with higher dimensionality.
- Provides feature importance, aiding in feature selection.

### Disadvantages:

- Less interpretable than individual decision trees.
- Computationally intensive, especially with large datasets.

## 🚀 Model Training

The model is trained using the following steps:

1. **Data Preprocessing**: Handling missing values, encoding categorical variables, and scaling features.
2. **Feature Selection**: Identifying the most relevant features for the model.
3. **Model Training**: Using the Random Forest algorithm to train the model on the dataset.
4. **Model Evaluation**: Assessing the model's performance using metrics like accuracy, precision, recall, and F1-score.

## 🌐 Web Application

The `app.py` file contains a Flask application that serves the trained model as a web service. Users can input their preferences through a web interface, and the model will predict the ratings for various movies.

## 📈 Results

The Random Forest model achieved an accuracy of approximately 90% on the test set, demonstrating its effectiveness in predicting user ratings.

## 📥 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Srinithimahalakshmi/Netflix_predict.git
   cd Netflix_predict
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000` to use the Netflix prediction web service.

## 📚 References

- [IBM: What is a Random Forest?](https://www.ibm.com/think/topics/random-forest)
- [GeeksforGeeks: Random Forest Algorithm in Machine Learning](https://www.geeksforgeeks.org/random-forest-algorithm-in-machine-learning/?ref=ml_lbp)
- [Built In: Random Forest: A Complete Guide for Machine Learning](https://builtin.com/data-science/random-forest-algorithm)
