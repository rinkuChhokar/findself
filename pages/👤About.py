
from PIL import Image
import base64
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd



video_html = """
        <style>

        #myVideo {
          position: fixed;
          right: 0;
          bottom: 0;
          min-width: 100%; 
          min-height: 100%;
         filter: brightness(0.8);

        }

        .content {
          position: fixed;
          bottom: 0;
          background: rgba(0, 0, 0, 0.5);
          color: #f1f1f1;
          width: 100%;
          padding: 20px;


        }

        </style>    
        <video autoplay muted loop id="myVideo">
          <source src="https://cdn.dribbble.com/users/707385/screenshots/16254656/media/0e6c823b03e24c70e67cc213fbf28187.mp4")>
          Your browser does not support HTML5 video.
        </video>


        """

st.markdown(video_html, unsafe_allow_html=True)


def text(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:60px;border-radius:2%;font-weight:bolder;font-family:lato;">{url}</p>', unsafe_allow_html=True)


# Title

header("About Us")


def header1(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:30px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

text("Findself provide 3 types of test to check your personality")

def header3(url):
 st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:30px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


#  Various personalities-

st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:

    
    st.image("https://github.com/rinkuChhokar/images/blob/main/iPhone 13 Pro Mockup Right View.png?raw=true")

with col2:

    header3("MBTI Personality Test")
    text("A personality type system called the Myers-Briggs Type Indicator (or MBTI for short) categorises each person into 16 different personality types along four axes:-")
    text("Introversion (I) – Extroversion (E)")
    text("Intuition (N) – Sensing (S)")
    text("Thinking (T) – Feeling (F)")
    text("Judging (J) – Perceiving (P)")
    

st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

col3, col4 = st.columns(2, gap="large")

with col3:

    
    st.image("https://github.com/rinkuChhokar/images/blob/main/iPhone 13 Pro Mockup Right View (1).png?raw=true")

with col4:

    header3("Color Personality Test")
    text("In this Color Personality Test, you will discover the qualities and characteristics of your personality and that of the people you know based on the color your and their favorite color. These personality tests help you to facilitate the discovery of self as well as others at your workplace, family, school, groups, etc to enable deeper understanding and communications.")


st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)


col5, col6 = st.columns(2, gap="large")

with col5:

    
    st.image("https://github.com/rinkuChhokar/images/blob/main/iPhone 13 Pro Mockup Right View (2).png?raw=true")

with col6:

    header3("LOGB Personality Test")
    text("LOGB Personality test is a four-animal personality test in which a person's personality is classified as a lion, otter, beaver, or golden retriever. Each letter (L, O, G, B) represents a different personality type.")
    text("L-Lion")
    text("O-Otter")
    text("G-Golden Retriever")
    text("B-Beaver")


st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)


col7, col8 = st.columns(2, gap="large")

with col7:

    
    st.image("https://github.com/rinkuChhokar/images/blob/main/iPhone 13 Pro Mockup Right View (3).png?raw=true")

with col8:

    header3("User Page")
    text("When you take a personality type test on the Findself web app, you will be granted a unique id. If you wish to learn more about your personality type in the future, this unique id will be useful. Simply input your unique id on the User page, and the website will display your personality type. This unique key is incredibly secure, ensuring that no one else learns about your personality without your permission.")




st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 200px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 200px;
        margin-left: -200px;
    }
     
    """,
    unsafe_allow_html=True,
)


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# def set_bg_hack(main_bg):
#     '''
#     A function to unpack an image from root folder and set as bg.
 
#     Returns
#     -------
#     The background.
#     '''
#     # set bg name
#     main_bg_ext = "png"
        
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

# set_bg_hack("about.jpg")


