import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from ibm_cloud_sdk_core import IAMTokenManager
import requests
import json


def generate_response(api_key,question):

    mltoken =  access_token = IAMTokenManager(apikey=api_key,url="https://iam.cloud.ibm.com/identity/token").get_token()

    payload_scoring = {"question": question}
    endpoint="https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5b077740-0699-4196-8de2-a6c6923b0755/ai_service?version=2021-05-01"
    response = requests.post(
        endpoint,
        json=payload_scoring,
        headers={'Authorization': 'Bearer ' + mltoken})
    generated_output = response.json()

    return generated_output



st.title("SQL Query AI Agent")
question = st.text_area('Question',height=70)
button_clicked = st.button("Get Query")
st.subheader("Response")
if button_clicked:
    st.write(f"USER INPUT : {question}")
    try:
        with st.spinner(text="Please Wait.."):
            if type(question)== str:
                generate_response_output = generate_response(api_key="ZNaSfHuHH1REixHmnWf3eEm-Y6KD-6YGCf0TAeTHMbxW",question=question)
                with st.expander("Show Response:"):
                    st.markdown(f'<p style="color:white; font-weight:bold;">QUESTION:&nbsp;&nbsp;</p><span style="font-family:monospace; font-size:18px;color:#fa0404 ;">{generate_response_output["query"]}</span>', unsafe_allow_html=True)
                    st.markdown(f'<p style="color:white; font-weight:bold;">ANSWER:&nbsp;&nbsp;</p><span style="font-family:monospace; font-size:16px; color:#1bfa04;font-style:bold;">{generate_response_output["result"]}</span>', unsafe_allow_html=True)
                    st.markdown(f'<p style="color:white; font-weight:bold;">TOTAL EXECUTION TIME:&nbsp;&nbsp;</p><span style="font-family:monospace; font-size:16px;color:#f7db7d; font-style:italic;">{generate_response_output["execution_time"]}</span>', unsafe_allow_html=True)
  

    
    except Exception as e:
        st.error(f"Error: {e}")
        st.warning("Please check your input and try again.")
        st.stop()

         