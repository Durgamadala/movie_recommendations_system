# 🎬 Movie Recommendation System

This is a web-based Movie Recommendation System that suggests movies similar to your selected favorite. Built with **Python**, **Streamlit**, and powered by machine learning.

---

## 🚀 Live Demo

🔗 [Try the App Now](https://durgamadala-movie-recommendations-system.streamlit.app)

---

## 🛠 Features

- Select any movie from a dropdown list
- Get 5 similar movie recommendations instantly
- Movie posters fetched dynamically from TMDB API
- Clean and interactive UI with **Streamlit**

---

## 📂 Tech Stack

- **Frontend/UI**: Streamlit
- **Backend**: Python
- **Machine Learning**: Cosine Similarity (precomputed similarity matrix)
- **APIs Used**: TMDB API (for posters)
- **Deployment**: Streamlit Cloud
- **Model Storage**: AWS S3 (for `.pkl` files)

---

## 📁 Project Structure
├── app.py # Main Streamlit app
├── import os.py # Extra helper logic
├── requirements.txt # Required libraries
├── Procfile, setup.sh # For deployment
├── README.md # Project documentation


---

## 📦 Installation (Run Locally)

1. Clone the repository:
   ```bash
   git clone https://github.com/Durgamadala/movie_recommendations_system.git
   cd movie_recommendations_system
2.install dependencies
  pip install -r requirements.txt
3.run app locally
  streamlit run app.py
🧠 How It Works
Preprocessed movie data and similarity matrix are stored on AWS S3.

User selects a movie → the app finds top 5 similar movies using cosine similarity.

Posters are fetched using the TMDB API and shown with movie titles.

🙌 Acknowledgements
Streamlit – for UI and deployment

TMDB API – for movie posters

AWS S3 – for storing model files

📧 Contact
Durga Madala
📧 durga01.madala@gmail.com
🌐 LinkedIn

yaml
Copy
Edit

---

✅ After pasting this:
- Save `README.md`
- Then run in terminal:

```bash
git add README.md
git commit -m "Complete README added"
git push




