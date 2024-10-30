import pandas as pd
import numpy as np
import streamlit as st
import joblib  
from xgboost import XGBRegressor
import sklearn 



# Load the trained model
model = joblib.load("Model.pkl")

# Define function to make predictions based on user input
def get_prediction(input_data):
    try:
        prediction = model.predict(input_data)
        st.text(f"The Predicted Flight Price is: ${prediction[0]:,.2f}")
    except Exception as e:
        st.text(f"Error in prediction: {str(e)}")

# Main function for the Streamlit app
def main():
    st.title("Flight Price Prediction App")
    
    # Get user inputs
    Airline = st.selectbox("Airline", ["IndiGo", "Air India","Jet Airways","SpiceJet","Multiple carriers","GoAir","Vistara","Air Asia","Multiple Airline carriers Premium"]) 
    Source = st.selectbox("Source", ["Banglore", "Kolkata","Delhi","Chennai","Mumbai"]) 
    Destination = st.selectbox("Destination", ["New Delhi", "Banglore","Cochin","Kolkata","Delhi","Hyderabad"])
    Route = st.selectbox("Route", ['DEL → BOM → COK','BLR → DEL','CCU → BOM → BLR','CCU → BLR','BOM → HYD','CCU → DEL → BLR','BLR → BOM → DEL','MAA → CCU',
'DEL → HYD → COK','DEL → BLR → COK','DEL → COK','DEL → JAI → BOM → COK','DEL → MAA → COK','DEL → AMD → BOM → COK',
'DEL → IDR → BOM → COK','DEL → HYD → MAA → COK','CCU → MAA → BLR','CCU → HYD → BLR','other'])
    Total_Stops = st.number_input("Total Stops", min_value=0, max_value=3, step=1)
    Dep_Time_Group = st.selectbox('Dep Time Group', ['Morning','Evening','Afternoon','Night'])
    Arrival_Time_Group = st.selectbox('Arrival_Time_Group', ['Morning','Evening','Afternoon','Night'])
    Duration_Minutes = st.number_input("Duration (in minutes)", min_value=30)
    Journey_Day = st.slider("Journey Day", min_value=1, max_value=31)
    Journey_Month = st.selectbox("Journey Month", ['1','2','3','4','5','6','7','8','9','10','11','12'])
    Day_of_Week = st.selectbox("Day of the Week", ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])  
    
    # Prepare input data
    input_data = pd.DataFrame({
        "Airline": [Airline],
        "Source": [Source],
        "Destination": [Destination],
        "Route": [Route],
        "Total_Stops": [Total_Stops],
        "Dep_Time_Group": [Dep_Time_Group],
        "Arrival_Time_Group": [Arrival_Time_Group],
        "Duration_Minutes": [Duration_Minutes],
        "Journey_Day": [Journey_Day],
        "Journey_Month": [Journey_Month],
        "Day_of_Week": [Day_of_Week]
    })
    
    # Button to make a prediction
    if st.button("Predict"):
        get_prediction(input_data)

# Run the app
main()
