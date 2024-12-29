# House-Price-Prediction
A web-based application built with Streamlit to predict house prices in Bangalore using a pre-trained Ridge Regression model. Users can input property details such as location, total square footage, bathrooms, and BHKs to get an estimated price. Ideal for buyers and real estate professionals. 🚀
# House Price Prediction App

 ![image](https://github.com/user-attachments/assets/4300a7f4-f550-4c59-b181-d42215a134eb)


 📖 Overview
The **House Price Prediction App** is a web-based application that predicts house prices in Bangalore based on key parameters such as location, square footage, number of bathrooms, and BHKs (Bedrooms, Hall, Kitchen)
. Built using **Streamlit**, the app leverages a pre-trained **Ridge Regression model** to provide accurate and user-friendly predictions.

This project can assist buyers, real estate agents, and developers in estimating property prices efficiently.

---

✨ Features


- **User-Friendly Interface**: Easy-to-use app built with Streamlit.

- **Accurate Predictions**: Pre-trained Ridge Regression model ensures reliable results.

- **Customizable Inputs**: Supports user-defined inputs like location, square footage, number of bathrooms, and BHKs.

- **Informative Insights**: Displays additional details about the property and prediction.

---

 📂 Project Structure

house-price-prediction

app.py # Main application script

Cleaned_data.csv 

# Pre-processed data for location options 

RidgeModel.pkl 

# Pre-trained Ridge Regression model 

requirements.txt 

# Python dependencies 

README.md 

# Project documentation

---

⚙️ Installation and Setup

Follow these steps to set up and run the project on your local machine.

**1. Clone the Repository**

git clone https://github.com/Lakshaysinghal01/House-Price-Prediction.git
 
 cd house-price-prediction.

Install Dependencies

Install the required libraries listed in requirements.txt:

pip install -r requirements.txt

If requirements.txt is not present, manually install these libraries:

pip install streamlit pandas numpy scikit-learn

Run the Application

Running the Project
1.	Start the Application: Navigate to the project directory and run:
streamlit run app.py

2.	Access the Web Interface: After running the above command, Streamlit will launch a local web server, and a browser tab will open automatically. If it doesn't, open the URL displayed in your terminal, typically http://localhost:8501.


3.	Navigation:

o	Home: An introduction to the app.

o	Predict Price:

	Select a location from the dropdown (populated from Cleaned_data.csv).

	Input total square footage, number of bathrooms, and number of BHKs.

	Click "Predict" to view the predicted price in lakhs.

o	About: Learn more about the app and its purpose.
________________________________________
Key Notes

•	Model Loading: The Ridge Regression model (RidgeModel.pkl) is loaded using pickle. Ensure this file is not corrupted or missing.

•	CSV Data: The Cleaned_data.csv file provides unique location options. If you want to update the locations, modify this file accordingly.

•	Streamlit Port: By default, Streamlit runs on port 8501. Use --server.port <port_number> if you want to run it on a different port.
________________________________________
Troubleshooting
1.	Module Not Found: Ensure all libraries are installed using pip install -r requirements.txt, where requirements.txt includes:
   
streamlit

pandas

numpy

scikit-learn

3.	File Not Found:

o	Ensure Cleaned_data.csv and RidgeModel.pkl are in the same directory as app.py.

o	If your terminal path differs, navigate to the correct folder before running streamlit.

4.	Model Issues: If the model raises errors, confirm that RidgeModel.pkl matches the input features specified in app.py.

🛠 How to Use

1.	Home Page: Provides an introduction to the app and its purpose.

2.	Predict Price:

o	Select a location from the dropdown menu.

o	Input the total square footage of the property.

o	Specify the number of bathrooms and BHKs.

o	Click on the Predict button to view the predicted price.

3.	About Page: Displays details about the app and its features.
________________________________________
📊 Input Parameters

The app accepts the following inputs:

•	Location: A dropdown list of predefined locations from Cleaned_data.csv.

•	Total Sqft: Total square footage of the property (range: 300 to 10,000 sqft).

•	Bathrooms: Number of bathrooms (range: 1 to 10).

•	BHK: Number of bedrooms, halls, and kitchens (range: 1 to 10).
________________________________________
🧠 Machine Learning Model

The app uses a Ridge Regression model trained on historical house price data from Bangalore.
Why Ridge Regression?

•	Handles multicollinearity effectively.

•	Reduces overfitting by applying L2 regularization.

•	Provides better generalization for unseen data.

The model was serialized using pickle and is loaded at runtime to make predictions.
________________________________________
📋 Dependencies

The following libraries are required to run this project:

•	streamlit==1.25.0

•	pandas==2.0.3

•	numpy==1.24.4

•	scikit-learn==1.3.0

You can install these dependencies using the requirements.txt file:

pip install -r requirements.txt
________________________________________
🎯 Future Improvements

•	Expand the app to support other cities and datasets.

•	Include additional features like proximity to schools, hospitals, and markets.

•	Integrate a dynamic database for real-time updates on property prices.

•	Deploy the app to a live server (e.g., Streamlit Cloud, Heroku, or AWS).
________________________________________
🌟 Screenshots
Home Page

 ![image](https://github.com/user-attachments/assets/d5ddf176-3b6d-4cd5-a410-39eea71d20ff)

Predict Price Page

![image](https://github.com/user-attachments/assets/d9a43397-1555-4186-bb0d-a488d3936829)
 
________________________________________
🏗 Deployment

You can deploy this project to the cloud using:

•	Streamlit Cloud: Quick and free deployment for Streamlit apps.

•	Heroku: For scalable deployment.

•	AWS/Docker: For enterprise-level deployment.
________________________________________
🤝 Contributing

Contributions are welcome! If you'd like to contribute:

1.	Fork the repository.

2.	Create a new branch (git checkout -b feature-branch).

3.	Commit your changes (git commit -m "Add new feature").

4.	Push to your branch (git push origin feature-branch).

5.	Open a pull request.
________________________________________
📞 Contact

For any questions or feedback, feel free to reach out:

•	Name: Lakshay Singhal

•	Email: lakshaysinghal2909@gmail.com

•	LinkedIn: Lakshay Singhal

