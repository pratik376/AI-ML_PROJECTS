# Book Recommendation System

**Author:** Pratik Babariya  
- GitHub: [https://github.com/pratik376](https://github.com/pratik376)  
- LinkedIn: [https://www.linkedin.com/in/babariya-pratik-083b3a20b](https://www.linkedin.com/in/babariya-pratik-083b3a20b)  
- Email: pbabari1@asu.edu
---


## Project Overview
This project is a **Machine Learning based Book Recommendation System** that suggests books to users based on rating patterns.  
It uses a preprocessed dataset and implements collaborative filtering techniques to generate recommendations.  
The project also includes a **Streamlit web app** for interactive usage.

---

## Features
- Recommend books based on user preferences  
- Simple, interactive **Streamlit web interface**  
- Predictions based on **real dataset from Kaggle**  

---

## Requirements
- Python 3.x  
- streamlit  
- pandas  
- numpy  
- scikit-learn  
- matplotlib (optional, for visualizations)  
- kaggle (for downloading the dataset)

> You can install all dependencies at once using a `requirements.txt` file.

---

## Files
- `website.py` → Streamlit web app  
- `download_data.py` → Script to download the Kaggle dataset  
- `books.csv` → Dataset downloaded from Kaggle (created by running `download_data.py`)  
- `model.pickle` → Pretrained recommendation model (if applicable)  

---

## Installation & How to Run

### Step 1: Clone this repository
```bash
git clone https://github.com/pratik376/AI-ML_PROJECTS.git
cd AI-ML_PROJECTS/Book_recommended_system
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
# or
pip install streamlit pandas numpy scikit-learn matplotlib kaggle
```


### Step 3: Setup Kaggle API
```bash
To download the dataset, you need Kaggle API credentials:

Go to your Kaggle Account
 → Create New API Token → download kaggle.json.

Place kaggle.json in the correct location:

Windows: C:\Users\<username>\.kaggle\kaggle.json

Mac/Linux: ~/.kaggle/kaggle.json

This file allows the download script to access the Kaggle dataset automatically.
```

### Step 4: Download the dataset

```bash
run data_downloader.py
```


### Step 5: Run the Streamlit app

```bash
python -m streamlit run website.py
```



