import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather forcast for the next days")
place = st.text_input("Place: ")
day = st.slider("Forcast Days: ", min_value=1, max_value=5,
                help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {day} days in {place}.")

if place:
    filtered_data = get_data(place, day)

    if option == "Temperature":
        temprature = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temprature, labels={"x": "date", "y": "temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/clear.png"}
        sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
        print(sky_condition)
        image_path = [images[condition] for condition in sky_condition]

        st.image(image_path, width=115)