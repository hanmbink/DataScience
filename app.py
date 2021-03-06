import streamlit as st
import pandas as pd
import numpy as np
import os, urllib
from feature_tests import tests
from feature_uber import uber_pickups
from feature_plot_maps import plot_maps
from feature_car_price_prediction import prediction

DATA_URL_ROOT	= "https://raw.githubusercontent.com/hanmbink/DataScience/main/"
FILE_NAME_INST	= "instructions.md"

def main():

    # Render the readme as markdown using st.markdown.

    readme_text = st.markdown(get_file_content_as_string(FILE_NAME_INST))

    # Add a select box for the options

    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox("Choose an app",
        ["Show instructions", 
        "App1 - Test", 
        "App2 - Uber Pickups", 
        "App3 - Plotting Maps",
        "App4 - Car Price Prediction"])

    if app_mode == "Show instructions":
        st.sidebar.success('To continue select an app from drop down list')
    
    elif app_mode == "App1 - Test":
        readme_text.empty()
        tests.run_it()
    
    elif app_mode == "App2 - Uber Pickups":
        readme_text.empty()
        uber_pickups.run_it()

    elif app_mode == "App3 - Plotting Maps":
        readme_text.empty()
        plot_maps.run_it()
    
    elif app_mode == "App4 - Car Price Prediction":
        readme_text.empty()
        prediction.run_it()

# Download a single file and make its content available as a string.
@st.cache(show_spinner=False)
def get_file_content_as_string(path):
	url = DATA_URL_ROOT + path
	response = urllib.request.urlopen(url)
	return response.read().decode("utf-8")

if __name__ == "__main__":
    main()
