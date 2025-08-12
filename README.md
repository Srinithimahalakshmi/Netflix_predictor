
#  Netflix Predictor – Random Forest Rating Recommender

##  Overview
This project employs a **Random Forest** model to predict user movie ratings—empowering personalized recommendations based on historical viewing data, genres, and other user/movie features. It covers data preprocessing, feature engineering, modeling, evaluation, and deployment with a Flask web interface.

---

##  Table of Contents
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [📊 Results](#-results)  
- [🤝 Contributing](#-contributing)  
- [📬 Contact](#-contact)  

---

##  Installation
```bash
git clone https://github.com/Srinithimahalakshmi/Netflix_predictor.git
cd Netflix_predictor

python3 -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate
pip install -r requirements.txt
````

---

## Usage

### 1. Explore & Train via Notebook

```bash
jupyter notebook model.ipynb
```

### 2. Run the Web App

```bash
python app.py
```

Then navigate to **[http://127.0.0.1:5000](http://127.0.0.1:5000)** and enter your preferences to get movie rating predictions!

---

## Project Structure

```
Netflix_predictor/
├── data/
│   └── Netflix TV Shows and Movies.csv   # Dataset for training
├── notebooks/
│   └── model.ipynb                       # Data exploration and model development
├── netflix_model.joblib                  # Trained Random Forest model
├── app.py                                # Flask application for deployment
├── templates/
│   └── [HTML templates]                  # Web interface files
├── static/
│   └── [CSS/JS assets]                   # Styling and scripts
├── Netflix_predictor.png                 # Visual preview (if applicable)
├── README.md                             # Documentation (this file)
└── requirements.txt                      # Python dependencies
```

---

## Results

* **Model Accuracy**: \~90% on the test set
* Visualizations and details—like feature importance and performance metrics—are featured in the notebook and app interface.

---

## Contributing

Your contributions are welcome! You can help by:

* Expanding the dataset or refining feature engineering
* Experimenting with alternative models (e.g., XGBoost, Neural Networks)
* Improving model explainability or UI interactivity
* Enhancing recommendations using collaborative filtering or hybrid methods

To contribute:

1. Fork the project
2. Create a branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add feature XYZ"`
4. Push and submit a Pull Request

---

## Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [srinithiarumugam2003@gmail.com](mailto:srinithiarumugam2003@gmail.com)
🔗 **GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

⭐ *If you found this project helpful, a star would be greatly appreciated!*

