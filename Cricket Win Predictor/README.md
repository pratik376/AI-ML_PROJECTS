# 🏏 IPL Match Prediction

**Author:** Pratik Babariya  
- GitHub: [https://github.com/pratik376](https://github.com/pratik376)  
- LinkedIn: [https://www.linkedin.com/in/babariya-pratik-083b3a20b](https://www.linkedin.com/in/babariya-pratik-083b3a20b)  
- Email: pbabari1@asu.edu 

---

## 📌 Project Overview
This project predicts the **outcome of IPL cricket matches** during the second innings using match and delivery-level data.  
It processes deliveries and match statistics, calculates features like **current run rate, required run rate, wickets remaining**, and trains a **Logistic Regression model** to predict if the batting team will win.

---

## ✨ Features
- Process IPL match (`matches.csv`) and delivery-level (`deliveries.csv`) datasets  
- Clean and preprocess data (filter teams, handle D/L matches, missing values)  
- Compute match features: `runs_left`, `balls_left`, `wickets`, `crr`, `rrr`  
- Train a **Logistic Regression** model to predict match outcome  
- Save the trained model as `pipe.pkl` for future predictions  

---

## 🛠 Requirements
- Python 3.x  
- pandas  
- numpy  
- scikit-learn  
- pickle (built-in Python module)  

> You can install all dependencies using a `requirements.txt` file.

---

## 📁 Files
- `matches.csv` → Match-level data for IPL matches  
- `deliveries.csv` → Ball-by-ball delivery data  
- `IPL_Prediction.ipynb` → Jupyter notebook with preprocessing, feature engineering, and model training  
- `pipe.pkl` → Trained Logistic Regression pipeline  
- `requirements.txt` → Python dependencies  

---

## 🚀 How to Run

### Step 1: Clone the Repository
```bash
git clone https://github.com/pratik376/AI-ML_PROJECTS.git
cd AI-ML_PROJECTS/Cricket Win Predictor
```

### Step 2: Execution

```bash
run cricket.ipynb and the use this command :- python -m streamlit run web.py
```
