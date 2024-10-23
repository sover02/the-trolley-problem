import streamlit as st
import streamlit.components.v1 as components
st.title("DayTrip \n City-to-City Ticket Booking")

# List of cities
cities = ["Bozeman", "Great Falls", "Missoula"]

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
            components.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d2825281.749719902!2d-115.15502791927071!3d46.24895132802401!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x5345444c4fba8813%3A0x63f5d064f73b60aa!2sBozeman%2C%20MT!3m2!1d45.679311899999995!2d-111.03725899999999!4m5!1s0x535dcc2a50f367cb%3A0xe9e31277ca94802e!2sMissoula%2C%20Montana!3m2!1d46.8721284!2d-113.9940314!5e0!3m2!1sen!2sus!4v1729721814965!5m2!1sen!2sus")
            st.write("Missoula is a great city!") 
        elif from_city == "Bozeman" and to_city == "Great Falls":
            components.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d1403936.9730217694!2d-112.71511319846933!3d46.58596424010401!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x5345444c4fba8813%3A0x63f5d064f73b60aa!2sBozeman%2C%20MT!3m2!1d45.679311899999995!2d-111.03725899999999!4m5!1s0x5342378d658cb83b%3A0xd6de56b18e5945a8!2sGreat%20Falls%2C%20MT!3m2!1d47.5052849!2d-111.3007715!5e0!3m2!1sen!2sus!4v1729722292227!5m2!1sen!2sus")
            st.write("Great Falls is a great city!")
        elif from_city == "Great Falls" and to_city == "Bozeman":
            components.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d1403223.074881477!2d-112.7330103782887!3d46.61352285527773!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x5342378d658cb83b%3A0xd6de56b18e5945a8!2sGreat%20Falls%2C%20MT!3m2!1d47.5052849!2d-111.3007715!4m5!1s0x5345444c4fba8813%3A0x63f5d064f73b60aa!2sBozeman%2C%20MT!3m2!1d45.679311899999995!2d-111.03725899999999!5e0!3m2!1sen!2sus!4v1729722586832!5m2!1sen!2sus")
            st.write("Great Falls is a great city!")
        elif from_city == "Great Falls" and to_city == "Missoula":
            components.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d693827.0903553538!2d-113.3081026644887!3d47.211454217955364!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x5342378d658cb83b%3A0xd6de56b18e5945a8!2sGreat%20Falls%2C%20MT!3m2!1d47.5052849!2d-111.3007715!4m5!1s0x535dcc2a50f367cb%3A0xe9e31277ca94802e!2sMissoula%2C%20MT!3m2!1d46.8721284!2d-113.9940314!5e0!3m2!1sen!2sus!4v1729723207607!5m2!1sen!2sus")
            st.write("Missoula is a great city!")
        elif from_city == "Missoula" and to_city == "Great Falls":
            components.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d696061.260774003!2d-113.3063774309157!3d47.04044077103771!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x535dcc2a50f367cb%3A0xe9e31277ca94802e!2sMissoula%2C%20MT!3m2!1d46.8721284!2d-113.9940314!4m5!1s0x5342378d658cb83b%3A0xd6de56b18e5945a8!2sGreat%20Falls%2C%20MT!3m2!1d47.5052849!2d-111.3007715!5e0!3m2!1sen!2sus!4v1729723287128!5m2!1sen!2sus")
            st.write("Great Falls is a great city!")
    else:
        st.error("Please select different cities for 'From' and 'To'.")

st.write("Here at DayTrip, we are dedicated to providing you with the best travel experience possible. We offer an alternative service to ensure your journey is comfortable and enjoyable. Our team is committed to providing you with the highest level of service throughout your trip. We look forward to helping you explore Montana and create unforgettable memories with others.")

