import streamlit as st
import requests
import pandas as pd
import pickle as pk
def fetch_poster(movie_id) :
    
     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cf5cba22411717ef33c051784f685f83&language=en-US'.format(movie_id))
     data = response.json()
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']



def recommend(movie):
    recommended_movies=[]
    recommended_movies_images=[]
    index=df[df['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    for i in distance[1:6]:
        recommended_movies.append(df.iloc[i[0]].title)
        id=df.iloc[i[0]].id
        recommended_movies_images.append(fetch_poster(id))
    return recommended_movies,recommended_movies_images

dfs=pk.load(open("movielist.pkl","rb"))
similarity=pk.load(open("similarity.pkl","rb"))
df=pd.DataFrame(dfs)


selected_movie=st.selectbox("select from the following",df['title'].values)
if st.button("recommend my movies!!"):

    movie_list,movie_poster=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_list[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_list[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_list[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_list[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_list[4])
        st.image(movie_poster[4])