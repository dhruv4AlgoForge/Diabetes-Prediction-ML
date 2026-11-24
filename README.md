# 🩺 Diabetes Prediction Using Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange" />
  <img src="https://img.shields.io/badge/Framework-Flask-black?logo=flask" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

## 📌 Project Overview

Diabetes Prediction is an end-to-end Machine Learning project that predicts the likelihood of diabetes based on medical and diagnostic measurements.

The project uses the **Pima Indians Diabetes Dataset** and implements multiple classification algorithms to compare their performance. A tuned Random Forest model is selected based on cross-validation results and integrated into a Flask web application for interactive predictions.

The objective is to demonstrate the complete machine learning workflow, from data preprocessing and exploratory data analysis to model training, evaluation, deployment, and prediction.

> **Disclaimer:** This project is developed for educational purposes only. Predictions are not medical diagnoses and should not replace professional medical advice.

## 🎯 Problem Statement

Diabetes is a chronic health condition that requires early identification and proper medical attention.

This project explores how machine learning classification algorithms can identify patterns in medical data and estimate the likelihood of diabetes based on patient attributes.

## 🎯 Project Objectives

- Perform exploratory data analysis to understand the dataset.
- Identify and handle missing or invalid values.
- Apply appropriate data preprocessing techniques.
- Train and compare multiple classification algorithms.
- Optimize model performance using GridSearchCV.
- Evaluate models using classification metrics.
- Deploy the trained model through a Flask web application.

## 📊 Dataset Information

**Dataset:** Pima Indians Diabetes Dataset

| Description | Details |
|---|---|
| Total records | 768 |
| Total columns | 9 |
| Input features | 8 |
| Target variable | Outcome |
| Problem type | Binary Classification |

**Input Features:**

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | 2-hour serum insulin |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Patient age |

**Target Variable:**
- `0` – Non-Diabetic
- `1` – Diabetic

## ⚙️ Project Workflow

1. Data collection and loading
2. Exploratory Data Analysis (EDA)
3. Data cleaning and preprocessing
4. Train-test splitting
5. Baseline model training
6. Hyperparameter tuning
7. Model evaluation and comparison
8. Saving the trained model using Joblib
9. Flask application development
10. Prediction through the web interface

## 🧹 Data Preprocessing

The following preprocessing techniques were implemented:

- Identified invalid zero values in Glucose, BloodPressure, SkinThickness, Insulin, and BMI.
- Replaced invalid zero values with missing values (NaN).
- Applied median imputation to handle missing values.
- Used an 80:20 stratified train-test split.
- Implemented preprocessing pipelines to prevent data leakage during model training and cross-validation.

## 🤖 Machine Learning Algorithms

Three classification algorithms were implemented and compared:

1. **Logistic Regression** – A classification algorithm that estimates the probability of a binary outcome.
2. **Support Vector Machine (SVM)** – Identifies an optimal decision boundary between classes.
3. **Random Forest Classifier** – Combines multiple decision trees to improve classification performance.

### Hyperparameter Tuning

GridSearchCV with 5-fold StratifiedKFold cross-validation was used to identify suitable hyperparameters for each algorithm.

### Cross-Validation Results

| Model | Best Cross-Validation F1-Score |
|---|---:|
| Logistic Regression | 0.6792 |
| SVM | 0.6902 |
| Random Forest | **0.7078** |

**Selected Model:** Tuned Random Forest Classifier.

## 📈 Model Evaluation

The tuned Random Forest model was evaluated on the unseen test dataset containing 154 records.

| Evaluation Metric | Score |
|---|---:|
| Accuracy | **73.38%** |
| Precision | 59.70% |
| Recall | 74.07% |
| F1-Score | 66.12% |
| ROC-AUC | **82.04%** |

### Confusion Matrix

| Actual / Predicted | Non-Diabetic | Diabetic |
|---|---:|---:|
| Non-Diabetic | 73 | 27 |
| Diabetic | 14 | 40 |

The model correctly classified 73 non-diabetic and 40 diabetic cases in the test dataset.

### Feature Importance

The Random Forest model identified the following important features:

| Feature | Importance |
|---|---:|
| Glucose | 0.3370 |
| BMI | 0.1818 |
| Age | 0.1262 |
| Insulin | 0.1149 |
| DiabetesPedigreeFunction | 0.0764 |
| Pregnancies | 0.0595 |
| SkinThickness | 0.0532 |
| BloodPressure | 0.0511 |

Glucose was the most influential feature in the trained Random Forest model, followed by BMI and Age.

## 🌐 Flask Web Application

The trained machine learning pipeline is integrated into a Flask-based web application.

**Application Features:**
- User-friendly interface for entering patient measurements.
- Accepts all eight input features.
- Loads the saved machine learning model.
- Generates a prediction using the trained pipeline.
- Displays the predicted class and estimated model probability.

The application provides two prediction outputs:
- Higher predicted diabetes risk
- Lower predicted diabetes risk

The probability is a model estimate, not a clinically validated measure of an individual's actual risk.

## 🏗️ Project Architecture

```text
Diabetes-Prediction-ML/
│
├── data/
│   └── diabetes.csv
│
├── models/
│   └── diabetes_prediction_model.pkl
│
├── notebooks/
│   └── diabetes_analysis.ipynb
│
├── src/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── .gitignore
```

## 🔄 Application Workflow

```text
User Input
    |
    v
Flask Web Application
    |
    v
Input Validation
    |
    v
Saved ML Pipeline
    |
    v
Data Preprocessing
    |
    v
Random Forest Model
    |
    v
Prediction + Probability
    |
    v
Result Displayed to User
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine learning and evaluation |
| Joblib | Model serialization |
| Flask | Web application and deployment |
| HTML & CSS | Frontend development |
| Jupyter Notebook | Data analysis and experimentation |
| Git & GitHub | Version control |

## 🚀 Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/dhruv4AlgoForge/Diabetes-Prediction-ML.git
```

### 2. Navigate to the Project Folder

```bash
cd Diabetes-Prediction-ML
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Flask Application

```bash
python app.py
```

### 7. Open in Browser

Visit:

```text
http://127.0.0.1:5000/
```

## 🔮 Future Improvements

- Experiment with advanced ensemble learning algorithms.
- Improve diabetic-class precision while maintaining good recall.
- Explore feature selection and additional model optimization.
- Add interactive model performance visualizations.
- Deploy the application to a cloud platform.
- Develop a more comprehensive and accessible user interface.

## 👨‍💻 Author

**Dhruv Panchal**

- GitHub: [@dhruv4AlgoForge](https://github.com/dhruv4AlgoForge)
- Project Repository: [Diabetes-Prediction-ML](https://github.com/dhruv4AlgoForge/Diabetes-Prediction-ML)

---

⭐ If you find this project interesting, consider giving the repository a star!
