import streamlit as st
import pickle
import numpy as np

# Load pre-saved objects
popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

st.set_page_config(page_title="Book Recommender", layout="wide")
st.title("📚 Book Recommendation System")

# Sidebar controls
st.sidebar.header("Options")
option = st.sidebar.selectbox("Choose Option:", ["Most Popular", "Search"])

def recommend(book_name):
    if book_name not in pt.index:
        return []
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
    recommended_books = [pt.index[i[0]] for i in similar_items]
    return recommended_books

books_per_row = 5

if option == "Most Popular":
    st.subheader("🔥 Most Popular Books")
    for i in range(0, len(popular_df), books_per_row):
        cols = st.columns(books_per_row)
        for j, col in enumerate(cols):
            if i + j < len(popular_df):
                book = popular_df.iloc[i + j]
                with col:
                    st.image(book['Image-URL-M'], width=120)
                    st.caption(book['Book-Title'])
elif option == "Search":
    search_book = st.sidebar.text_input("Type a book name:")
    if search_book:
        # Find closest match (case-insensitive)
        matched_books = [book for book in pt.index if search_book.lower() in book.lower()]
        if matched_books:
            selected_book = matched_books[0]  # Take first matched book
            st.subheader(f"🔹 Recommendations for '{selected_book}'")
            recommended_books = recommend(selected_book)
            if recommended_books:
                for i in range(0, len(recommended_books), books_per_row):
                    cols = st.columns(books_per_row)
                    for j, col in enumerate(cols):
                        if i + j < len(recommended_books):
                            book_name = recommended_books[i + j]
                            book_info = books[books['Book-Title'] == book_name].iloc[0]
                            with col:
                                st.image(book_info['Image-URL-M'], width=120)
                                st.caption(book_info['Book-Title'])
            else:
                st.info("No recommendations found for this book.")
        else:
            st.warning("No book found matching your search.")
