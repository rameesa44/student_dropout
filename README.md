# Student Dropout Prediction

A machine learning classification project that predicts whether a student is likely to drop out based on academic, demographic, socioeconomic, and enrollment-related information.

The project includes a complete machine learning workflow, from data preprocessing and exploratory data analysis to model training, evaluation, and deployment through an interactive Streamlit application.

---

## Project Overview

Student Dropout Prediction is a **binary classification** machine learning project designed to identify students who may be at risk of dropping out.

The prediction application provides:

* Dropout probability
* Risk category
* Prediction result
* Interactive student input interface

The project demonstrates an end-to-end machine learning workflow including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and web application deployment.

---

## Problem Statement

Student dropout negatively affects both students and educational institutions. Identifying students who may be at risk of dropping out at an early stage can help institutions provide appropriate academic and support interventions.

The objective of this project is to build a machine learning model that predicts whether a student will drop out based on available student information.

---

## Objective

* Predict student dropout status.
* Analyze factors associated with student dropout.
* Train a binary classification model.
* Evaluate model performance using classification metrics.
* Develop an interactive prediction application.
* Provide dropout probability and risk categorization.

---

## Dataset

The Student Dropout Prediction Dataset contains **10,000 student records** and **19 columns**.

### Dataset Breakdown

| Target Value | Meaning    | Records |
| ------------ | ---------- | ------: |
| `0`          | No Dropout |   7,646 |
| `1`          | Dropout    |   2,354 |

The dataset contains a higher number of non-dropout students, resulting in a **class imbalance** between the two target classes.

---

## Data Preprocessing

The following preprocessing steps were performed before training the machine learning model:

### Missing Values

* Numerical features were handled using **median imputation**.
* Categorical features were handled using **mode imputation**.
* No missing values remained after preprocessing.

### Categorical Encoding

* Binary categorical features were converted into binary integer values.
* Nominal categorical features were transformed using **One-Hot Encoding**.
* The encoded dataset resulted in **26 columns**.

### Feature Selection

* `Student_ID` was removed because it is a non-predictive identifier.
* A total of **24 model input features** were used for prediction.

---

## Exploratory Data Analysis

Several important patterns were identified during exploratory data analysis.

### Academic Performance

Students with lower **GPA and CGPA** showed a stronger association with dropout occurrences.

### Attendance

Students who dropped out generally had **lower attendance rates** compared with students who did not drop out.

### Stress Level

Higher **stress index scores** showed a positive relationship with dropout rates.

### Socioeconomic Factors

Family income and study hours showed relatively similar distributions between the two target classes and did not demonstrate a strong relationship with dropout compared with academic and attendance-related features.

---

## Machine Learning Model

### Algorithm

**Logistic Regression**

Logistic Regression was selected because the target variable represents a binary classification problem:

* `0` → No Dropout
* `1` → Dropout

### Train-Test Split

The dataset was divided into:

* **80% Training:** 8,000 records
* **20% Testing:** 2,000 records
* **Random State:** `42`

### Feature Scaling

`StandardScaler` was used to normalize numerical feature values.

The scaler was fitted **only on the training data** to prevent data leakage and then applied to the test data.

---

## Model Evaluation

The trained Logistic Regression model was evaluated using standard classification metrics.

| Metric        |      Score |
| ------------- | ---------: |
| **Accuracy**  | **81.35%** |
| **Precision** | **64.34%** |
| **Recall**    | **40.44%** |
| **F1-Score**  | **49.66%** |

### Metric Summary

* **Accuracy:** Measures the overall percentage of correct predictions.
* **Precision:** Measures how many students predicted as dropouts were actually dropouts.
* **Recall:** Measures how many actual dropout students were correctly identified.
* **F1-Score:** Provides a balance between precision and recall.

---

## Confusion Matrix

The model produced the following confusion matrix results:

|                       | Predicted No Dropout | Predicted Dropout |
| --------------------- | -------------------: | ----------------: |
| **Actual No Dropout** |                1,443 |               102 |
| **Actual Dropout**    |                  271 |               184 |

### Classification Results

* **True Negative (TN):** 1,443
* **False Positive (FP):** 102
* **False Negative (FN):** 271
* **True Positive (TP):** 184

The model correctly identified **184 students who actually dropped out**, while **271 actual dropout cases were predicted as non-dropouts**.

---

## Risk Categorization

The deployed application converts the predicted dropout probability into three risk categories.

| Probability   | Risk Level     |
| ------------- | -------------- |
| **Below 30%** | 🟢 Low Risk    |
| **30% – 60%** | 🟡 Medium Risk |
| **Above 60%** | 🔴 High Risk   |

This allows the prediction output to be easier to interpret than probability alone.

---

## Prediction Application

The project includes an interactive **Streamlit web application**.

Users can enter student-related information and receive a prediction containing:

* Predicted dropout status
* Dropout probability
* Risk category
* Clear visual prediction feedback

The application uses the trained Logistic Regression model and the saved preprocessing scaler to generate predictions.

---

## Project Structure

```text
student-dropout-prediction/
│
├── app.py
├── dropout_model.pkl
├── dropout_scaler.pkl
├── requirements.txt
├── Student_Dropout_Prediction.ipynb
└── README.md
```

### File Description

| File                               | Description                       |
| ---------------------------------- | --------------------------------- |
| `app.py`                           | Streamlit prediction application  |
| `dropout_model.pkl`                | Trained Logistic Regression model |
| `dropout_scaler.pkl`               | Saved StandardScaler              |
| `requirements.txt`                 | Project dependencies              |
| `Student_Dropout_Prediction.ipynb` | Complete ML workflow and analysis |
| `README.md`                        | Project documentation             |

---

## Technologies Used

### Programming & Data

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Logistic Regression
* StandardScaler

### Web Application

* Streamlit

### Deployment & Version Control

* Git
* GitHub
* Render

---

## Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Missing Value Handling
   ↓
Categorical Encoding
   ↓
Feature Selection
   ↓
Exploratory Data Analysis
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Logistic Regression
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
Streamlit Application
   ↓
Render Deployment
```

---

## Live Demo

The Student Dropout Prediction application is deployed and available online.

### Live Application

**https://student-dropout-8n5t.onrender.com**

You can use the deployed application to enter student information and receive a dropout prediction, probability score, and corresponding risk level.

---

## Key Highlights

* End-to-end machine learning classification project
* Binary classification using Logistic Regression
* Data preprocessing and categorical encoding
* Exploratory data analysis
* Feature scaling without data leakage
* Accuracy, Precision, Recall, and F1-Score evaluation
* Confusion Matrix analysis
* Dropout probability prediction
* Risk-level categorization
* Interactive Streamlit application
* Cloud deployment using Render

---

## Conclusion

The Student Dropout Prediction project demonstrates how machine learning can be used to identify students who may be at risk of dropping out based on available student information.

The Logistic Regression model achieved an **81.35% accuracy** on the test dataset. The deployed Streamlit application makes the model accessible through an interactive interface and provides both dropout probability and an easy-to-understand risk category.
