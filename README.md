# Customer Lifetime Value (CLV) Prediction using Machine Learning

A complete end-to-end **Predictive Analytics** project that estimates the **Future Customer Lifetime Value (Future_CLV)** of e-commerce customers using Machine Learning.

The project demonstrates the entire data science workflow, from data cleaning and exploratory data analysis to feature engineering, model development, evaluation, and deployment using **Streamlit**.

---

## 🚀 Live Demo

🌐 **Streamlit App:**  
https://predictive-analytics-mini-project.streamlit.app/

📂 **GitHub Repository:**  
https://github.com/AswinSanthoshDev/Predictive-Analytics-Mini-Project

---

## 📌 Project Overview

Customer Lifetime Value (CLV) is an important business metric that estimates the total value a customer is expected to generate over time.

This project predicts **Future Customer Lifetime Value** using customer demographic, behavioral, transactional, and engagement data. Several regression models were evaluated, and **XGBoost Regressor** achieved the best performance.

---

## 🎯 Objectives

- Perform Exploratory Data Analysis (EDA)
- Clean and preprocess real-world style data
- Handle missing values, duplicates, and inconsistent values
- Create meaningful engineered features
- Build multiple regression models
- Compare model performance
- Deploy the best model using Streamlit

---

## 📊 Dataset

The dataset contains **25,000 customer records** after preprocessing.

### Features Included

- Customer Demographics
- Purchase History
- Customer Engagement
- Membership Information
- Website Activity
- App Activity
- Customer Support Metrics
- Payment Information

### Target Variable

- **Future_CLV**

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

- Handled missing values
- Removed duplicate records
- Corrected inconsistent categorical values
- Standardized text formatting
- Converted appropriate data types
- Applied One-Hot Encoding for categorical variables

---

## ⚙️ Feature Engineering

Three new features were created:

| Feature | Description |
|----------|-------------|
| Purchase Intensity | Total Orders ÷ Customer Tenure |
| Engagement Score | Website Visits + App Sessions |
| Spend Per Day | Total Spend ÷ Customer Tenure |

These engineered features improved the predictive capability of the model.

---

## 🤖 Models Implemented

The following regression models were evaluated:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

---

## 📈 Model Performance

| Model | R² Score |
|--------|----------:|
| Linear Regression | 0.830567 |
| Ridge Regression | 0.830566 |
| Lasso Regression | 0.830928 |
| Random Forest | 0.850619 |
| Gradient Boosting | 0.853334 |
| **XGBoost** | **0.855563** |

### Best Model

🏆 **XGBoost Regressor**

Performance:

- **MAE:** **198.522807**
- **RMSE:** **454.797930**
- **R² Score:** **0.855563**

---

## 💻 Streamlit Application

The deployed web application allows users to:

- Enter customer information
- Predict Future Customer Lifetime Value
- View customer value classification
- Receive business recommendations based on predicted CLV

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- Joblib
- Streamlit
- Git
- GitHub

---

## 📂 Project Structure

```
Predictive-Analytics-Mini-Project/
│
├── data/
│   └── ecommerce_clv_dataset.csv
│
├── models/
│   ├── feature_columns.pkl
│   ├── xgboost_model.pkl
│   └── categorical_columns.pkl
│
├── notebooks/
│   └── project_analysis.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📌 Key Insights

- Customer spending is one of the strongest indicators of Future CLV.
- Purchase frequency positively influences customer lifetime value.
- Customers with longer tenure generally have higher predicted CLV.
- Highly engaged customers tend to generate greater long-term value.
- Membership level contributes significantly to customer value prediction.
- Feature engineering improved model performance.
- XGBoost produced the most accurate predictions among all evaluated models.

---

## ⚠️ Limitations

- The dataset is synthetic and may not capture all real-world behaviors.
- External business factors were not included.
- Predictions depend on the quality of input data.
- Customer behavior can change over time.
- Periodic model retraining is recommended.

---

## 🔮 Future Improvements

- Train on real-world business data.
- Deploy using Docker and cloud services.
- Add SHAP explainability for model predictions.
- Integrate with a live database.
- Automate model retraining using MLOps.

---

## 👨‍💻 Author

**Aswin Santhosh**

GitHub: https://github.com/AswinSanthoshDev

LinkedIn: https://www.linkedin.com/in/aswin-santhosh-114b87364/

---

⭐ If you found this project useful, consider giving the repository a star.