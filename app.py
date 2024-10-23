import streamlit as st

st.title("City-to-City Ticket Booking")

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
    else:
        st.error("Please select different cities for 'From' and 'To'.")

st.write("Hello world")



