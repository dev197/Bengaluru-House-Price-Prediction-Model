A machine learning project that predicts house prices in Bengaluru based on key property features such as area, location, number of bedrooms, and bathrooms.
Built with Python and deployed as a Streamlit web app on Render, this tool provides quick and reliable real estate price predictions.

📘 Introduction

The Bengaluru real estate market is complex, with prices varying widely by location and property size.
This project uses Linear Regression to analyze property data and estimate prices accurately.
Users can interact with a simple web interface to input details and get instant predictions.

🧠 Dataset

Source: Kaggle - Bengaluru House Prices Dataset

Key Features:

Location

Area (sqft)

Number of Bedrooms (BHK)

Number of Bathrooms

Price (target variable)

Data preprocessing includes cleaning, removing outliers, and encoding categorical variables.

⚙️ Tech Stack

Language: Python

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit

Model: Linear Regression

Deployment: Streamlit on Render

💻 Installation

To set up locally:

# Clone the repo
git clone - https://github.com/dev197/Bengaluru-House-Price-Prediction-Model
cd bengaluru-house-price-prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


Then open the local URL (usually http://localhost:5000) in your browser.

🚀 Usage

Open the Streamlit app.

Select the property location, BHK, bathrooms, and square footage.

Click Predict Price to get the estimated property price.

The model returns predictions in lakhs of INR.

🌐 Deployment

The app is deployed live on Render.
You can access it here once deployed:
🔗 Live Demo-- https://bengaluru-house-price-prediction-model.onrender.com

👨‍💻 Developer

Developed by Dev Gupta
