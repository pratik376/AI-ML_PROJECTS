import streamlit as st
import pickle
import pandas as pd

# -------------------------------
# Load your trained pipeline
# -------------------------------
pipe = pickle.load(open('pipe.pkl', 'rb'))  # Save your trained pipe using pickle.dump(pipe, open('pipe.pkl','wb'))

# Define teams and cities (must match training data)
teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities = [
    'Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata',
    'Delhi', 'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town',
    'Port Elizabeth', 'Durban', 'Centurion', 'East London',
    'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad',
    'Cuttack', 'Nagpur', 'Dharamsala', 'Visakhapatnam', 'Pune',
    'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Mohali'
]

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Cricket Match Win Predictor", layout="centered")

st.title("🏏 Cricket Match Win Predictor")
st.write("Predict the probability of a team winning based on match situation.")

# Sidebar Inputs
st.sidebar.header("Match Information")

batting_team = st.sidebar.selectbox("Select the Batting Team", sorted(teams))
bowling_team = st.sidebar.selectbox("Select the Bowling Team", sorted(teams))
city = st.sidebar.selectbox("Select Host City", sorted(cities))

target = st.sidebar.number_input("Target Runs", min_value=20, max_value=300, step=1)
score = st.sidebar.number_input("Current Score", min_value=0, max_value=300, step=1)
wickets = st.sidebar.number_input("Wickets Out", min_value=0, max_value=10, step=1)
overs_completed = st.sidebar.number_input("Overs Completed", min_value=0.0, max_value=20.0, step=0.1)

# -------------------------------
# Prediction
# -------------------------------
if st.sidebar.button("Predict Win Probability"):

    runs_left = target - score
    balls_left = 120 - int(overs_completed * 6)
    wickets_left = 10 - wickets
    crr = score / overs_completed if overs_completed > 0 else 0
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    # Create input DataFrame
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets_left],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    # Get prediction
    result = pipe.predict_proba(input_df)
    loss_prob = result[0][0]
    win_prob = result[0][1]

    st.subheader(f"📊 Results for {batting_team} vs {bowling_team} in {city}")
    st.write(f"🎯 Target: {target} | 🏏 Score: {score}/{wickets} in {overs_completed} overs")
    st.progress(int(win_prob * 100))

    st.success(f"✅ {batting_team} Win Probability: {round(win_prob * 100, 2)}%")
    st.error(f"❌ {bowling_team} Win Probability: {round(loss_prob * 100, 2)}%")
