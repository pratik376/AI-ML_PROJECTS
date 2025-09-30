# 🔍 Duplicate Question Pair Detection (Quora Dataset)

**Author:** Pratik Babariya  
- GitHub: [https://github.com/pratik376](https://github.com/pratik376)  
- LinkedIn: [https://www.linkedin.com/in/babariya-pratik-083b3a20b](https://www.linkedin.com/in/babariya-pratik-083b3a20b)  
- Email: pbabari1@asu.edu
---


This project is an **NLP + Machine Learning exercise** that aims to detect whether two given questions are duplicates of each other.  
It is inspired by the **Quora Duplicate Questions dataset**.  

---

## 📊 Project Overview
- Preprocessed and cleaned the dataset (removed missing values, sampled subset).  
- Engineered features such as:
  - Question length (`q1_len`, `q2_len`)  
  - Number of words (`q1_num_words`, `q2_num_words`)  
  - Common words count (`word_comman`)  
  - Total words (`word_total`)  
  - Word share ratio (`word_share`)  
- Applied **Bag of Words (CountVectorizer)** for text representation.  
- Built a **Random Forest Classifier** to predict whether a question pair is duplicate or not.  

---

## ⚙️ Installation

Clone this repository and run on your machine:

```bash
git clone https://github.com/pratik376/AI-ML_PROJECTS.git
cd AI-ML_PROJECTS/NLP_Duplicated_text_pairs
```

## How to run

```bash
jupyter notebook quora_duplicate_text.ipynb
```