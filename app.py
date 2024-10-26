import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV file using a relative path
data_file = './datasets/vehicles_us.csv'

try:
    df = pd.read_csv(data_file)
    st.write("Data loaded successfully!")

    # The dataframe is missing values found in the following columns:
    # - `model_year`
    # - `cylinders`
    # - `odometer`
    # - `paint_color`
    # - `is_4wd`

    # Also, we need to adjust some improperly assigned data types:
    # - `model_year`, which is of `float64`, should be `int`
    # - `cylinders`, which is of `float64`, should be `int64`
    # - `is_4wd`, which is `float64`, should be `boolean`
    # - `date_posted`, which is `string`, should be `datetime`

    # Strategy for columns with missing values:
    # - `model_year`: Rows will be dropped
    # - `cylinders`: Rows will be set to 6
    # - `odometer`: Rows will be dropped
    # - `paint_color`: These will be set to 'gray'
    # - `is_4wd`: These will be set to 0

    # Handle missing values per missing value strategy (above)
    # Drop rows with NaN in 'model_year' and 'odometer' columns
    df = df.dropna(subset=['model_year', 'odometer'])

    # Replace NaN values in columns with specified values
    df['cylinders'] = df['cylinders'].fillna(6)
    df['paint_color'] = df['paint_color'].fillna('gray')
    df['is_4wd'] = df['is_4wd'].fillna(0)

    # Convert date fields to their proper type to make data extraction more efficient/accurate
    df['model_year'] = df['model_year'].astype(int)
    df['cylinders'] = df['cylinders'].astype(int)
    df['is_4wd'] = df['is_4wd'].astype(bool)
    df['date_posted'] = pd.to_datetime(df['date_posted'])

    st.header("Sprint 4 project")
    st.subheader("Analysis of vehicle data")

    # Pie chart of car conditions
    show_pie_chart = st.checkbox("Show pie chart of conditions or bar chart of model year vs. price")

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

    # Scatterplot for price vs. odometer
    fig = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer')
    st.plotly_chart(fig)

    # Scatterplot for price vs. model year
    fig = px.scatter(df, x='model_year', y='price', title='Price vs. Model Year')
    st.plotly_chart(fig)

except FileNotFoundError as e:
    st.error(f"File {data_file} not found. Please ensure the file is in the correct directory.")
