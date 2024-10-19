import streamlit as st
st.header('Basic Calculator')

def square(num):
    return num*num

#number input
number = st.number_input("Insert a number")
st.write("The current number is ", number)


if st.button('Calculate square'):
    st.subheader(square(number))
