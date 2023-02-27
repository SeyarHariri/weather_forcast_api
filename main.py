import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather forcast for the next days")
place = st.text_input("Place: ")
day = st.slider("Forcast Days: ", min_value=1, max_value=5,
                help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {day} days in {place}.")


data = get_data(place, day, option)



figure = px.line(x=d, y=t, labels={"x": "date", "y": "temperature (C)"})

st.plotly_chart(figure)