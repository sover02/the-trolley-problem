import streamlit as st
import streamlit.components.v1 as components
import re

st.title("🚌 Treasure State Transit \n City-to-City Ticket Booking")
# Removes special characters from user input
def used_input(user_name):
    return re.sub(r'[^A-Za-z0-9 ]+', '', user_name)
user_name = st.text_input("Enter your name:")
# List of cities and ticket quantities
cities = ["Bozeman", "Billings", "Missoula"]
tickets = list(range(1, 11))
# Dropdown for 'tickets'
num_tickets = st.selectbox("Number of tickets:", tickets)
# Returns a string based on the number of tickets
def ticket_string(num_tickets):
    if num_tickets == 1:
        return "1 ticket"
    else:
        return f"{num_tickets} tickets"
# Dropdown for 'From' city
from_city = st.selectbox("From:", cities)

# Dropdown for 'To' city
to_city = st.selectbox("To:", cities)

# Button to book tickets
if st.button("Book Tickets"):
    if user_name and used_input(user_name) != '':
        if from_city == "Missoula" and to_city == "Bozeman" or from_city == "Bozeman" and to_city == "Missoula":
            price = 50
        elif from_city == "Bozeman" and to_city == "Billings" or from_city == "Billings" and to_city == "Bozeman":
            price = 45
        elif from_city == "Missoula" and to_city == "Billings" or from_city == "Billings" and to_city == "Missoula":
            price = 60
        if from_city != to_city:
            st.success(f"{ticket_string(num_tickets)} has been booked from {from_city} to {to_city}! \n Your total is ${price * num_tickets}.")
            if from_city == "Missoula" and to_city == "Bozeman":
                components.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d2825286.638113635!2d-115.1550279294301!3d46.248856423346794!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x535dcc2a50f367cb%3A0xe9e31277ca94802e!2sMissoula%2C%20Montana!3m2!1d46.8721284!2d-113.9940314!4m5!1s0x5345444c4fba8813%3A0x63f5d064f73b60aa!2sBozeman%2C%20MT!3m2!1d45.679311899999995!2d-111.03725899999999!5e0!3m2!1sen!2sus!4v1729718007070!5m2!1sen!2sus")
                st.write("Bozeman is a great city! Your ride will leave at 09:30 on 11/05/2024. Enjoy your trip " + used_input(user_name) + "!")
            elif from_city == "Bozeman" and to_city == "Missoula":
                components.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d2825281.749719902!2d-115.15502791927071!3d46.24895132802401!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x5345444c4fba8813%3A0x63f5d064f73b60aa!2sBozeman%2C%20MT!3m2!1d45.679311899999995!2d-111.03725899999999!4m5!1s0x535dcc2a50f367cb%3A0xe9e31277ca94802e!2sMissoula%2C%20Montana!3m2!1d46.8721284!2d-113.9940314!5e0!3m2!1sen!2sus!4v1729721814965!5m2!1sen!2sus")
                st.write("Missoula is a great city! Your ride will leave at 14:15 on 11/12/2024. Enjoy your trip " + used_input(user_name) + "!") 
            elif from_city == "Bozeman" and to_city == "Billings":
                components.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d1426555.1130005287!2d-111.08807952749913!3d45.70621277062569!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x5345444c4fba8813%3A0x63f5d064f73b60aa!2sBozeman%2C%20MT!3m2!1d45.679311899999995!2d-111.03725899999999!4m5!1s0x53486f8888fa9d97%3A0x373556d4f179b550!2sBillings%2C%20MT!3m2!1d45.7832856!2d-108.5006904!5e0!3m2!1sen!2sus!4v1729745874567!5m2!1sen!2sus")
                st.write("Billings is a great city! Your ride will leave at 11:45 on 11/18/2024. Enjoy your trip " + used_input(user_name) + "!")
            elif from_city == "Billings" and to_city == "Bozeman":
                components.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d1426548.0695403074!2d-111.08181107177944!3d45.70648877250476!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x53486f8888fa9d97%3A0x373556d4f179b550!2sBillings%2C%20MT!3m2!1d45.7832856!2d-108.5006904!4m5!1s0x5345444c4fba8813%3A0x63f5d064f73b60aa!2sBozeman%2C%20MT!3m2!1d45.679311899999995!2d-111.03725899999999!5e0!3m2!1sen!2sus!4v1729745974376!5m2!1sen!2sus")
                st.write("Bozeman is a great city! Your ride will leave at 08:00 on 11/23/2024. Enjoy your trip! " + used_input(user_name) + "")
            elif from_city == "Billings" and to_city == "Missoula":
                components.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d2823189.2360936226!2d-113.88051327537192!3d46.28956218042968!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x53486f8888fa9d97%3A0x373556d4f179b550!2sBillings%2C%20MT!3m2!1d45.7832856!2d-108.5006904!4m5!1s0x535dcc2a50f367cb%3A0xe9e31277ca94802e!2sMissoula%2C%20MT!3m2!1d46.8721284!2d-113.9940314!5e0!3m2!1sen!2sus!4v1729746016733!5m2!1sen!2sus")
                st.write("Missoula is a great city! Your ride will leave at 10:30 on 11/27/2024. Enjoy your trip! " + used_input(user_name) + "")
            elif from_city == "Missoula" and to_city == "Billings":
                components.iframe("https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d2827460.9387272!2d-113.88679068475159!3d46.206628993663166!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e0!4m5!1s0x535dcc2a50f367cb%3A0xe9e31277ca94802e!2sMissoula%2C%20MT!3m2!1d46.8721284!2d-113.9940314!4m5!1s0x53486f8888fa9d97%3A0x373556d4f179b550!2sBillings%2C%20MT!3m2!1d45.7832856!2d-108.5006904!5e0!3m2!1sen!2sus!4v1729746076246!5m2!1sen!2sus")
                st.write("Billings is a great city! Your ride will leave at 13:00 on 11/30/2024. Enjoy your trip! " + used_input(user_name) + "")
        else:
            st.error("Please select different cities for 'From' and 'To'.")
    else:
        st.error("Please enter a valid name.")
st.write("Here at Treasure State Transit, we are dedicated to providing you with the best travel experience possible. We offer an alternative service to ensure your journey is comfortable and enjoyable. Our team is committed to providing you with the highest level of service throughout your trip. We look forward to helping you explore Montana and create unforgettable memories with others.")
