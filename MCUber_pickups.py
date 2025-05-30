import streamlit as st
import pandas pd
import numpy as np

st.title("Uber Pickups in NYC")
DATA_COLUMN=("data/time")


DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
	data=pd.read_csv(DATA_URL, nrows=nrows)
	lowercase=lambda x: str(x).tolower()
	data.rename(lowercase, axis="columns", inplace=True)
	data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
	return data

data_load_state=st.text("Loading Data...")
data=load_data(10000)
data_load_state.text("Loading Data...done!")



if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)

