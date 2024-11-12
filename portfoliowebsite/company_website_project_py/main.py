import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.subheader(":blue[Join Our Startup]")
    st.title("Creating an inovation in the :green[medical] space")
    paragraph = """
    Join our team and help us bring this project to life.
    """
    st.write(paragraph)
    st.text_input(placeholder="Your Email: ", label="")
    st.button(label="Upload CV & Send")

with col2:
    st.image("images/mainphoto.jpg")

st.title("Our Team: ")

col3, col4, col5 = st.columns(3)

df = pandas.read_csv("data.csv", sep=",")
with col3:
    for index, row in df[:4].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])
        
with col4:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col5:
    for index, row in df[8:].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])