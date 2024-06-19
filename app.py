import streamlit as st

# Function to perform calculations
def calculate(operation, num1, num2):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        return num1 / num2
    else:
        return "Invalid operation"

# Streamlit app layout
st.title("Simple Calculator")

# Input fields
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])
num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")

# Perform calculation
if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f"The result is: {result}")
    log
