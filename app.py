import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV file using a relative path
data_file = './datasets/vehicles_us.csv'

try:
    df = pd.read_csv(data_file)
    st.write("Data loaded successfully!")
    
    # Handle missing values
    df = df.fillna(0)
    df['paint_color'] = df['paint_color'].astype(str)
    st.write(df.head())  # Display the first few rows of the DataFrame
    st.header("Sprint 4 project")
    
    # Pie chart of car conditions
    show_pie_chart = st.checkbox("Show Pie Chart of Conditions")
    
    if show_pie_chart:
        fig = px.pie(df, names='condition', title='Conditions', color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig)
    else:
        # Bar chart of model year vs price grouped by condition
        fig = px.bar(df, x='model_year', y='price', title='Model Year vs Price', color='condition', barmode='group')
        st.plotly_chart(fig)
    
    # Histogram for price vs odometer
    fig = px.histogram(df, y='price', x='odometer', title='Price Based on Mileage', color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig)  # Correct method to display in Streamlit
    
    # Box plot for price vs odometer
    fig = px.box(df, y='price', x='odometer', title='Price Distribution Based on Mileage', color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig)
    
    # Scatterplot for price vs. odometer
    fig = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer')
    st.plotly_chart(fig)

    # Scatterplot for price vs. model year
    fig = px.scatter(df, x='model_year', y='price', title='Price vs. Model Year')
    st.plotly_chart(fig)

except FileNotFoundError as e:
    st.error(f"File {data_file} not found. Please ensure the file is in the correct directory.")

