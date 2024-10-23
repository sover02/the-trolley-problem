import streamlit as st
import streamlit.components.v1 as components
st.title("DayTrip \n City-to-City Ticket Booking")

# List of cities
cities = ["Missoula", "Bozeman", "Great Falls"]

# Dropdown for 'From' city
from_city = st.selectbox("From:", cities)

# Dropdown for 'To' city
to_city = st.selectbox("To:", cities)

# Button to book tickets
if st.button("Book Tickets"):
    if from_city != to_city:
        st.success(f"Tickets booked from {from_city} to {to_city}!")
        if from_city == "Missoula" and to_city == "Bozeman":
            components.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d2825286.638113635!2d-115.1550279294301!3d46.248856423346794!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x535dcc2a50f367cb%3A0xe9e31277ca94802e!2sMissoula%2C%20Montana!3m2!1d46.8721284!2d-113.9940314!4m5!1s0x5345444c4fba8813%3A0x63f5d064f73b60aa!2sBozeman%2C%20MT!3m2!1d45.679311899999995!2d-111.03725899999999!5e0!3m2!1sen!2sus!4v1729718007070!5m2!1sen!2sus")
            st.write("Bozeman is a great city!")
        elif from_city == "Bozeman" and to_city == "Missoula":
            st.components.iframe("https://maps.app.goo.gl/nFr3nSj18DpNo3jPA")
            st.write("Missoula is a great city!") 
        elif from_city == "Bozeman" and to_city == "Great Falls":
            st.components.iframe("https://maps.app.goo.gl/PhHdMDheDLzHtSdMA")
            st.write("Great Falls is a great city!")
        elif from_city == "Great Falls" and to_city == "Bozeman":
            st.components.iframe("https://maps.app.goo.gl/fUCwt4GTXY3MnUqb7")
            st.write("Great Falls is a great city!")
    else:
        st.error("Please select different cities for 'From' and 'To'.")

st.write("Hello world")

