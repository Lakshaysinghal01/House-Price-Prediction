import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# Load the model
with open('RidgeModel.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the cleaned data to get the list of locations
cleaned_data = pd.read_csv('Cleaned_data.csv')

def main():
    st.markdown(
        """
        <style>
        .welcome-text {
            font-size: 48px;
            font-weight: bold;
            color: #FF5733;
            text-shadow: 3px 3px 5px #000000;
            margin-top: 20px;
            margin-bottom: 20px;
            text-align: center;
        }
        .stApp {
            background-image: url('https://assets.newamericanfunding.com/media/4590/home-prices-are-rising-in-literally-every-major-housing-market-1200-x-630.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
        }
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 30px;
        }
        .prediction-result {
            background-color: rgba(255, 87, 51, 0.1);
            padding: 20px;
            border-radius: 10px;
            font-size: 24px;
            text-align: center;
        }
        .input-box {
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .property-details {
            background-color: rgba(240, 242, 246, 0.8);
            padding: 10px;
            border-radius: 10px;
            margin-top: 10px;
        }
        .about-text {
            font-size: 20px;
            color: #333;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .about-image {
            border-radius: 10px;
            margin-top: 20px;
            width: 80%;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Predict Price", "About"])

    if page == "Home":
        st.markdown('<p class="welcome-text">Welcome to House Price Prediction</p>', unsafe_allow_html=True)
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://assets.newamericanfunding.com/media/4590/home-prices-are-rising-in-literally-every-major-housing-market-1200-x-630.jpg" width="70%" style="border-radius: 10px;">
                <p style="font-size: 20px; margin-top: 20px; color:blue;">Use this app to predict the prices of houses in Bangalore based on various parameters like location, total square feet, number of bathrooms, and BHK. Click on the 'Predict Price' tab in the sidebar to get started!</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    if page == "Predict Price":
        st.markdown('<p class="header">Predict House Price</p>', unsafe_allow_html=True)

        # User input for location, total sqft, bath, and bhk
        locations = cleaned_data['location'].unique().tolist()
        location = st.selectbox('Location', locations, index=locations.index('other'))
        total_sqft = st.number_input('Total Sqft', min_value=300.0, max_value=10000.0, value=1000.0, step=100.0, format="%.1f", key="total_sqft")
        bath = st.number_input('Bathrooms', min_value=1, max_value=10, value=2, step=1, key="bath")
        bhk = st.number_input('BHK', min_value=1, max_value=10, value=2, step=1, key="bhk")

        # Make predictions
        if st.button('Predict'):
            input_data = pd.DataFrame([[location, total_sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
            prediction = model.predict(input_data)[0]
            st.success(f'The predicted price for the property is: ₹{prediction:.2f} lakh')

            # Show additional details
            st.write("### Property Details")
            st.markdown(
                f"""
                <div class="property-details">
                <p><strong>Location:</strong> {location}</p>
                <p><strong>Total Sqft:</strong> {total_sqft} sqft</p>
                <p><strong>Bathrooms:</strong> {bath}</p>
                <p><strong>BHK:</strong> {bhk}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    if page == "About":
        st.markdown('<p class="header">About This App</p>', unsafe_allow_html=True)
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://assets.newamericanfunding.com/media/4590/home-prices-are-rising-in-literally-every-major-housing-market-1200-x-630.jpg" class="about-image">
                <p class="about-text">This app helps users predict the prices of houses in Bangalore based on various parameters like location, total square feet, number of bathrooms, and BHK. It's designed to be user-friendly and provides accurate predictions using a Ridge Regression model.</p>
                <p class="about-text">Our goal is to simplify the home buying process by offering valuable insights into property prices. Feel free to explore and use the app to make informed decisions!</p>
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == '__main__':
    main()
