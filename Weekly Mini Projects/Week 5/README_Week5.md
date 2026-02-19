# 📊 Employee Salary Prediction Using Machine Learning

**Student:** Muhammad Asim  
**Company:** DEVSIL (SMC-PRIVATE) LIMITED  
**Date:** February 8, 2025  

---

## 📝 Project Overview

The **Employee Salary Prediction Project** aims to predict an employee's salary using **machine learning models** based on features such as **experience, education, job role, and other employee attributes**.  

This project covers the **entire machine learning workflow**, including:  
- Data understanding and exploration  
- Data cleaning and preprocessing  
- Feature encoding and scaling  
- Training multiple machine learning models  
- Model evaluation and comparison  
- Identification of the best-performing model  
- Deriving insights and recommendations  

---

## 🎯 Project Goals

- Load and explore the **employee salary dataset** from Kaggle  
- Understand the structure and variables of the dataset  
- Preprocess the dataset for machine learning  
- Train at least **three machine learning models** to predict employee salary  
- Evaluate model performance using **R² score, MAE, MSE**  
- Compare model accuracy and select the best-performing model  
- Provide actionable insights and recommendations  

---

## 📂 Dataset

**Dataset Name:** `salary_data.csv`  

**Description:**  
Contains employee details with numerical and categorical features. The **target variable** is **Salary**, and the features include:  

| Feature | Description |
|---------|-------------|
| Age | Employee age in years |
| Experience | Years of experience |
| Education | Education level (Bachelor, Master, PhD, etc.) |
| JobRole | Employee job title |
| Skills | Optional skills or certifications |
| Salary | Target variable to predict |

---

## 🔑 Key Features

- **Numerical features:** Age, Experience  
- **Categorical features:** Education, JobRole, Skills  
- **Target variable:** Salary  

> All categorical features are automatically encoded using **LabelEncoder** before training the models.  

---

## 🛠️ Technologies & Libraries Used

- **Python** – Main programming language  
- **Pandas & NumPy** – Data manipulation and analysis  
- **Matplotlib & Seaborn** – Data visualization  
- **Scikit-learn** – Machine learning models and evaluation  

**ML Models Used:**  
- Linear Regression  
- Random Forest Regressor  
- K-Nearest Neighbors (KNN)  

**Evaluation Metrics:**  
- R² Score  
- Mean Absolute Error (MAE)  
- Mean Squared Error (MSE)  

---

## ⚙️ Project Workflow

1. **Data Loading & Exploration:**  
   - Load dataset using `pandas`  
   - Check dataset shape, info, and descriptive statistics  

2. **Data Cleaning & Preprocessing:**  
   - Handle missing values  
   - Encode categorical variables automatically using `LabelEncoder`  
   - Separate features (X) and target (y)  

3. **Train-Test Split & Scaling:**  
   - Split data into training (80%) and testing (20%)  
   - Scale features using `StandardScaler`  

4. **Model Training:**  
   - Train multiple regression models  
   - Linear Regression, Random Forest, KNN  

5. **Model Evaluation & Comparison:**  
   - Evaluate using R², MAE, and MSE  
   - Compare results to select the best-performing model  

6. **Insights & Recommendations:**  
   - Random Forest often performs best due to handling non-linear patterns  
   - Provides HR insights for salary planning and budgeting  

---

## 📊 Example Code Snippets

**Feature & Target Separation:**
```python
X = df.drop("Salary", axis=1)
y = df["Salary"]


from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

for col in df.select_dtypes(include='object').columns:
    df[col] = encoder.fit_transform(df[col])
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
