import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline 

st.title("Student Performance Indicator")

gender = st.selectbox("Gender", options=['male', 'female'])

col1, col2 = st.columns(2)
with col1: 
    race_ethnicity = st.selectbox("Race/Ethnicity", options=['group A', 'group B', 'group C', 'group D', 'group E', ])
    test_preparation_course = st.selectbox("Test preparation course", options=["none", "completed"])
    reading_score = st.slider(label="Reading Score", min_value=0, max_value=100)

with col2:
    parental_level_of_education = st.selectbox("Parental level of Education", options=["associate's degree", "bachelor's degree", "high school", "master's degree", "some college", "some high school"])
    lunch = st.selectbox("Lunch Type", options=["free/reduced", "standard"])
    writing_score = st.slider(label="Writing Score", min_value=0, max_value=100)

predict_button = st.button("Predict")

st.session_state['result'] = ""

if predict_button:
    data = CustomData(gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score)
    pred_df = data.get_data_as_df()

    predict_pipeline = PredictPipeline()
    result = predict_pipeline.predict(pred_df)
    st.session_state['result'] = f"Result: {round(result[0], 2)}"
    st.write(st.session_state['result'])
