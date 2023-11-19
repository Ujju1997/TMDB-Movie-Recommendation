
import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
# print(similarity)
def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=848256ace3cdd3ffb1353ffb6ee91f8c&language=en-US".format(movie_id)).json()
    return "https://image.tmdb.org/t/p/w500/" + response['poster_path']

def recommend(movie):
    movie_index = movies[ movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    proximity_list = sorted(enumerate(distances), reverse = True, key = lambda x : x[1])[1:6]
    recommended_list = []
    poster_list = []
    for i in proximity_list:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_list.append(movies.iloc[i[0]]['title'])
        poster_list.append(fetch_poster(movie_id))
    return recommended_list, poster_list


st.title('Movie Recommender')
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    recommendations, posters = recommend(selected_movie_name)
    # for i in recommendations:
        # st.write(i)


    col1, col2, col3, col4, col5 = st.columns(5)
    column_list = [col1, col2, col3, col4, col5]
    for i in range(5):
        with column_list[i]:
            st.image(posters[i])
            st.text(recommendations[i])

        # with col2:
        #     st.image(posters[1])
        #     st.text(recommendations[1])
        #
        # with col3:
        #     st.image(posters[2])
        #     st.text(recommendations[2])
        #
        #
        # with col4:
        #     st.image(posters[3])
        #     st.text(recommendations[3])
        #
        #
        # with col5:
        #     st.image(posters[4])
        #     st.text(recommendations[4])

