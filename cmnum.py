import streamlit as st

st.write("""
# Comparision of two numbers
""")



st.header('User Input Parameters')

n1 = st.number_input("First number :")
n2 = st.number_input("Second number :")

if n1>n2:
    st.write("The greater number is :",n1)
elif n1==n2:
    st.write("The numbers are equal")
else:
   st.write("The greater number is :",n2)