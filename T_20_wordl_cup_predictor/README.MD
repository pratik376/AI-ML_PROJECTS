# 🏏 Cricket Match Delivery Data Analysis

**Author:** Pratik Babariya  
- GitHub: [https://github.com/pratik376](https://github.com/pratik376)  
- LinkedIn: [https://www.linkedin.com/in/babariya-pratik-083b3a20b](https://www.linkedin.com/in/babariya-pratik-083b3a20b)  
- Email: pbabari1@asu.edu

---

## 📌 Project Overview
This project analyzes detailed **IPL/T20 cricket match data** at the delivery level.  
It processes raw YAML/JSON match files to generate a structured dataset with ball-by-ball information, including:

- Match ID  
- Batting and bowling teams  
- Runs scored per ball  
- Player dismissed  
- Venue and city  

The project also includes a **Streamlit web app** for interactive exploration and visualization of match statistics.

---

## ✨ Features
- Process raw match files into a clean dataset (`delivery_df`)  
- Filter matches by overs, gender, and teams  
- Explore batting and bowling statistics at the delivery level  
- Interactive **Streamlit app** for visualizations  
- Fully reproducible with Python virtual environment  

---

## 🛠 Requirements
- Python 3.x  
- pandas  
- numpy  
- streamlit  
- tqdm  
- pyyaml  


---

## 🚀 How to Run

### Step 1: Clone the Repository
```bash
git clone https://github.com/pratik376/AI-ML_PROJECTS.git
cd AI-ML_PROJECTS/T_20_wordl_cup_predictor
```

### Step 2: Install  Dependency
```bash
pip install -r requirements.txt
```

### Step 3 : Run the file
```bash
pip install notebook
jupyter nbconvert --to notebook --execute t20_predictor.ipynb
```