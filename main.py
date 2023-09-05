import streamlit as st
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import pandas as pd
import time

st.title('Prompt-driven Analysis with Pandas AI\n')

# Input fields for user name and password
user_name = st.text_input("Enter your user name:")
password = st.text_input('Enter the password', type='password')

# Check user input for validity
if user_name.isalpha() and password == 'Praneeth@1998':
    st.write(f'Entered user_name is valid')

    # Input field for OpenAI API Key
    api_key = st.text_input("Enter your OpenAI API Key:")

    if st.button('Submit'):
        if not api_key:
            st.warning("Please enter your OpenAI API Key.")
        else:
            st.write("OpenAI API Key submitted.")

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
                st.info('Generating analysis...')
                analysis_result = pandas_ai.run(df, prompt=prompt, openai_api_key=api_key)
                st.write(analysis_result)
                st.success('Analysis completed.')
                # fig = px.bar(df)
                # st.plotly_chart(fig)
            else:
                st.warning("Please upload a file before generating analysis.")
        else:
            st.warning('Enter your prompt to execute the code')
else:
    st.error('Invalid user name or password.')
