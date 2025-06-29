#for calculate prepare
import streamlit as st

st.title("Corvit Grading System")

st.number_input('Enter ObtainMarks: , min value = 0')

total = st.number_imput('Enter Total Marks')

p = marks / total * 100

st.subheader(f'Your Percentage :blue[{p} %] %')

if p >= 80:
    st.success('Your Percentage is 80 %')


