import streamlit as st
from PIL import Image

# Loading Assets
img_rz = Image.open("cropped_img.png")

# Outlook
st.set_page_config(page_title="Rzgr - Programmer and Chess Player", page_icon=img_rz, layout="wide")

# Header Section
with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Hello, I'm Rzgr")
        st.title("A programmer and chess player")
        st.write("I have been programming since the age of 8 and playing chess for around a year.  \n My peak was 1437 which was in the top 5% of all online rapid chess players.")
        st.write("Access my trash profile [here.](https://www.chess.com/member/horsieenjoyer)")
    with right_column:
        st.image(img_rz, width=450)

st.write("---")

# More details
with st.container():
        st.header("My Hobbies")
        st.write("I like to watch anime, read manga from time to time, do programming and play chess. I also like working with interesting maths.  \n I enjoy learning languages but can only speak two fluently at the moment :pensive:")

st.write("---")

with st.container():
    st.header("Why and how I made this website")
    st.subheader("Why I made this website")
    st.write("I wanted to work on a simple and fun project while creating a place in which I could allow people to learn more about me, look at the projects I am working on and easily contact me.")
    st.subheader("How I made this website")
    st.write("I decided to make this website using [Streamlit](https://streamlit.io/), a tool which makes developing websites with python easy and [Python 3.9](https://www.python.org/), a simple and effective programming language.  \nWith a combination of both of these things plus another library or two I was able to create this website with ease in a short amount of time.")

st.write("---")

with st.container():
    st.header("My accounts and contact information")
    st.write("Github: [RzgrDev](https://github.com/RzgrDev)  \n Replit: [RzgrDev](https://replit.com/@RzgrDev)")
    st.write("Discord: Rzgr#6231")
    st.write("rzgrdeveloper@gmail.com")
