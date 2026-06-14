import streamlit as st
from movieRecommendationEngine import contents_based_recommender

def main():
    st.title("🎬 Movie Recommendation System")
    movie_input = st.text_input("Movie name:")
    how_many = st.slider("Number of recommendations:", 1, 20, 5)

    if st.button("Recommend"):
        if movie_input.strip():
            import io, sys
            buffer = io.StringIO()
            sys.stdout = buffer
            contents_based_recommender(movie_input, how_many)
            sys.stdout = sys.__stdout__
            st.text(buffer.getvalue())
        else:
            st.warning("Please enter a movie name.")

if __name__ == "__main__":
    main()


