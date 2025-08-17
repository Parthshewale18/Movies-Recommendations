🎬 Movie Recommendation System

This project is a content-based movie recommendation system built with Python, scikit-learn, and Streamlit. It uses TF–IDF vectorization and cosine similarity on movie overviews to suggest the top 10 most similar movies to a given title.

🚀 Features

Recommend similar movies based on plot descriptions.

Display movie posters using TMDb API.

Interactive Streamlit web app with a clean grid layout.

🛠️ Tech Stack

Python

scikit-learn (TF–IDF, cosine similarity)

pandas / numpy

Streamlit (UI)

TMDb API (for posters & movie metadata)

📦 Setup

Clone the repo:

git clone https://github.com/Parthshewale18/Movies-Recommendations.git
cd Movies-Recommendations

Install dependencies:

pip install -r requirements.txt


Get a free API key from TMDb.
Add it inside your script (e.g., fetch_poster() function).

Run the app:

streamlit run app.py

🎯 Usage

Select a movie from the dropdown.

Click Recommend.

View the top 10 recommended movies with posters in a 2×5 grid.

📸 Example:
<img width="561" height="627" alt="Capture" src="https://github.com/user-attachments/assets/121cda92-98a8-4fea-ac84-90720f8f77c8" />


⚡ Future Improvements

Hybrid recommendations (content + collaborative).

Deploy on Streamlit Cloud or Heroku.

Add search functionality.
