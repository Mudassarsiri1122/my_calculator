import streamlit as st
from addition import addition
from substraction import subtract
from multiplication import Multiply
from division import division


def main():
    st.title('Simple Calculator')

    menu = ['Add', 'Subtract', 'Multiply', 'Divide']
    choice = st.sidebar.selectbox('Select Operation:', menu)

    num1 = st.number_input('Enter the first number:')
    num2 = st.number_input('Enter the second number:')

    if st.button('Calculate'):
        if choice == 'Add':
            result = addition(num1, num2)
            st.write(f"{num1} + {num2} = {result}")
        elif choice == 'Subtract':
            result = subtract(num1, num2)
            st.write(f"{num1} - {num2} = {result}")
        elif choice == 'Multiply':
            result = Multiply(num1, num2)
            st.write(f"{num1} * {num2} = {result}")
        elif choice == 'Divide':
            if num2 == 0:
                st.error("Error: Division by zero!")
            else:
                result = division(num1, num2)
                st.write(f"{num1} / {num2} = {result}")
        else:
            st.error("Invalid input. Please select an operation.")

    quit_choice = st.radio("Do you want to quit?", ("Yes", "No"))

    if quit_choice == "No":
        st.write("Choose new numbers and operation or quit.")
    else:
        st.write("Thanks for using the calculator!")

if __name__ == '__main__':
    main()