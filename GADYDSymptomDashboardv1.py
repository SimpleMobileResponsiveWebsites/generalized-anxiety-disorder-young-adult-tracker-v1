import streamlit as st
import pandas as pd
import plotly.express as px

# Load data into a DataFrame
data = {
    "Symptom": [
        "Persistent worrying or anxiety out of proportion to events", "Overthinking plans and worst-case outcomes",
        "Perceiving situations/events as threatening", "Difficulty handling uncertainty",
        "Indecisiveness and fear of making wrong decisions", "Inability to set aside or let go of a worry",
        "Inability to relax, feeling restless, on edge", "Difficulty concentrating or mind going blank",
        "Fatigue", "Trouble sleeping", "Muscle tension or aches", "Trembling, twitchiness",
        "Nervousness or being easily startled", "Sweating", "Nausea, diarrhea or irritable bowel syndrome",
        "Irritability", "Excessive worries about school/sports performance", "Excessive worries about family safety",
        "Excessive worries about punctuality", "Excessive worries about catastrophic events",
        "Feeling overly anxious to fit in", "Being a perfectionist", "Redoing tasks because they aren’t perfect",
        "Spending excessive time on homework", "Lack of confidence", "Striving for approval",
        "Requiring reassurance about performance", "Frequent stomachaches or physical complaints",
        "Avoiding school or social situations"
    ],
    "Severity": [
        "Mild", "Mild", "Moderate", "Moderate", "Moderate", "Moderate", "Moderate", "Moderate",
        "Moderate", "Moderate", "Moderate", "Moderate", "Moderate", "Moderate", "Moderate",
        "Moderate", "Mild", "Mild", "Moderate", "Moderate", "Moderate", "Moderate", "Moderate",
        "Moderate", "Moderate", "Severe", "Moderate", "Moderate", "Moderate"
    ],
    "Notes": ["test"] * 29  # Sample note for each symptom
}

df = pd.DataFrame(data)

# Map severity to numeric scale for visualization
severity_mapping = {"Not present": 0, "Mild": 1, "Moderate": 2, "Severe": 3, "Very severe": 4}
df['Severity Level'] = df['Severity'].map(severity_mapping)

# Streamlit Dashboard
st.title("GAD Symptom Severity Dashboard")
st.markdown("### Overview of Generalized Anxiety Disorder (GAD) Symptoms")

# Severity Distribution Chart
st.subheader("Severity Distribution of Symptoms")
severity_counts = df['Severity'].value_counts()
fig_severity = px.bar(severity_counts, x=severity_counts.index, y=severity_counts.values, labels={'x': 'Severity', 'y': 'Count'},
                      title="Symptom Severity Counts")
st.plotly_chart(fig_severity)

# Table with Symptom Details
st.subheader("Detailed Symptom Information")
st.dataframe(df[['Symptom', 'Severity', 'Notes']])

# Filter by Severity Level
st.subheader("Filter Symptoms by Severity Level")
selected_severity = st.selectbox("Select a severity level to filter:", options=severity_counts.index)

filtered_df = df[df['Severity'] == selected_severity]
st.write(f"### Symptoms with '{selected_severity}' Severity")
st.dataframe(filtered_df[['Symptom', 'Notes']])

# Symptom Severity Pie Chart
st.subheader("Severity Levels as a Percentage")
fig_pie = px.pie(df, names='Severity', title="Severity Distribution (Percentage)")
st.plotly_chart(fig_pie)

# Average Severity Score
st.subheader("Average Severity Level")
average_severity = df['Severity Level'].mean()
st.write(f"The average severity level across all symptoms is: {average_severity:.2f}")

# Allow download of the data as CSV
st.subheader("Download Data")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV", csv, "GAD_symptom_data.csv", "text/csv")
