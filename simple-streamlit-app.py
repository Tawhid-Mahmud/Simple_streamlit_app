import streamlit as st
import pandas as pd
import plotly.express as px

# Configure the page
st.set_page_config(page_title="Simple Dashboard", layout="wide")

# Add a title and intro text
st.title("📊 Simple Dashboard")
st.markdown("Welcome to this simple dashboard. Select different options to explore the data.")

# Create two columns
col1, col2 = st.columns(2)

# First column content
with col1:
    st.subheader("📈 Sales Metrics")
    # Add a metric
    st.metric(
        label="Revenue",
        value="$12,345",
        delta="$1,234",
        delta_color="normal"
    )
    
    # Add a selectbox
    option = st.selectbox(
        'Select Product Category',
        ['Electronics', 'Clothing', 'Food', 'Books']
    )
    
    st.write('You selected:', option)

# Second column content
with col2:
    st.subheader("🎯 Performance")
    # Create sample data
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Sales': [100, 150, 130, 180, 140]
    }
    df = pd.DataFrame(data)
    
    # Create and display chart
    fig = px.bar(
        df,
        x='Month',
        y='Sales',
        title='Monthly Sales',
        text='Sales'
    )
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

# Add a slider
st.subheader("🔧 Settings")
value = st.slider('Select a value', 0, 100, 50)
st.write('Selected value:', value)

# Add a text input
user_text = st.text_input('Enter some text', 'Type here...')
st.write('You entered:', user_text)

# Add a button
if st.button('Click Me!'):
    st.balloons()
    st.write('Button clicked! 🎉')

# Add an expand