from dotenv import load_dotenv
import os
import streamlit as st
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import plotly.express as px
import pandas as pd
import time
import matplotlib

matplotlib.use('TkAgg')

# Load environment variables from .env
load_dotenv()

API_KEY = os.environ['OPENAI_API_KEY']
llm = OpenAI(api_token=API_KEY)
pandas_ai = PandasAI(llm)

#image_url = 'C:/Users/spran/OneDrive/Desktop/artificial-brain-scaled.jpg'


image_path = 'https://mindmatters.ai/wp-content/uploads/sites/2/2021/04/artificial-brain-scaled.jpg'
st.image(image_path, use_column_width=True)

st.title('prompt driven analysis with pandas AI\n')

# Input fields for user name and password
user_name = st.text_input("Enter your user name:")
password = st.text_input('Enter the password',type == 'password')

# Check user input for validity
if user_name.isalpha() and password == 'Praneeth@1998':
    st.write(f'Entered user_name is valid')

    # File uploader
    uploaded_file = st.file_uploader("Upload a file:")

    if uploaded_file is not None:
        st.write("File uploaded:", uploaded_file.name)
        df = pd.read_csv(uploaded_file)  # Load the DataFrame

        if st.button('Submit'):
            st.write(df.head(10))  # Display a preview of the DataFrame

# Prompt and analysis
prompt = st.text_area('Enter your prompt')

if st.button('Generate'):
    if prompt:
        if 'df' in locals():
            # Simulating processing time
            analysis_result = pandas_ai.run(df, prompt=prompt)
            st.write(analysis_result)
            with st.spinner('Processing'):
                time.sleep(3)
                st.write('Code executed')
            #fig = px.bar(df)
            #st.plotly_chart(fig)
        else:
            st.warning("Please upload a file before generating analysis.")
    else:
        st.warning('Enter your prompt to execute the code')










