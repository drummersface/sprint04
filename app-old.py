import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV file using a relative path
data_file = './datasets/vehicles_us.csv'

try:
    df = pd.read_csv(data_file)
    st.write("Data loaded successfully!")
    df = df.fillna(0)
    st.write(df.head())  # Display the first few rows of the DataFrame
    st.header("Sprint 4 project")

    show_pie_chart = st.checkbox("Show Pie Chart of Conditions")

    if show_pie_chart:
        fig = px.pie(df, names='condition', title='Conditions', color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig)
    else:
        fig = px.bar(df, x='model_year', y='price', title='Model Year vs Price', color='condition', barmode='group')
        st.plotly_chart(fig)

    fig= px.histogram(df, y='price',x='odometer', title='Prices Based Mileage', color_discrete_sequence=px.colors.qualitative.Set3)
    fig.show()
    fig= px.box(df, y='price',x='odometer', title='Prices Based Mileage', color_discrete_sequence=px.colors.qualitative.Set3)
    fig.show()
    fig= px.pie(df, names='condition',values='model_year', title='Conditions', color_discrete_sequence=px.colors.qualitative.Set3)
    fig.show()

    # Scatterplot for price vs. odometer
    fig = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer')
    fig.show()

    # Scatterplot for price vs. model year
    fig = px.scatter(df, x='model_year', y='price', title='Price vs. Model Year')
    fig.show()

except FileNotFoundError as e:
    st.error(f"File {data_file} not found. Please ensure the file is in the correct directory.")

