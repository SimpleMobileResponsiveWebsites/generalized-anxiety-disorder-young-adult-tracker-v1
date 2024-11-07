import streamlit as st
import pandas as pd
import plotly.express as px

# Title and description
st.title("Generalized Anxiety Disorder (GAD) Symptom Dashboard")
st.markdown("This dashboard allows you to upload a CSV file of GAD symptoms, view symptom details, and analyze severity distribution.")

# File upload
uploaded_file = st.file_uploader("Upload your GAD symptoms CSV file", type="csv")

if uploaded_file:
    # Load data
    df = pd.read_csv(uploaded_file)

    # Validate CSV format
    required_columns = {"Symptom", "Severity", "Notes"}
    if not required_columns.issubset(df.columns):
        st.error("The uploaded CSV file must contain 'Symptom', 'Severity', and 'Notes' columns.")
    else:
        # Map severity levels for easier analysis
        severity_mapping = {"Not present": 0, "Mild": 1, "Moderate": 2, "Severe": 3, "Very severe": 4}
        df['Severity Level'] = df['Severity'].map(severity_mapping)

        # Display data table
        st.subheader("Uploaded Symptom Data")
        st.dataframe(df[['Symptom', 'Severity', 'Notes']])

        # Severity Distribution Bar Chart
        st.subheader("Severity Distribution")
        severity_counts = df['Severity'].value_counts().sort_index(key=lambda x: [severity_mapping[y] for y in x])
        fig_bar = px.bar(severity_counts, x=severity_counts.index, y=severity_counts.values,
                         labels={'x': 'Severity', 'y': 'Count'}, title="Counts by Severity Level")
        st.plotly_chart(fig_bar)

        # Pie Chart for Severity Levels
        st.subheader("Severity Levels as Percentage")
        fig_pie = px.pie(df, names='Severity', title="Severity Levels (Percentage)")
        st.plotly_chart(fig_pie)

        # Filter by Severity Level
        st.subheader("Filter Symptoms by Severity Level")
        selected_severity = st.selectbox("Select severity to filter:", options=severity_counts.index)
        filtered_df = df[df['Severity'] == selected_severity]
        st.write(f"### Symptoms with '{selected_severity}' Severity")
        st.dataframe(filtered_df[['Symptom', 'Notes']])

        # Average Severity Score
        st.subheader("Average Severity Level")
        average_severity = df['Severity Level'].mean()
        st.write(f"The average severity level across all symptoms is: {average_severity:.2f}")

        # Download processed data as CSV
        st.subheader("Download Processed Data")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", csv, "GAD_symptom_data.csv", "text/csv")

else:
    st.info("Please upload a CSV file to begin.")
