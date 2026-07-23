import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Saved Files
# -----------------------------
model = joblib.load("random_forest_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")

st.set_page_config(page_title="Hotel Reservation Cancellation Prediction")

st.title("🏨 Hotel Reservation Cancellation Prediction")
st.write("Enter the booking details below.")

# -----------------------------
# User Inputs
# -----------------------------

no_of_adults = st.number_input("Number of Adults", min_value=0, value=2)

no_of_children = st.number_input("Number of Children", min_value=0, value=0)

no_of_weekend_nights = st.number_input("Weekend Nights", min_value=0, value=1)

no_of_week_nights = st.number_input("Week Nights", min_value=0, value=2)

meal = st.selectbox(
    "Meal Plan",
    ["Meal Plan 1","Meal Plan 2","Meal Plan 3","Not Selected"]
)

required_car_parking_space = st.selectbox(
    "Car Parking Required",
    [0,1]
)

room = st.selectbox(
    "Room Type",
    [
        "Room_Type 1",
        "Room_Type 2",
        "Room_Type 3",
        "Room_Type 4",
        "Room_Type 5",
        "Room_Type 6",
        "Room_Type 7"
    ]
)

lead_time = st.number_input("Lead Time", min_value=0, value=80)

arrival_year = st.selectbox(
    "Arrival Year",
    [2017,2018]
)

arrival_month = st.slider(
    "Arrival Month",
    1,
    12,
    7
)

arrival_date = st.slider(
    "Arrival Date",
    1,
    31,
    15
)

market = st.selectbox(
    "Market Segment",
    [
        "Offline",
        "Online",
        "Corporate",
        "Aviation",
        "Complementary"
    ]
)

repeated_guest = st.selectbox(
    "Repeated Guest",
    [0,1]
)

no_of_previous_cancellations = st.number_input(
    "Previous Cancellations",
    min_value=0,
    value=0
)

no_of_previous_bookings_not_canceled = st.number_input(
    "Previous Successful Bookings",
    min_value=0,
    value=0
)

avg_price_per_room = st.number_input(
    "Average Room Price",
    min_value=0.0,
    value=100.0
)

no_of_special_requests = st.number_input(
    "Special Requests",
    min_value=0,
    value=0
)

# -----------------------------
# Encode Categorical Columns
# -----------------------------

meal_map = {
    "Meal Plan 1": 0,
    "Not Selected": 1,
    "Meal Plan 2": 2,
    "Meal Plan 3": 3
}

room_map = {
    "Room_Type 1": 0,
    "Room_Type 4": 1,
    "Room_Type 2": 2,
    "Room_Type 6": 3,
    "Room_Type 5": 4,
    "Room_Type 7": 5,
    "Room_Type 3": 6
}

market_map = {
    "Offline": 0,
    "Online": 1,
    "Corporate": 2,
    "Aviation": 3,
    "Complementary": 4
}

meal = meal_map[meal]
room = room_map[room]
market = market_map[market]

# -----------------------------
# Create DataFrame
# -----------------------------

data = pd.DataFrame([[
    no_of_adults,
    no_of_children,
    no_of_weekend_nights,
    no_of_week_nights,
    meal,
    required_car_parking_space,
    room,
    lead_time,
    arrival_year,
    arrival_month,
    arrival_date,
    market,
    repeated_guest,
    no_of_previous_cancellations,
    no_of_previous_bookings_not_canceled,
    avg_price_per_room,
    no_of_special_requests
]], columns=[
    'no_of_adults',
    'no_of_children',
    'no_of_weekend_nights',
    'no_of_week_nights',
    'type_of_meal_plan',
    'required_car_parking_space',
    'room_type_reserved',
    'lead_time',
    'arrival_year',
    'arrival_month',
    'arrival_date',
    'market_segment_type',
    'repeated_guest',
    'no_of_previous_cancellations',
    'no_of_previous_bookings_not_canceled',
    'avg_price_per_room',
    'no_of_special_requests'
])

# -----------------------------
# Scale Data
# -----------------------------

scaled = scaler.transform(data)

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict"):

    prediction = model.predict(scaled)[0]

    if prediction == 1:
        st.error("❌ Booking will be Cancelled")
    else:
        st.success("✅ Booking will NOT be Cancelled")