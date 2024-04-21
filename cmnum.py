import streamlit as st

st.write("""
# Comparision of two numbers
""")



st.header('User Input Parameters')

n1 = st.number_input("First number :")
n2 = st.number_input("Second number :")
n3 = st.number_input("Third number :")

g =max(n1,n2,n3)

st.write("The greatest number is ",g)
