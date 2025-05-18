import streamlit as st

st.set_page_config(page_title="My first website", page_icon="🌏", layout="centered")
st.title("Welcome to my first python website!")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.header("Home")
    st.write("This is the home page build with python and streamlit.")
    name = st.text_input("Enter your name")
    if name:
        st.success(f"Hello, {name}! Welcome to my website.")
elif page == "About":
    st.header("About")
    st.write("This is the about page. Here you can find information about me and my website.")
  
elif page == "Contact":
    st.header("Contact")
    st.write("This is the contact page. You can reach me at my email:")  
    email = st.text_input("Enter your email")
    message = st.text_area("Enter your message")
    if st.button("Submit"):
        if email and message:
            st.success("Your message has been sent!")
        else:
            st.error("Please fill in all fields.")
