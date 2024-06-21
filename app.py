import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0e11f067e4dcd35425a796a789deca1e&language=en-US'.format(movie_id))
    data=response.json()
    print(data)
    return  "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie =[]
    recommended_movie_poster=[]
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie , recommended_movie_poster

movie_dic= pickle.load(open('mov.pkl','rb'))
movies= pd.DataFrame(movie_dic)
similarity= pickle.load(open('similarity.pkl','rb'))
st.title("MOVIE Recommender System ")

selected_movie_name= st.selectbox (
'I WILL RECOMMEND YOU SIMILAR MOVIES', movies['title'].values
)

if st.button('Recommend') :
    recommended_movie , recommended_movie_poster = recommend(selected_movie_name)

    col1, col2, col3,col4,col5= st.columns(5)

    with col1:
        st.header(recommended_movie[0])
        st.image(recommended_movie_poster[0])

    with col2:
        st.header(recommended_movie[1])
        st.image(recommended_movie_poster[1])

    with col3:
        st.header(recommended_movie[2])
        st.image(recommended_movie_poster[2])

    with col4:
        st.header(recommended_movie[3])
        st.image(recommended_movie_poster[3])

    with col5:
        st.header(recommended_movie[4])
        st.image(recommended_movie_poster[4])
