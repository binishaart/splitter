import streamlit as st

st.set_page_config(page_title="Simple Expense Splitter", page_icon="💰")

st.title("💰 Simple Expense Splitter")

# Input fields
total_bill = st.text_input("Enter total bill amount:")
num_people = st.text_input("Enter number of people:")

# Function to validate inputs
def is_valid_number(value):
    try:
        val = float(value)
        return val > 0
    except:
        return False

if st.button("Calculate"):
    if not is_valid_number(total_bill):
        st.error("❌ Total bill must be a positive number!")
    elif not num_people.isdigit() or int(num_people) <= 0:
        st.error("❌ Number of people must be a positive integer!")
    else:
        per_person = float(total_bill) / int(num_people)
        st.success(f"✅ Each person should pay: ₹{per_person:.2f}")
