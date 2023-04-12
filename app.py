import streamlit as st
from PIL import Image
import os

from pathlib import Path


cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
prof_pic = cur_dir / "assets" / "ricky.jpg"

cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()



# Description
PAGE_TITLE = "LAPTOP PRICE RECOMMENDATION"
PAGE_ICON = "✨"

DESCRIPTION = """
I am a I.T. student, currently in 4th year and enthusiastic in data science, data analysis & Machine Learning, aspire to learn new thing. 
"""


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("LAPTOP PRICE  :red[RECOMMENDATION]")
st.subheader("Welcome all,")
st.subheader("About me")

st.write(DESCRIPTION)



st.subheader("Project Name - Laptop Price Prediction")
st.subheader("Project Requirements ")
st.write(
    """
- The Things are done so far for this project......
- All the information are scraped from flipkart.com and are produced the raw data in a .csv file
- leaning and do all the preprocessing task through pandas library of python to get a clean dataframe
- Done the data preprocessing task by regex in python
- Done all the visualization task through plotly library of python
- Making the model through Random Forest Regressior, to get the desired prediction of laptop price 
- Last but not the list make the website through streamlit framework through python and deploy in 
streamlit app."
"""
)


