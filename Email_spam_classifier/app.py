import streamlit as st
import pickle
import numpy as np
import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TreebankWordTokenizer

# Load NLTK resources
nltk.download('punkt')
nltk.download('stopwords')


tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("spam_model.pkl", "rb"))

# Text preprocessing
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
tokenizer = TreebankWordTokenizer()

def transform_text(text):
    text = text.lower()
    tokens = tokenizer.tokenize(text)

    # Remove non-alphanumeric
    tokens = [i for i in tokens if i.isalnum()]
    # Remove stopwords and punctuation
    tokens = [i for i in tokens if i not in stop_words and i not in string.punctuation]
    # Stemming
    tokens = [stemmer.stem(i) for i in tokens]

    return " ".join(tokens)

# Streamlit UI
st.set_page_config(page_title="📩 Spam Message Detector", page_icon="📩", layout="centered")

st.title("📩 Spam vs Not Spam Classifier")
st.write("This app uses **Machine Learning** (TF-IDF + Classifier) to detect if a message is **Spam or Not Spam**.")


input_sms = st.text_area("✍️ Enter the message here:")

if st.button("Predict"):
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message before prediction.")
    else:
        # 1. Preprocess
        transformed_sms = transform_text(input_sms)

        # 2. Vectorize
        vector_input = tfidf.transform([transformed_sms]).toarray()

        # 3. Predict
        result = model.predict(vector_input)[0]
        prob = model.predict_proba(vector_input)[0] if hasattr(model, "predict_proba") else None

        # 4. Display
        if result == 1:
            st.error("🚨 This message is **SPAM**!")
        else:
            st.success("✅ This message is **NOT Spam**.")

        if prob is not None:
            st.write(f"🔍 Confidence: Spam = {prob[1]*100:.2f}%, Not Spam = {prob[0]*100:.2f}%")
