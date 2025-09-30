import streamlit as st
import pickle
import pandas as pd
import requests

st.title("Movie Recommender System")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=3fedf9a2a00c3c49652931ed297f233e&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):

      movie_index= movies[movies['title']==movie].index[0]
      movie_list=sorted(list(enumerate(similarity[movie_index])),reverse=True,key= lambda x:x[1])[1:6]

      recommend_movies=[]
      recommend_movies_poster=[]
      for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))

      return recommend_movies , recommend_movies_poster 



similarity=pickle.load(open('similarity.pkl','rb'))



movies_list=pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movies_list)

st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬")
selected_movie_name = st.selectbox(
    "What movie is on your mind",
    movies['title'].values
)

if st.button("Recommend"):
    recommended_movie_names,recommended_movie_posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
 