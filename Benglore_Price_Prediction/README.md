# Bangalore House Price Prediction

**Author:** Pratik Babariya  
- GitHub: [https://github.com/pratik376](https://github.com/pratik376)  
- LinkedIn: [https://www.linkedin.com/in/babariya-pratik-083b3a20b](https://www.linkedin.com/in/babariya-pratik-083b3a20b)  
- Email: pbabari1@asu.edu 

---

## Project Overview
This is a **Machine Learning project** that predicts house prices in Bangalore based on features like **Total Square Feet, BHK, Bathrooms, and Location**.  
The project uses **Linear Regression** and a pre-trained model saved as `banglore_home_prices_model.pickle`.

---

## Features
- Predict house prices in **Lakhs INR**  
- Interactive **dropdown menus** for user inputs  
- Simple and user-friendly **Streamlit web app**  

---

## Requirements
- Python 3.x  
- streamlit  
- pandas  
- numpy  
- scikit-learn  
- matplotlib (optional, for visualizations)  

> You can install all dependencies at once using `requirements.txt`.

---

## Files
- `website.py` → Streamlit web app  
- `banglore_home_prices_model.pickle` → trained model  
- `columns.pickle` → feature columns used for prediction  
- `data.csv` → original dataset (optional)  

---

## Installation & How to Run

1. **Clone this repository:**
```bash
git clone https://github.com/pratik376/AI-ML_PROJECTS.git
cd AI-ML_PROJECTS/Bangalore_House_Price_Prediction
pip install -r requirements.txt
python -m streamlit run website.py
