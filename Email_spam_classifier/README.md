# 📧 Email Spam Classifier

**Author:** Pratik Babariya  
- GitHub: [https://github.com/pratik376](https://github.com/pratik376)  
- LinkedIn: [https://www.linkedin.com/in/babariya-pratik-083b3a20b](https://www.linkedin.com/in/babariya-pratik-083b3a20b)  
- Email: pbabari1@asu.edu
---


This project is a **Machine Learning-based Email Spam Classifier** that detects whether a given email/message is **Spam** or **Not Spam (Ham)**.  
It uses Natural Language Processing (NLP) techniques for preprocessing and multiple ML algorithms for classification.

---

## 🚀 Features
- Preprocesses email text (tokenization, stopword removal, stemming).
- Extracts features using **TF-IDF Vectorizer**.
- Trains multiple classifiers (Naive Bayes, SVM, Logistic Regression, Random Forest, etc.).
- Implements **Voting Classifier** and **Stacking Classifier** for better performance.
- Achieves high **accuracy and precision** for reliable spam detection.
- Streamlit-based **interactive UI** for testing emails in real-time.

---

## 📊 Model Performance
Using **Stacking Classifier**:
- **Accuracy**: `0.9758220502901354`  
- **Precision**: `0.9185185185185185`

---

## 🛠️ Tech Stack
- **Python 3.x**
- **Pandas, NumPy** (Data handling)
- **NLTK** (Text preprocessing)
- **Scikit-learn** (ML algorithms, evaluation)
- **Matplotlib, Seaborn** (Visualization)
- **WordCloud** (Spam/Ham visualization)
- **Streamlit** (Web UI)

---

### How To run 
## 1 : Clone the Repository
```bash
git clone https://github.com/pratik376/AI-ML_PROJECTS.git
cd AI-ML_PROJECTS/Email_spam_classifier
```

## 2: Run the Notebook and Python File

```bash
jupyter notebook email_spam.ipynb
python -m streamlit run app.py
```
