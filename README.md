# 🎬 Movie-Recommendation-Engine


## 📌 Intern Details
- **Intern ID:** CITS1931  
- **Full Name:** Boddu Neha Madhuri  
- **Project Name:** Movie Recommendation Engine  
- **Duration:** 6 Weeks  

---

## 📖 Project Overview
The Movie Recommendation Engine is a machine learning-based web application that suggests similar movies based on a user’s input movie name.  

It uses **Content-Based Filtering** with **TF-IDF vectorization** on movie genres and computes similarity using **linear kernel similarity**. The system also integrates **fuzzy string matching** to handle misspelled or partial movie names.

A simple and interactive **Streamlit UI** is used to make the recommendation system user-friendly.

---

## 🎯 Project Objective
To build an intelligent recommendation system that:
- Understands movie genres
- Finds similarity between movies
- Handles user input errors (typos / partial names)
- Displays top-N recommended movies in a web interface

---

## 🧠 Machine Learning Approach
### ✔ Content-Based Filtering
- Uses movie **genres** as features
- Converts text into numerical vectors using **TF-IDF Vectorizer**
- Computes similarity using **Linear Kernel (Cosine Similarity)**

### ✔ Fuzzy Matching
- Uses `fuzzywuzzy` to match closest movie titles
- Improves user experience for incorrect inputs

---

## 📊 Dataset
- Dataset file: `movies.csv`
- Key columns used:
  - `title`
  - `genres`

---

## ⚙️ Features
- 🎯 Movie similarity recommendation
- 🔍 Handles typos using fuzzy matching
- 🎛 Adjustable number of recommendations
- 🌐 Streamlit web interface
- 📌 Clean preprocessing of movie titles and genres

---

## 🧰 Tech Stack
- Python
- Pandas & NumPy
- Scikit-learn
- Streamlit
- FuzzyWuzzy

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
