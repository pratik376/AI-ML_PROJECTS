# 🚗 Quikr Car Price Prediction

**Author:** Pratik Babariya  
- GitHub: [https://github.com/pratik376](https://github.com/pratik376)  
- LinkedIn: [https://www.linkedin.com/in/babariya-pratik-083b3a20b](https://www.linkedin.com/in/babariya-pratik-083b3a20b)  
- Email: pbabari1@asu.edu

---

## 📌 Project Overview
This project predicts the **selling price of used cars** from the Quikr dataset.  
It cleans and preprocesses the raw dataset, handles missing and inconsistent values, and trains a **Linear Regression model** using one-hot encoding for categorical features.  

The trained model is saved as `LinearRegressionModel.pkl` for future predictions.

---

## ✨ Features
- Clean and preprocess car dataset (`quikr_car.csv`)  
- Handle missing, non-numeric, and outlier values  
- Convert categorical features (`name`, `company`, `fuel_type`) using **One-Hot Encoding**  
- Train a **Linear Regression model** to predict car prices  
- Save the trained model as a `.pkl` file  

---

## 🛠 Requirements
- Python 3.x  
- pandas  
- numpy  
- scikit-learn  
- matplotlib (optional for visualization)  
- pickle (built-in Python library)  

> You can install all dependencies using a `requirements.txt` file.

---

## 📁 Files
- `quikr_car.csv` → Original dataset of used cars  
- `CarPricePrediction.ipynb` → Jupyter notebook with data preprocessing, model training, and evaluation  
- `LinearRegressionModel.pkl` → Trained Linear Regression model (created after running the notebook)  
- `requirements.txt` → Python dependencies  

---

## 🚀 How to Run

### Step 1: Clone the Repository
```bash
git clone https://github.com/pratik376/AI-ML_PROJECTS.git
cd AI-ML_PROJECTS/CAR_PRICE_PREDICTOR
```
### Step 2: Run the Notebook and then run Web.py
```bash
python -m streamlit run web.py
```



