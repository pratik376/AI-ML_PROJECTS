# Laptop Price Prediction

**Author:** Pratik Babariya  
- GitHub: [https://github.com/pratik376](https://github.com/pratik376)  
- LinkedIn: [https://www.linkedin.com/in/babariya-pratik-083b3a20b](https://www.linkedin.com/in/babariya-pratik-083b3a20b)  
- Email: pbabari1@asu.edu
---


This is a **Machine Learning project** to predict laptop prices based on features like **Company, Type, RAM, GPU, Operating System, Weight, Touchscreen, IPS, PPI, CPU, HDD, and SSD**.  
The project uses a **pre-trained pipeline model** saved as `pipe.pkl` and can be used via a **Streamlit web app** with interactive dropdowns and input hints.

## Features
- Predict laptop prices using a user-friendly web interface
- Dropdown menus for categorical features
- Input hints for easier usage
- Supports features like RAM, Storage, GPU, CPU, OS, and more

## Model Performance
- Model used: **Voting Regressor pipeline**
- Accuracy (R² score): **~89%**

## Installation & Requirements
- Python 3.x
- Streamlit
- Pandas
- Numpy
- Scikit-learn
- Matplotlib
- Seaborn (optional, for data visualization)

Install dependencies via:

```bash
pip install -r requirements.txt
```
### How to run 

## 1 : Clone the Repository

```bash
git clone https://github.com/pratik376/AI-ML_PROJECTS.git
cd AI-ML_PROJECTS/Laptop_price_predictorr
```

## 2: Run the Notebook and Python file

```bash
jupyter notebook laptop_price_predictor.ipynb
python -m streamlit run app.py
```
