import streamlit as st
import pandas as pd

# Define symptom categories and descriptions
psychological_symptoms = [
    "Persistent worrying or anxiety out of proportion to events",
    "Overthinking plans and worst-case outcomes",
    "Perceiving situations/events as threatening",
    "Difficulty handling uncertainty",
    "Indecisiveness and fear of making wrong decisions",
    "Inability to set aside or let go of a worry",
    "Inability to relax, feeling restless, on edge",
    "Difficulty concentrating or mind going blank"
]

physical_symptoms = [
    "Fatigue",
    "Trouble sleeping",
    "Muscle tension or aches",
    "Trembling, twitchiness",
    "Nervousness or being easily startled",
    "Sweating",
    "Nausea, diarrhea or irritable bowel syndrome",
    "Irritability"
]

child_teen_symptoms = [
    "Excessive worries about school/sports performance",
    "Excessive worries about family safety",
    "Excessive worries about punctuality",
    "Excessive worries about catastrophic events",
    "Feeling overly anxious to fit in",
    "Being a perfectionist",
    "Redoing tasks because they aren’t perfect",
    "Spending excessive time on homework",
    "Lack of confidence",
    "Striving for approval",
    "Requiring reassurance about performance",
    "Frequent stomachaches or physical complaints",
    "Avoiding school or social situations"
]

# Streamlit application interface
st.title("Generalized Anxiety Disorder (GAD) Symptom Tracker")

st.markdown("""
This application allows you to track various psychological and physical symptoms associated with Generalized Anxiety Disorder (GAD), including symptoms specific to children and teenagers.
Use the sliders to select the severity of each symptom, and download your inputs as a CSV file for further tracking or sharing with a healthcare provider.
""")

# Container for input data
input_data = {}

# Function to add symptoms with sliders
def add_symptom_inputs(symptom_list, category_name):
    st.header(category_name)
    for symptom in symptom_list:
        severity = st.slider(f"{symptom}", 0, 4, 0, format="%d", key=symptom)
        input_data[symptom] = severity

# Gather inputs for each symptom category
add_symptom_inputs(psychological_symptoms, "Psychological Symptoms")
add_symptom_inputs(physical_symptoms, "Physical Symptoms")
add_symptom_inputs(child_teen_symptoms, "Child/Teen Specific Symptoms")

# Map severity numeric scale to descriptions for export
severity_map = {0: "Not present", 1: "Mild", 2: "Moderate", 3: "Severe", 4: "Very severe"}
input_df = pd.DataFrame([(symptom, severity_map[severity]) for symptom, severity in input_data.items()], columns=["Symptom", "Severity"])

# Download button for CSV export
st.header("Download Symptom Data")
st.write("Click the button below to download your symptom data as a CSV file.")

csv = input_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="GAD_symptom_data.csv",
    mime="text/csv"
)

# Display the input data as a table in the app
st.header("Your Input Data")
st.dataframe(input_df)
