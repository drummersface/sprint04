# sprint04

"""
Description of project: This project examines various aspects and trends
related to vehicle data.

The following are the methods and libraries used to implement it:
Libraries:

- Streamlit (streamlit): Used for building the interactive web application. Specifically, it is used to create the user interface, display text, and render visualizations.
- Pandas (pandas): Used for data manipulation and analysis. In this code, it reads the CSV file and manages the DataFrame for data operations (like handling missing values).
- Plotly Express (plotly.express): Used for creating the various visualizations (pie chart, bar chart, histogram, box plot, scatterplot).

This code combines Streamlit for the interface and Plotly Express for interactive charts while Pandas handles data processing.

Methods:

- st.write(): A Streamlit method to display data or text in the app. It's used to show confirmation messages, display the DataFrame, and other outputs.
- st.header(): Displays a header to label sections within the app.
- st.checkbox(): Creates a checkbox for users to interact with. In this case, it toggles between showing a pie chart or a bar chart.
- st.plotly_chart(): This method is used to display Plotly charts in the Streamlit app.
- pd.read_csv(): A Pandas method to read the CSV file and load it into a DataFrame.
- df.fillna(): A Pandas method used to handle missing values by replacing them with 0.
- df.head(): Displays the first few rows of the DataFrame.
- px.pie(): A Plotly Express method to create a pie chart. It is used to display the distribution of car conditions.
- px.bar(): A Plotly Express method to create a bar chart. It compares model years against prices, grouped by the condition of the car.
- px.histogram(): A Plotly Express method to create a histogram, visualizing car prices against mileage (odometer readings).
- px.box(): A Plotly Express method to create a box plot, showing the distribution of car prices based on mileage.
- px.scatter(): A Plotly Express method to create scatterplots, visualizing relationships between price vs odometer and price vs model_year.
- st.error(): A Streamlit method that displays an error message in case the CSV file isn't found.

To launch this project on your local machine:

"""
