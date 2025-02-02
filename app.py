import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    respnse = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=fd28c4cfa16feadf432f45d1af64b9f9&language=en-US'.format(movie_id))
    data = respnse.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommended_movies_posters = []
    recommended_movies = []
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)  # Use i[0] to access the correct movie
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


movies = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation')

selected_movie_name = st.selectbox(
    'Search Movies By Name',
    movies['title'].values
)

#if st.button('Recommend'):
 #   names,posters = recommend(selected_movie_name)

  #  col1, col2, col3, col4, col5 = st.columns(5)
   # with col1:
    #    st.header(names[0])
     #   st.image(posters[0])
    #with col2:
     #   st.header(names[1])
      #  st.image(posters[1])
    #with col3:
     #   st.header(names[2])
      #  st.image(posters[2])
    #with col4:
     #   st.header(names[3])
      #  st.image(posters[3])
    #with col5:
     #   st.header(names[4])
      #  st.image(posters[4])
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f"<h4 style='text-align: center; font-size:16px;'>{names[0]}</h4>", unsafe_allow_html=True)
        st.image(posters[0])
    with col2:
        st.markdown(f"<h4 style='text-align: center; font-size:16px;'>{names[1]}</h4>", unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        st.markdown(f"<h4 style='text-align: center; font-size:16px;'>{names[2]}</h4>", unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        st.markdown(f"<h4 style='text-align: center; font-size:16px;'>{names[3]}</h4>", unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        st.markdown(f"<h4 style='text-align: center; font-size:16px;'>{names[4]}</h4>", unsafe_allow_html=True)
        st.image(posters[4])



