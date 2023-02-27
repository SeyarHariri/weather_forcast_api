import streamlit as st
import plotly.express as px
st.title("Weather forcast for the next days")
place = st.text_input("Place: ")
day = st.slider("Forcast Days: ", min_value=1, max_value=5,
                help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {day} days in {place}.")
def get_day(day):
    date = ["2023-02-24", "2023-02-25", "2023-03-26"]
    temperature = [10, 11, 15]
    temperature = [day * i for i in temperature]
    return date, temperature

d, t = get_day(day)


figure = px.line(x=d, y=t, labels={"x": "date", "y": "temperature (C)"} )
st.plotly_chart(figure)