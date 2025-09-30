# 🎬 Movie Recommendation System

**Author:** Pratik Babariya  
- GitHub: [https://github.com/pratik376](https://github.com/pratik376)  
- LinkedIn: [https://www.linkedin.com/in/babariya-pratik-083b3a20b](https://www.linkedin.com/in/babariya-pratik-083b3a20b)  
- Email: pbabari1@asu.edu

---

## 📌 Project Overview
This project is a **Movie Recommendation System** built using **Machine Learning** and the **TMDB Movie Metadata dataset** from Kaggle.  

It demonstrates:
- Data preprocessing and feature engineering  
- Building a recommendation model  
- Saving the model as `.pkl`  
- A **Streamlit web app** for interactive movie recommendations  

---

## ✨ Features
- Recommends movies based on similarity of metadata  
- Simple and interactive **Streamlit web interface**  
- Dataset downloaded directly from Kaggle with a single script  

---

## 📂 Project Structure
├── download_tmdb_datasets.py # Script to download TMDB dataset from Kaggle
├── Movie_Recommendation.ipynb # Jupyter Notebook: data prep, model training, and .pkl creation
├── web.py # Streamlit app for recommendations
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 🛠 Requirements
- Python 3.x  
- streamlit  
- pandas  
- numpy  
- scikit-learn  
- kaggle  

Install all dependencies:
```bash
pip install -r requirements.txt
```

## How to run
```bash
git clone https://github.com/pratik376/AI-ML_PROJECTS.git
cd AI-ML_PROJECTS/Movie_Recommendation_System

pip install -r requirements.txt
```

###  Setup Kaggle API
```bash
To download the dataset, you need Kaggle API credentials:

Go to your Kaggle Account
 → Create New API Token → download kaggle.json.

Place kaggle.json in the correct location:

Windows: C:\Users\<username>\.kaggle\kaggle.json

Mac/Linux: ~/.kaggle/kaggle.json

This file allows the download script to access the Kaggle dataset automatically.
```

### Download the dataset

```bash
run download_tmdb_datasets.py
run Movie_Recommendation.ipynb # this will create necessary .pkl files to run web.py
```


### Run the Streamlit app

```bash
python -m streamlit run web.py
```


