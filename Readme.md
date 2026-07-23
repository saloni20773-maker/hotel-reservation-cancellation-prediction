Readme

# 🏨 Hotel Reservation Cancellation Prediction

## Project Overview

This project predicts whether a hotel reservation is likely to be cancelled using Machine Learning techniques. The objective is to help hotels improve revenue management, optimize resource allocation, and support better decision-making.

---

## Problem Statement

Hotel reservation cancellations can lead to revenue loss and inefficient resource planning. This project builds predictive models to identify bookings that are likely to be cancelled before the customer's arrival.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

## Machine Learning Models

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier (Best Model)

---

## Best Model Performance

- Accuracy: **90.54%**
- Precision: **91.46%**
- Recall: **94.67%**
- F1-Score: **93.03%**

---

## Features Used

- Lead Time
- Number of Adults
- Number of Children
- Weekend Nights
- Week Nights
- Meal Plan
- Room Type
- Market Segment
- Repeated Guest
- Previous Cancellations
- Previous Bookings
- Average Price Per Room
- Special Requests
- Arrival Date Information

---

## Project Structure

```
Hotel Reservation Cancellation Prediction/
│
├── Predicting Hotel Reservation Cancellations.ipynb
├── app.py
├── random_forest_model.pkl
├── scaler.pkl
├── label_encoders.pkl
├── Hotel Reservations.csv
├── requirements.txt
├── README.md
└── Hotel Reservation Cancellation Prediction.pptx
```

---

## Run the Streamlit App

```bash
streamlit run app.py
```

---

## Future Scope

- Deploy the application on Streamlit Cloud.
- Integrate SHAP for model interpretability.
- Develop REST APIs using FastAPI for hotel management system integration.

---

## Author

**Saloni Sharma**

Machine Learning Project - Spinnaker Analytics