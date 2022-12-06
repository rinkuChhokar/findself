from PIL import Image
import base64
import streamlit as st
import database as db
import pandas as pd



# example




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
          <source src="https://cdn.dribbble.com/uploads/39416/original/8d75bb5bf136d8292e8dc54a9629ff7c.mp4?1657824883")>
          Your browser does not support HTML5 video.
        </video>


        """

st.markdown(video_html, unsafe_allow_html=True)




data = db.fetch_details()

res = pd.DataFrame.from_dict(data)

res = res.sort_values(by=['Personality Type'])

res = res[["Date and Time","key","Name","Gender","Person","Personality Type"]]

def header(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:60px;border-radius:2%;font-weight:bolder;font-family:lato;">{url}</p>', unsafe_allow_html=True)


header("Admin Page")

# image = Image.open('home.jpg')

# st.image(image, caption='Stock Price')


def header1(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:30px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

header1("Login")


def header3(url):
    st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def callback():

    st.session_state.button_click = True


# Login Page-

uname = st.text_input("Username")
pswd = st.text_input("Password",type="password")

submit_button = st.button("Submit",on_click = callback)

# user-details

user_details = db.fetch_admin_details()

if 'button_click' not in st.session_state:

    st.session_state.button_click = False



if (submit_button or st.session_state.button_click):


    if uname == user_details[0]["key"] and pswd == user_details[0]["Password"]:

        st.markdown("<br>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
        header1(f"Welcome {uname}")

        st.markdown("<br>",unsafe_allow_html=True)

        header3("Click on the check box below to see the database")


        if st.checkbox("Show Database"):

            st.dataframe(res)


        col3, col4 = st.columns(2)

        with col3:

            header3("Click on button if want to download file ")


        with col4:
            
            @st.cache
            def convert_df(df):
                return df.to_csv().encode('utf-8')



            csv = convert_df(res)

            st.download_button(
               "Press to Download",
               csv,
               "file.csv",
               "text/csv",
               key='download-csv'
        
                )
    elif uname!="" and pswd!="":
        st.error("Username/password is incorrect!!")


st.markdown("<style>.css-16nzq6b{font-size:22px;}</style>",unsafe_allow_html=True)

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

# set_bg_hack("admin.jpg")


