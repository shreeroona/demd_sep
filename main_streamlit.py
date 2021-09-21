from flask import Flask, render_template,request
import streamlit as st

def praxis():
    st.title("Learning Streamlit")
    name = st.text_input("student_name","Type here")
    num = st.text_input("roll_no","Type here")
    result = ""
    if st.button("Show Result"):
        st.success(f"The Student name is {name} with number {num}")

if __name__ =="__main__":
    praxis()
