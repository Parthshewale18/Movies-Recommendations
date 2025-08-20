import streamlit as st
import pandas as pd
import requests
import pickle

with open('movies_data.pkl', 'rb') as file:
    movies,cosine_sim = pickle.load(file)

def get_recommendations(title,cosine_sim=cosine_sim):
    idx = movies[movies['title']==title].index[0] 
    sim_scores = list(enumerate(cosine_sim[idx])) 
    sim_scores = sorted(sim_scores,key=lambda x:x[1], reverse=True) 
    sim_scores = sim_scores[1:11]
    movies_indices = [i[0] for i in sim_scores]
    return movies[['title','movie_id']].iloc[movies_indices]

def fetch_poster(movie_id):
    api_key = "Enter your APL KEY"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None

st.title('Movie Recommender System')

selected_movie = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    recommendations = get_recommendations(selected_movie)
    st.write(f"Top 10 Recommendations for: {selected_movie}")
    cols = st.columns(5)
    for idx, row in enumerate(recommendations.iterrows()):
        i, rec = row
        poster = fetch_poster(rec['movie_id'])
        col = cols[idx % 5]
        with col:
            st.image(poster, width=100)
            st.write(f"**{rec['title']}**")
            st.write(f"ID: {rec['movie_id']}")
            st.write("")
        if (idx + 1) % 5 == 0 and idx != 9:
            cols = st.columns(5)
