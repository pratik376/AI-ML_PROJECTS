# Movie Dataset Analysis 📊🎬

**Author:** Pratik Babariya  
- GitHub: [https://github.com/pratik376](https://github.com/pratik376)  
- LinkedIn: [https://www.linkedin.com/in/babariya-pratik-083b3a20b](https://www.linkedin.com/in/babariya-pratik-083b3a20b)  
- Email: pbabari1@asu.edu  

---

## Overview
This project analyzes a movie dataset (`mymoviedb.csv`) to extract insights about movie popularity, genres, release years, and vote counts. The analysis includes basic data cleaning, feature engineering, and exploration to understand trends in the dataset.

---

## Dataset
- **File:** `mymoviedb.csv`
- **Columns used:**  
  - `Title` – Name of the movie  
  - `Genre` – Movie genre(s)  
  - `Release_Date` – Year of release  
  - `Vote_Count` – Number of votes received  
  - `Popularity` – Popularity score of the movie  

- **Columns dropped:** `Overview`, `Poster_Url`, `Original_Language`  

---

## Data Cleaning & Processing
1. Removed unnecessary columns.
2. Checked for missing values and removed rows with `NaN`.
3. Dropped duplicate entries.
4. Converted `Release_Date` to **year** format.
5. Split the `Genre` column to handle multiple genres and exploded it for analysis.
6. Converted `Genre` to categorical data type.

---

## Analysis Performed
- Count of movies per genre.
- Sum of vote counts per genre.
- Identification of the **most popular movie** based on the `Popularity` column.
- Identification of the genre of the most popular movie.
- Basic descriptive statistics of the dataset.

---

## Key Insights
- The dataset contains movies across multiple genres and years.
- The most popular movie and its corresponding genre can be easily extracted.
- Genre-based analysis can provide insights into which genres are receiving more votes or popularity.

---

## Author
**Pratik Babariya**

---

## Tools & Libraries Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 🚀 How to Run

### Step 1: Clone the Repository
```bash
git clone https://github.com/pratik376/AI-ML_PROJECTS.git
cd AI-ML_PROJECTS/Netflix
```

### Step 2: Run Notebook on your machine
```bash
run netflix_data_analysis.ipynb on your machine
```

