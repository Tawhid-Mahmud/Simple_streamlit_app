import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page config
st.set_page_config(page_title="Streamlit Tutorial", layout="wide")

# Add a title
st.title("Welcome to Streamlit! 👋")

# Add some text
st.write("""
This is a demo app showing some basic Streamlit features.
Let's explore different types of inputs and visualizations!
""")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.header("Interactive Inputs")
    
    # Text input
    user_name = st.text_input("What's your name?", "")
    if user_name:
        st.write(f"Hello {user_name}! 👋")
    
    # Slider
    number = st.slider("Pick a number", 0, 100, 50)
    st.write(f"You picked: {number}")
    
    # Selectbox
    option = st.selectbox(
        'What is your favorite color?',
        ['Red', 'Blue', 'Green', 'Yellow']
    )
    st.write(f'Your favorite color is {option}!')

with col2:
    st.header("Data Visualization")
    
    # Generate sample data
    dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
    data = pd.DataFrame({
        'date': dates,
        'values': np.random.randn(30).cumsum()
    })
    
    # Create a line chart
    fig = px.line(data, x='date', y='values',
                  title='Random Walk Chart')
    st.plotly_chart(fig)

# Add a data table
st.header("Sample Data Table")
df = pd.DataFrame({
    'Column 1': ['A', 'B', 'C', 'D'],
    'Column 2': [1, 2, 3, 4],
    'Column 3': ['P', 'Q', 'R', 'S']
})
st.dataframe(df)

# Add a sidebar
with st.sidebar:
    st.header("Sidebar Controls")
    show_data = st.checkbox("Show raw data")
    if show_data:
        st.write("Raw data:", data)
    
    st.markdown("""
    ### About this app
    This is a simple demo showing:
    - Text inputs
    - Sliders
    - Selectboxes
    - Charts
    - Tables
    - Sidebars
    """)
