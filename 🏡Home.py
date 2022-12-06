import time
import base64
from PIL import Image
import streamlit as st
import pandas as pd
import database as datab
from datetime import datetime


import uuid

# Page configration
st.set_page_config(
    page_title="Findself App",
    page_icon="👪",
)


video_html = """
        <style>

        #myVideo {
          position: fixed;
          right: 0;
          bottom: 0;
          min-width: 100%; 
          min-height: 100%;
         filter: brightness(0.5);

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
          <source src="https://cdn.dribbble.com/users/707385/screenshots/18180953/media/abd8a0139c99f81e05c70ae830f150a9.mp4")>
          Your browser does not support HTML5 video.
        </video>


        """

st.markdown(video_html, unsafe_allow_html=True)





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



def header(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:60px;border-radius:2%;font-weight:bolder;font-family:lato;">{url}</p>', unsafe_allow_html=True)


def kid_test(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:45px;border-radius:2%;font-weight:bolder;font-family:lato;">{url}</p>', unsafe_allow_html=True)


def mbti_test(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:45px;border-radius:2%;font-weight:bolder;font-family:lato;">{url}</p>', unsafe_allow_html=True)



# Title

header("Findself")



# Introduction

# st.header("Introduction")
# st.text("Findself is a website which is designed to measure your Personality type. Completing the test should only take 15 minutes or so.")
def header1(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:30px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

header1("Introduction")


# Body-

def text(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:16px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def note(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:18px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


text("On Findself, you may learn about your personality type, your strengths, your limitations, and many other things. Answer honestly, not how you want other people to perceive you.")

st.markdown("<br>",unsafe_allow_html=True)

def header3(url):
 st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

note("Just keep in mind while taking this quiz:")
text("I. Every personality type can have a wonderful life, career, and relationships.")
text("II. You are not trapped by your personality; it is ultimately determined by your choices.")


st.markdown("<br>",unsafe_allow_html=True)
header3("------------Let's find out who you are------------")

def header4(url):
 st.markdown(f'<p style=color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


def header31(url):
 st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:25px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header312(url):
 st.markdown(f'<p style=color:#ffffff;font-size:25px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)



def callback():

    st.session_state.button_click = True

name = st.text_input("Name")
gender = st.radio(
 "Gender",
 ('Male', 'Female'),key=None)

option = st.selectbox(
 'Are you?',('Select option','Kid', 'Teenager', 'Adult'))


option1 = st.selectbox(
 'Choose type of personality test',('Select option','MBTI Personality Test', 'LOGB Personality Test', 'Color Personality Test'))





if len(name)!=0  and gender!=None and option!="Select option" and option1!="Select option" and option1=="MBTI Personality Test":


    
    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)

    mbti_test("MBTI Personality Test")
    
    q1 = st.selectbox("1. What would you prefer to do when you go somewhere for the day?",("Select option","Plan what you will do and when, or","Just go!!"),key=None)
    
    q2 = st.selectbox("2. Are you usually",("Select option","A 'good mixer' with groups of people, or","Rather quiet and reserved"),key=None)
    
    q3 = st.selectbox("3. When you have a special job to do, do you like to",("Select option","Organize it carefully before you start, or","Find out what is necessary as you go along"),key=None)
    
    q4 = st.selectbox("4. Is it a higher compliment to be called",("Select option","A person of real feeling, or","A consistently reasonable person"),key=None)
    
    q5 = st.selectbox("5. Among your friends are you",("Select option","Full of news about everybody, or","One of the last to hear what is going on"),key=None)
    
    q6 = st.selectbox("6. In reading for pleasure, do you",("Select option","Enjoy odd or original ways of saying things, or","Like writers to say exactly what they mean"),key=None)
    
    q7 = st.selectbox("7. Does following a schedule",("Select option","Appeal to you, or","Cramp you"),key=None)
    
    q8 = st.selectbox("8. Do you usually",("Select option","Value emotion more than logic, or","Value logic more than feelings"),key=None)
    
    q9 = st.selectbox("9. Do you",("Select option","Talk easily to almost anyone for as long as you have to, or","Find a lot to say only to certain people or under certain conditions"),key=None)
    
    q10 = st.selectbox("10. Are you more interested in",("Select option","What is actual","What is possible"),key=None)
    
    q11 = st.selectbox("11. Do you prefer to work",("Select option","To deadlines","Just 'whenever'"),key=None)
    
    q12 = st.selectbox("12. Are you more comfortable in making",("Select option","Logical judgments","Value judgments"),key=None)
    
    q13 = st.selectbox("13. Would you say you are more",("Select option","Serious and determined","Easy-going"),key=None)
    
    q14 = st.selectbox("14. At a party do you",("Select option","Interact with many, including strangers","Interact with a few, known to you"),key=None)
    
    q15 = st.selectbox("15. Which do you wish more for yourself",("Select option","Clarity of reason","Strength of compassion"),key=None)
    
    q16 = st.selectbox("16. Are you more likely to trust your",("Select option","Experience","Hunch"),key=None)
    
    q17 = st.selectbox("17. Are you more inclined to be",("Select option","Easy to approach","Somewhat reserved"),key=None)
    
    q18 = st.selectbox("18. Which rules you more",("Select option","Your head","Your heart"),key=None)
    
    q19 = st.selectbox("19. When the phone rings do you",("Select option","Hasten to get to it first","Hope someone else will answer"),key=None)
    
    q20 = st.selectbox("20. In company do you",("Select option","Initiate conversation","Wait to be approached"),key=None)
    

    submit_btn = st.button("Submit test")

    if submit_btn and q1!="Select option" and q2!="Select option" and q3!="Select option" and q4!="Select option" and q5!="Select option" and q6!="Select option" and q7!="Select option" and q8!="Select option" and q9!="Select option" and q10!="Select option" and q11!="Select option" and q12!="Select option" and q13!="Select option" and q14!="Select option" and q15!="Select option" and q16!="Select option" and q17!="Select option" and q18!="Select option" and q19!="Select option" and q20!="Select option":
        
        E = 0
        I = 0
        S = 0
        N = 0
        T = 0
        F = 0
        J = 0
        P = 0

        if q1 != "Select option" and q1 == "Plan what you will do and when, or":
            J+=2

        else:
            P+=2

        if q2 != "Select option" and q2 == "A 'good mixer' with groups of people, or":
            E+=2

        else:
            I+=2


        if q3 != "Select option" and q3 == "Organize it carefully before you start, or":
            J+=1

        else:
            P+=2

        
        if q4 != "Select option" and q4 == "A person of real feeling, or":
            F+=1

        else:
            T+=2


        if q5 != "Select option" and q5 == "Full of news about everybody, or":
            E+=2

        else:
            I+=1


        if q6 != "Select option" and q6 == "Enjoy odd or original ways of saying things, or":
            N+=0

        else:
            S+=1


        if q7 != "Select option" and q7 == "Appeal to you, or":
            J+=2

        else:
            P+=2


        if q8 != "Select option" and q8 == "Value emotion more than logic, or":
            F+=2

        else:
            T+=2


        if q9 != "Select option" and q9 == "Value emotion more than logic, or":
            E+=2

        else:
            I+=2


        if q10 != "Select option" and q10 == "What is actual":
            S+=2

        else:
            N+=1


        if q11 != "Select option" and q11 == "To deadlines":
            J+=2

        else:
            P+=2


        if q12 != "Select option" and q12 == "Logical judgments":
            T+=2

        else:
            F+=2


        if q13 != "Select option" and q13 == "Serious and determined":
            J+=2

        else:
            P+=2


        if q14 != "Select option" and q14 == "Interact with many, including strangers":
            E+=2

        else:
            I+=1


        if q15 != "Select option" and q15 == "Clarity of reason":
            T+=2

        else:
            F+=1


        if q16 != "Select option" and q16 == "Experience":
            S+=1

        else:
            N+=2


        if q17 != "Select option" and q17 == "Easy to approach":
            E+=2

        else:
            I+=2


        if q18 != "Select option" and q18 == "Your head":
            T+=2

        else:
            F+=1


        if q19 != "Select option" and q19 == "Hasten to get to it first":
            E+=2

        else:
            I+=1


        if q20 != "Select option" and q20 == "Initiate conversation":
            E+=2

        else:
            I+=1





        res = ""


        if E == I:

            res+= "I"
        else:
            if E > I:
                res+="E"

            else:
                res+="I"

        if S == N:
            res+="N"


        else:
            if S > N:
                res+="S"

            else:
                res+="N"


        if T == F:
            if gender == "Male":
                res+="T"
            else:
                res+="F"

        else:
            if T > F:
                res+="T"

            else:
                res+="F"


        if J == P:
            res+="P"


        else:
            if J > P:
                res+="J"

            else:
                res+="P"

        if res == "ESTJ":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Extraverted Sensing Thinking Judging")
            header31("Executive")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://assets-metrostyle.abs-cbn.com/prod/metrostyle/attachments/0103cade-f05c-498c-b7de-954c77524279_fullsizephoto968194.jpg")
            
            with col2:
                header4("ESTJs are hardworking traditionalists, eager to take charge in organizing projects and people. Orderly, rule-abiding, and conscientious, ESTJs like to get things done, and tend to go about projects in a systematic, methodical way.")

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Dedicated")
                header4("2. Strong-willed")
                header4("3. Direct and Honest")
                header4("4. Loyal, Patient and Reliable")


            with col4:

                header312("Weaknesses")
                header4("1. Uncomfortable with Unconventional Situations")
                header4("2. Too Focused on Social Status")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/1-6.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Kamala Harris</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/4-6.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Michelle Obama</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/6-6.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Ivanka Trump</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)



        elif res == "ENTJ":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Extraverted Intuitive Thinking Judging")
            header31("Commander")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://i.pinimg.com/736x/0c/f4/ba/0cf4ba53a0a1ebcf7ab5468616f83b57.jpg")
            
            with col2:
                header4("ENTJs are strategic leaders, motivated to organize change. They are quick to see inefficiency and conceptualize new solutions, and enjoy developing long-range plans to accomplish their vision. They excel at logical reasoning and are usually articulate and quick-witted.")
            

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Efficient")
                header4("2. Energetic")
                header4("3. Self-Confident")
                header4("4. Strong-Willed")


            with col4:

                header312("Weaknesses")
                header4("1. Impatient")
                header4("2. Cold and Ruthless")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/ENTJ-3-1.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Steve Jobs</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/ENTJ-1.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Simon Cowell</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/ENTJ-6-1.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Gillian Anderson</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)




        elif res == "ESFJ":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Extraverted Sensing Feeling Judging")
            header31("Caregiver")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://pbs.twimg.com/media/EejEZ0cUcAAhBHq.jpg")
            
            with col2:
                header4("ESFJ, also known as 'The Caregiver' or 'The Consul,' is one of the 16 personality types identified by the Myers-Briggs Type Indicator. People with an ESFJ personality type tend to be outgoing, loyal, organized, and tender-hearted. ESFJs gain energy from interacting with other people.")
            

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Strong Practical Skills")
                header4("2. Strong Sense of Duty")
                header4("3. Very Loyal")
                header4("4. Sensitive and Warm")


            with col4:

                header312("Weaknesses")
                header4("1. Too Selfless ")
                header4("2. Inflexible")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/4-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Taylor Swift</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/15-3.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Chris Evans</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/10-3.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Ariana Grande</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)



        
        elif res == "ENFJ":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Extraverted Intuitive Feeling Judging")
            header31("Giver")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://media.timeout.com/images/105875926/750/422/image.jpg")
            
            with col2:
                header4("ENFJ indicates a person who is energized by time spent with others (Extraverted), who focuses on ideas and concepts rather than facts and details (iNtuitive), who makes decisions based on feelings and values (Feeling) and who prefers to be planned and organized rather than spontaneous and flexible (Judging).")
            

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Reliable")
                header4("2. Passionate")
                header4("3. Charismatic")
                header4("4. Receptive")


            with col4:

                header312("Weaknesses")
                header4("1. Overly Idealistic")
                header4("2. Intense")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/ENFJ-7-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Barack Obama</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/ENFJ-9-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Drake</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/ENFJ-21-1.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Emma Stone</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)

            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <a class="btn btn-primary" href="http://localhost:8501/" target="_self" role="button">Play Again</a>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)




        elif res == "ISTJ":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Introverted Sensing Thinking Judging")
            header31("Logistician")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://3.bp.blogspot.com/-4V0TX-nahtc/VJ7WbxtIwdI/AAAAAAAABrw/eyzcUbxYMFI/s1600/10609472_1497427670512774_7223601241914768748_n.jpg")
            
            with col2:
                header4("ISTJ indicates a person who is energized by time spent alone (Introverted), who focuses on facts and details rather than ideas and concepts (Sensing), who makes decisions based on logic and reason (Thinking) and who prefers to be planned and organized rather than spontaneous and flexible (Judging).")
            

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Honest and Direct")
                header4("2. Strong-willed and Dutiful")
                header4("3. Very Responsible")
                header4("4. Calm and Practical")


            with col4:

                header312("Weaknesses")
                header4("1. Always by the Book")
                header4("2. Often Unreasonably Blame Themselves")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/2-3.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Queen Elizabeth II</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/4-3.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Jeff Bezos</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/5-3.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Warren Buffet</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)




        elif res == "ISFJ":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Introverted Sensing Feeling Judging")
            header31("Nurturer")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://www.kdramalove.com/Just-Between-Lovers_MomDaughter.jpg")
            
            with col2:
                header4(" ISFJ stands for introverted, sensing, feeling, judging. This personality type is given the nickname 'The Protector' or 'The Defender,' and for good reason. 2 People who have ISFJ personalities are known for being warm-hearted, responsible, and reserved. The ENTP personality type is the opposite.")
            

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Supportive")
                header4("2. Reliable")
                header4("3. Observant")
                header4("4. Enthusiastic")


            with col4:

                header312("Weaknesses")
                header4("1. Overly Humble")
                header4("2. Taking Things Personally")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/21-1.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Selena Gomez</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/11-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Ed Sheeran</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/10-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Emma Watson</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <a class="btn btn-success" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)





        elif res == "INTJ":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Introverted Intuitive Thinking Judging")
            header31("Scientist")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://media.starbiz.net/2020/08/upcoming-drama-alice-stills-kim-hee-sun-intelligent-scientist.jpg")
            
            with col2:
                header4("People with an INTJ personality type tend to be confident, analytical, and ambitious in their behavior. They love to pursue knowledge and tend to be very logically minded. They are independent thinkers focused on solving the world's problems.")
            

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Rational")
                header4("2. Independent")
                header4("3. Curious")
                header4("4. Determined")


            with col4:

                header312("Weaknesses")
                header4("1. Overly Critical")
                header4("2. Dismissive of Emotions")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/INTJ-2-1.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Elon Musk</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/INTJ-4.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Mark Zuckerberg </h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/INTJ-10.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Nikola Tesla</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)




        elif res == "INFJ":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Introverted Intuitive Feeling Judging")
            header31("Advocate")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://dramaswithasideofkimchi.com/wp-content/uploads/2018/06/img_5314.jpg")
            
            with col2:
                header4("Scoring as an INFJ means that your personality type is best described as Introverted, Intuitive, Feeling, and Judging. Sometimes referred to as the 'Advocate' or the 'Idealist,' people with this personality type often feel misunderstood.")
            

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Creative")
                header4("2. Insightful")
                header4("3. Passionate")
                header4("4. Principled")


            with col4:

                header312("Weaknesses")
                header4("1. Avoiding the Ordinary")
                header4("2. Sensitive to Criticism")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/INFJ-6-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">J.K. Rowling</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/INFJ-2-3.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Nelson Mandela</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/INFJ-7-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Benedict Cumberbatch</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)




        elif res == "ESTP":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Extraverted Sensing Thinking Perceiving")
            header31("Entrepreneur")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://i.pinimg.com/originals/55/d6/d3/55d6d3d3425f9572162db1ccd2d5d3d7.jpg")
            
            with col2:
                header4("ESTP indicates a person who is energized by time spent with others (Extraverted), who focuses on facts and details rather than ideas and concepts (Sensing), who makes decisions based on logic and reason (Thinking) and who prefers to be spontaneous and flexible rather than planned and organized (Perceiving).")
            

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Bold")
                header4("2. Rational and Practical")
                header4("3. Direct")
                header4("4. Sociable")


            with col4:

                header312("Weaknesses")
                header4("1. Insensitive")
                header4("2. Impatient")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/3-7.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Dwayne Johnson</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/7-7.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Madonna</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/5-7.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Angelina Jolie</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)




        elif res == "ESFP":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Extraverted Sensing Feeling Perceiving")
            header31("Entertainer")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://pbs.twimg.com/media/ELTUTE-U4AYWoWB.jpg")
            
            with col2:
                header4("People with ESFP personality types are often described as spontaneous, resourceful, and outgoing. They love being the center of attention and are often described as entertainers or “class clowns.” ESFP is the opposite of the INTJ personality type.")
            

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Bold")
                header4("2. Excellent People Skills")
                header4("3. Aesthetics and Showmanship")
                header4("4. Observant")


            with col4:

                header312("Weaknesses")
                header4("1. Sensitive")
                header4("2. Easily Bored")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/5-5.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Cristiano Ronaldo</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/4-5.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Camilla Cabello</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/12-6.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Leonardo DiCaprio</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)



        elif res == "ENTP":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Extraverted Intuitive Thinking Perceiving")
            header31("Debater")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://4.bp.blogspot.com/-SvcwyAQitWE/Wra30rGidmI/AAAAAAAACwM/R8uxpnB_CuQ8RJZVZahhACbXPa_yzHyjgCLcBGAs/s1600/Go%2BHye%2BRan%2BMisty.png")
            
            with col2:
                header4("A Debater (ENTP) is a person with the Extraverted, Intuitive, Thinking, and Prospecting personality traits. They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility. They pursue their goals vigorously despite any resistance they might encounter.")


            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Knowledgeable")
                header4("2. Quick Thinkers")
                header4("3. Excellent Brainstormers")
                header4("4. Energetic")


            with col4:

                header312("Weaknesses")
                header4("1. Very Argumentative")
                header4("2. Intolerant")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.egypttoday.com/siteimages/Larg/202201191141444144.jpg" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Thomas Edison</h6></div>
                      <div class="col-sm-4"><img src="https://images.complex.com/complex/images/c_fill,dpr_auto,f_auto,q_90,w_1400/fl_lossy,pg_1/ce8yuj7kxprixv6ojqcs/ryan-reynolds" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Ryan Reynolds</h6></div>
                      <div class="col-sm-4"><img src="https://images.indianexpress.com/2021/07/robert-downey-jr-1200.jpeg" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Robert Downey Jr.</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)




        elif res == "ENFP":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Extraverted Intuitive Feeling Perceiving")
            header31("Inspirer")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://1739752386.rsc.cdn77.org/data/images/full/247919/melancholia.jpg")
            
            with col2:
                header4("ENFPs are people-centered creators with a focus on possibilities and a contagious enthusiasm for new ideas, people and activities. Energetic, warm, and passionate, ENFPs love to help other people explore their creative potential.")


            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Curious")
                header4("2. Perceptive")
                header4("3. Enthusiastic")
                header4("4. Good-Natured")


            with col4:

                header312("Weaknesses")
                header4("1. Overly Optimistic")
                header4("2. Restless")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/ENFP-15-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Daniel Radcliffe</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/ENFP-24.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Jennifer Lawrence</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/ENFP-19-1.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Chris Pratt</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)




        elif res == "ISTP":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Introverted Sensing Thinking Perceiving")
            header31("Virtuoso")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://kdramadiary.com/wp-content/uploads/2021/04/seo-in-guk-pipeline-kdramadiary.jpg")
            
            with col2:
                header4("A Virtuoso (ISTP) is someone with the Introverted, Observant, Thinking, and Prospecting personality traits. They tend to have an individualistic mindset, pursuing goals without needing much external connection. They engage in life with inquisitiveness and personal skill, varying their approach as needed.")
            

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Optimistic and Energetic")
                header4("2. Creative and Practical")
                header4("3. Know How to Prioritize")
                header4("4. Great in a Crisis")


            with col4:

                header312("Weaknesses")
                header4("1. Private and Reserved")
                header4("2. Insensitive")


            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/ISTP-9-1.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Tom Cruise</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/ISTP-8-1.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Scarlett Johansson</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/ISTP-18.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Bear Grylls</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)




        elif res == "ISFP":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Introverted Sensing Feeling Perceiving")
            header31("Artist")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://media.starbiz.net/2020/10/16-times-iu-had-us-feeling-super-soft-in-the-fluffiest-over-sized-sweaters-3.jpg")
            
            with col2:
                header4("ISFPs are gentle caretakers who live in the present moment and enjoy their surroundings with cheerful, low-key enthusiasm. They are flexible and spontaneous, and like to go with the flow to enjoy what life has to offer. ISFPs are quiet and unassuming, and may be hard to get to know.")
            

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Charming")
                header4("2. Artistic")
                header4("3. Imaginative")
                header4("4. Curious")


            with col4:

                header312("Weaknesses")
                header4("1. Overly Competitive")
                header4("2. Unpredictable")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/Zodiac-Famous-People.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Michael Jackson</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/7-4.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Billie Eilish</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/04/15-5.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Dua Lipa</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)




        elif res == "INTP":

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Introverted Intuitive Thinking Perceiving")
            header31("Thinker")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://kdramadiary.com/wp-content/uploads/2020/09/hyun-bin-summer-ad-kdramadiary-f.jpg")
            
            with col2:
                header4(" People who score as INTP are often described as quiet and analytical. They enjoy spending time alone, thinking about how things work and coming up with solutions to problems. INTPs have a rich inner world and would rather focus their attention on their internal thoughts rather than the external world.")


            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Analytical")
                header4("2. Curious")
                header4("3. Open-Minded")
                header4("4. Objective")


            with col4:

                header312("Weaknesses")
                header4("1. Dissatisfied")
                header4("2. Impatient")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/INTP-5-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Albert Einstein</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/INTP-22.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Bill Gates</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/INTP-8-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Rowan Atkinson</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)



        else:

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type-")
            header(res)
            header1("Introverted Intuitive Feeling Perceiving")
            header31("Idealist")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://m.media-amazon.com/images/M/MV5BMmUwMTIxMjctZDk1OS00Y2M4LTlkMzAtNjNlNmM0YzU1NGIyXkEyXkFqcGdeQXVyODA4ODIwNDM@._V1_.jpg")
            
            with col2:
                header4("The INFP personality type is often described as an 'idealist' or 'mediator' personality. People with this kind of personality tend to be introverted, idealistic, creative, and driven by high values. INFPs also have strong interests in making the world a better place.")
            

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,res)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Generous")
                header4("2. Empathetic")
                header4("3. Creative")
                header4("4. Passionate")


            with col4:

                header312("Weaknesses")
                header4("1. Self-Isolating")
                header4("2. Emotionally Vulnerable")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            header31("Famous people of this personality type")
            html_code ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div class="row">
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/3-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Princess Diana</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/14-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Keanu Reeves</h6></div>
                      <div class="col-sm-4"><img src="https://www.sosyncd.com/wp-content/uploads/2021/05/15-2.png" class="img-fluid" alt="Responsive image"><h6 style="text-align:center">Robert Pattinson</h6></div>
                    </div>
                </div>
                """

            st.markdown(html_code,unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)
            








elif len(name)!=0 and gender!=None and option!="Select option" and option1!="Select option" and option1=="LOGB Personality Test":

    

    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    kid_test("LOGB Personality Test")
    q1 = "q1"
    if q1 not in st.session_state:
        st.session_state[q1] = ""

    def assign(i,val):
        st.session_state[i] = val

    header312("1. Which of the following best describes you when you're with your friends?")
    
   
    col1, col2, col3, col4 = st.columns(4)
    with col1:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/1a.PNG")

        btn = st.button("I take charge",key=0)
        if btn:

            assign(q1,"I take charge")


    with col2:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/1b.PNG")
 
        btn = st.button("I can sell an idea",key=1)
        if btn:

            assign(q1,"I can sell an idea")


    with col3:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/1c.PNG")

        btn = st.button("I'm quite serious",key=2)
        
        if btn:

            assign(q1,"I'm quite serious")


    with col4:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/1d.PNG")
 
        btn = st.button("I'm a good listener",key=3)
        
        if btn:

            assign(q1,"I'm a good listener")

    st.write(f"You chose-{st.session_state[q1]}")



    q2 = "q2"
    if q2 not in st.session_state:
        st.session_state[q2] = ""


    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("2. What is your most likely sentence?")
    
    col5, col6, col7, col8 = st.columns(4)
    with col5:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/2a.PNG")

        btn2 = st.button("'let's do it my way!'",key=4)
        if btn2:
            assign(q2,"'let's do it my way!'")


    with col6:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/2b.PNG")

        btn2 = st.button("'no worries bro!'",key=5)
        if btn2:
            assign(q2,"'no worries bro!'")


    with col7:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/2c.PNG")

        btn2 = st.button("'how does that work?'",key=6)
        
        if btn2:
            assign(q2,"'how does that work?'")


    with col8:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/2d.PNG")

        btn2 = st.button("'let's keep the peace'",key=7)
        
        if btn2:
            assign(q2,"'let's keep the peace'")

    st.write(f"You chose-{st.session_state[q2]}")




    q3 = "q3"
    if q3 not in st.session_state:
        st.session_state[q3] = ""

    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("3. Which way of thinking best describes you?")


    col9, col10, col11, col12 = st.columns(4)
    with col9:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/3a.PNG")

        btn3 = st.button("calm",key=8)
        if btn3:
            assign(q3,"calm")


    with col10:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/3b.PNG")

        btn3 = st.button("practical",key=9)
        if btn3:
            assign(q3,"practical")


    with col11:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/3c.PNG")

        btn3 = st.button("independent",key=10)
        
        if btn3:
            assign(q3,"independent")


    with col12:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/3d.PNG")

        btn3 = st.button("bright ideas",key=11)
        
        if btn3:
            assign(q3,"bright ideas")
    st.write(f"You chose-{st.session_state[q3]}")




    q4 = "q4"
    if q4 not in st.session_state:
        st.session_state[q4] = ""


    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("4. Plans have changed how do you deal?")
    
    col13, col14, col15, col16 = st.columns(4)
    with col13:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/4a.PNG")

        btn4 = st.button("It's exciting I enjoy change",key=12)
        if btn4:
            assign(q4,"It's exciting I enjoy change")


    with col14:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/4b.PNG")

        btn4 = st.button("'I'll work it out'",key=13)
        if btn4:
            assign(q4,"'I'll work it out'")


    with col15:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/4c.PNG")

        btn4 = st.button("I like challenges to overcome",key=14)
        
        if btn4:
            assign(q4,"I like challenges to overcome")


    with col16:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/4d.PNG")

        btn4 = st.button("I'm patient and flexible",key=15)
        
        if btn4:
            assign(q4,"I'm patient and flexible")

    st.write(f"You chose-{st.session_state[q4]}")





    q5 = "q5"
    if q5 not in st.session_state:
        st.session_state[q5] = ""


    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("5. Have you ever been told you're a little loud?")

    
    col17, col18, col19, col20 = st.columns(4)
    with col17:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/5a.PNG")

        btn5 = st.button("Yes but it's a good thing",key=16)
        if btn5:
            assign(q5,"Yes but it's a good thing")


    with col18:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/5b.PNG")

        btn5 = st.button("I was just excited",key=17)
        if btn5:
            assign(q5,"I was just excited")


    with col19:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/5c.PNG")

        btn5 = st.button("Maybe once or twice",key=18)
        
        if btn5:
            assign(q5,"Maybe once or twice")


    with col20:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/5d.PNG")

        btn5 = st.button("No way!",key=19)
        
        if btn5:
            assign(q5,"No way!")

    st.write(f"You chose-{st.session_state[q5]}")





    q6 = "q6"
    if q6 not in st.session_state:
        st.session_state[q6] = ""

    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("6. Which of these describes you best?")

    
    col21, col22, col23, col24 = st.columns(4)
    with col21:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/6a.PNG")

        btn6 = st.button("Puts other people first",key=20)
        if btn6:
            assign(q6,"Puts other people first")


    with col22:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/6b.PNG")

        btn6 = st.button("Neat and tidy",key=21)
        if btn6:
            assign(q6,"Neat and tidy")


    with col23:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/6c.PNG")

        btn6 = st.button("People like me",key=22)
        
        if btn6:
            assign(q6,"People like me")


    with col24:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/6d.PNG")

        btn6 = st.button("Confident and brave",key=23)
        
        if btn6:
            assign(q6,"Confident and brave")

    st.write(f"You chose-{st.session_state[q6]}")





    q7 = "q7"
    if q7 not in st.session_state:
        st.session_state[q7] = ""

    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("7. If your friends had to describe you in a single word, it would be-")

    
    col25, col26, col27, col28 = st.columns(4)
    with col25:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/7a.PNG")

        btn7 = st.button("Friendly",key=24)
        if btn7:
            assign(q7,"Friendly")


    with col26:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/7b.PNG")

        btn7 = st.button("Loyal",key=25)
        if btn7:
            assign(q7,"Loyal")


    with col27:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/7c.PNG")

        btn7 = st.button("Reliable",key=26)
        
        if btn7:
            assign(q7,"Reliable")


    with col28:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/7d.PNG")

        btn7 = st.button("Competitive",key=27)
        
        if btn7:
            assign(q7,"Competitive")

    st.write(f"You chose-{st.session_state[q7]}")





    q8 = "q8"
    if q8 not in st.session_state:
        st.session_state[q8] = ""


    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("8. When you're angry at someone, you tend to-")

    
    col29, col30, col31, col32 = st.columns(4)
    with col29:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/8a.PNG",width=150)
        
        btn8 = st.button("Keep it to yourself",key=28)
        if btn8:
            assign(q8,"Keep it to yourself")


    with col30:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/8b.PNG",width=170)
        btn8 = st.button("Yell at them",key=29)
        if btn8:
            assign(q8,"Yell at them")


    with col31:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/8c.PNG",width=170)
        btn8 = st.button("Make fun of them",key=30)
        
        if btn8:
            assign(q8,"Make fun of them")


    with col32:

        st.image("https://raw.githubusercontent.com/rinkuChhokar/images/main/8d.PNG",width=150)

        btn8 = st.button("People don't make me frustrated very often",key=31)
        
        if btn8:
            assign(q8,"People don't make me frustrated very often")

    st.write(f"You chose-{st.session_state[q8]}")

    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)

    submit_btn = st.button("Submit test")

    if submit_btn and st.session_state[q1]!="" and st.session_state[q2]!="" and st.session_state[q3]!="" and st.session_state[q4]!="" and st.session_state[q5]!="" and st.session_state[q6]!="" and st.session_state[q7]!="" and st.session_state[q8]!="":


        l = 0
        o = 0
        g = 0
        b = 0

        if st.session_state[q1]=="I take charge":
            l+=1

        elif st.session_state[q1]=="I can sell an idea":
            o+=1

        elif st.session_state[q1]=="I'm quite serious":
            b+=1

        else:
            g+=1


        if st.session_state[q2]=="'let's do it my way!'":
            l+=1

        elif st.session_state[q2]=="'no worries bro!'":
            o+=1

        elif st.session_state[q2]=="'how does that work?'":
            b+=1

        else:
            g+=1



        if st.session_state[q3]=="calm":
            g+=1

        elif st.session_state[q3]=="practical":
            b+=1

        elif st.session_state[q3]=="independent":
            l+=1

        else:
            o+=1


        if st.session_state[q4]=="It's exciting I enjoy change":
            o+=1

        elif st.session_state[q4]=="'I'll work it out'":
            b+=1

        elif st.session_state[q4]=="I like challenges to overcome":
            l+=1

        else:
            g+=1



        if st.session_state[q5]=="Yes but it's a good thing":
            g+=1

        elif st.session_state[q5]=="I was just excited":
            o+=1

        elif st.session_state[q5]=="Maybe once or twice":
            b+=1

        else:
            l+=1



        if st.session_state[q6]=="Puts other people first":
            g+=1

        elif st.session_state[q6]=="Neat and tidy":
            b+=1

        elif st.session_state[q6]=="People like me":
            o+=1

        else:
            l+=1



        if st.session_state[q7]=="Friendly":
            o+=1

        elif st.session_state[q7]=="Loyal":
            g+=1

        elif st.session_state[q7]=="Reliable":
            b+=1

        else:
            l+=1



        if st.session_state[q8]=="Keep it to yourself":
            g+=1

        elif st.session_state[q8]=="Yell at them":
            l+=1

        elif st.session_state[q8]=="Make fun of them":
            o+=1

        else:
            b+=1


        choice = max(l,o,g,b)

        if choice == l:

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type animal-")
            header("Lion")
            header31("Strong")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)


            col1,col2 = st.columns(2)

            with col1:

                st.image("https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1386&q=80")
            
            with col2:
                header4("Lions are leaders. They are usually the bosses at work...or believe they are! They are decisive, bottom-line people who observe rather than watch or listen. They enjoy solving problems. They are typically individualists who seek out new adventures and opportunities.")

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,"Lion")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            
            col3,col4 = st.columns(2)
            

            with col3:

                header312("Strengths")
                header4("1. Goal-oriented")
                header4("2. Independent")
                header4("3. Takes charge")
                header4("4. Competitive")


            with col4:

                header312("Weaknesses")
                header4("1. Impatient")
                header4("2. Poor listener")

            st.session_state[q1] = st.session_state[q2] = st.session_state[q3] = st.session_state[q4] = st.session_state[q5] = st.session_state[q6] = st.session_state[q7] = st.session_state[q8] = ""

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)



        elif choice == o:

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type animal-")
            header("Otter")
            header31("Smart")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)
            
            col1,col2 = st.columns(2)

            with col1:

                st.image("https://images.unsplash.com/photo-1595703013566-db085ae93c04?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1376&q=80")
            
            with col2:
                header4("Otters are exuberant, fun-seeking individuals who enjoy talking! They are excellent motivators and require an environment in which they can speak freely and vote on major decisions. Because of their outgoing personalities, otters make excellent networkers—they usually know a lot of people who know a lot of people.")


            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            datab.insert_values(str(dt_string),str(uid),name,gender,option,"Otter")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Enthusiastic")
                header4("2. Good Communicator")
                header4("3. Outgoing")
                header4("4. Fun-loving")


            with col4:

                header312("Weaknesses")
                header4("1. Impulsive")
                header4("2. Can be too talkative")

            st.session_state[q1] = st.session_state[q2] = st.session_state[q3] = st.session_state[q4] = st.session_state[q5] = st.session_state[q6] = st.session_state[q7] = st.session_state[q8] = ""
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)



        elif choice == g:

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type animal-")
            header("Golden Retriever")
            header31("Loyal")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://images.unsplash.com/photo-1633722715463-d30f4f325e24?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80")
            
            with col2:
                header4("These people can be described in one word: LOYAL. They are so devoted that they can endure the most emotional pain and punishment in a relationship and still remain committed. They are excellent listeners, empathetic, and encouraging.")


            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            datab.insert_values(str(dt_string),str(uid),name,gender,option,"Golden Retriever")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Patient")
                header4("2. Stable")
                header4("3. Compassionate")
                header4("4. Reliable")


            with col4:

                header312("Weaknesses")
                header4("1. Indecisive")
                header4("2. Fears change")

            st.session_state[q1] = st.session_state[q2] = st.session_state[q3] = st.session_state[q4] = st.session_state[q5] = st.session_state[q6] = st.session_state[q7] = st.session_state[q8] = ""
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)


        
        else:

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type animal-")
            header("Beaver")
            header31("Practical")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://images.unsplash.com/photo-1544878221-efc436f31748?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80")
            
            with col2:
                header4("Beavers have a strong desire to do things correctly and according to the rules. They are, in fact, the type of people who read instruction manuals. They excel at quality control in the office and will provide quality control in any situation or field that requires accuracy, such as accounting, engineering, and so on.")

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            datab.insert_values(str(dt_string),str(uid),name,gender,option,"Beaver")

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Analytical")
                header4("2. Controlled")
                header4("3. Accurate")
                header4("4. Orderly")


            with col4:

                header312("Weaknesses")
                header4("1. Overly cautious")
                header4("2. Overly sensitive")

            st.session_state[q1] = st.session_state[q2] = st.session_state[q3] = st.session_state[q4] = st.session_state[q5] = st.session_state[q6] = st.session_state[q7] = st.session_state[q8] = ""
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)










elif len(name)!=0 and gender!=None and option!="Select option" and option1!="Select option" and option1=="Color Personality Test":
    

    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    
    mbti_test("Color Personality Test")


    q1 = "q1"
    if q1 not in st.session_state:
        st.session_state[q1] = ""

    def assign(i,val):
        st.session_state[i] = val

    header312("1. You might display these qualities-")
    
   
    col1, col2, col3, col4 = st.columns(4)
    with col1:

        st.image("https://images.unsplash.com/photo-1576618148400-f54bed99fcfd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn = st.button("Responsibility",key=0)
        if btn:

            assign(q1,"Responsibility")


    with col2:

        st.image("https://images.unsplash.com/photo-1505394033641-40c6ad1178d7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1487&q=80")
 
        btn = st.button("Objectivity",key=1)
        if btn:

            assign(q1,"Objectivity")


    with col3:

        st.image("https://images.unsplash.com/photo-1590080875515-8a3a8dc5735e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn = st.button("Loyalty",key=2)
        
        if btn:

            assign(q1,"Loyalty")


    with col4:

        st.image("https://images.unsplash.com/photo-1588195540875-63c2be0f60ae?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1498&q=80")
 
        btn = st.button("Courage",key=3)
        
        if btn:

            assign(q1,"Courage")

    st.write(f"You chose-{st.session_state[q1]}")



    q2 = "q2"
    if q2 not in st.session_state:
        st.session_state[q2] = ""


    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("2. You could view yourself as-")
    
    col5, col6, col7, col8 = st.columns(4)
    with col5:

        st.image("https://images.unsplash.com/photo-1546039907-7fa05f864c02?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn2 = st.button("Stable",key=4)
        if btn2:
            assign(q2,"Stable")


    with col6:

        st.image("https://images.unsplash.com/photo-1586190848861-99aa4a171e90?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn2 = st.button("Superior intellect",key=5)
        if btn2:
            assign(q2,"Superior intellect")


    with col7:

        st.image("https://images.unsplash.com/photo-1490457843367-34b21b6ccd85?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1444&q=80")

        btn2 = st.button("Warm",key=6)
        
        if btn2:
            assign(q2,"Warm")


    with col8:

        st.image("https://images.unsplash.com/photo-1540832804691-58c47b913830?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn2 = st.button("Fun-loving, enjoys life",key=7)
        
        if btn2:
            assign(q2,"Fun-loving, enjoys life")

    st.write(f"You chose-{st.session_state[q2]}")




    q3 = "q3"
    if q3 not in st.session_state:
        st.session_state[q3] = ""

    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("3. Others may perceive you as-")


    col9, col10, col11, col12 = st.columns(4)
    with col9:

        st.image("https://images.unsplash.com/photo-1583401495411-d693f393c074?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn3 = st.button("Bossy",key=8)
        if btn3:
            assign(q3,"Bossy")


    with col10:

        st.image("https://images.unsplash.com/photo-1563117983-1879e02d1340?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn3 = st.button("Emotionally controlled",key=9)
        if btn3:
            assign(q3,"Emotionally controlled")


    with col11:

        st.image("https://images.unsplash.com/photo-1657101455328-6821c90b0ad3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1481&q=80")

        btn3 = st.button("Hopelessly naïve",key=10)
        
        if btn3:
            assign(q3,"Hopelessly naïve")


    with col12:

        st.image("https://images.unsplash.com/photo-1646990378605-aea406fc1868?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn3 = st.button("Not able to stay on task",key=11)
        
        if btn3:
            assign(q3,"Not able to stay on task")
    st.write(f"You chose-{st.session_state[q3]}")




    q4 = "q4"
    if q4 not in st.session_state:
        st.session_state[q4] = ""


    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("4. Things that annoy you-")
    
    col13, col14, col15, col16 = st.columns(4)
    with col13:

        st.image("https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1536&q=80")

        btn4 = st.button("Irresponsibility",key=12)
        if btn4:
            assign(q4,"Irresponsibility")


    with col14:

        st.image("https://images.unsplash.com/photo-1617455559706-fa196228c05d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn4 = st.button("Routine",key=13)
        if btn4:
            assign(q4,"Routine")


    with col15:

        st.image("https://images.unsplash.com/photo-1619371812376-e34e819eb8f1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1505&q=80")

        btn4 = st.button("Lying",key=14)
        
        if btn4:
            assign(q4,"Lying")


    with col16:

        st.image("https://images.unsplash.com/photo-1628505048571-327399c9324c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1429&q=80")

        btn4 = st.button("Rules and laws",key=15)
        
        if btn4:
            assign(q4,"Rules and laws")

    st.write(f"You chose-{st.session_state[q4]}")





    q5 = "q5"
    if q5 not in st.session_state:
        st.session_state[q5] = ""


    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("5. Things you do that annoy others-")

    
    col17, col18, col19, col20 = st.columns(4)
    with col17:

        st.image("https://images.unsplash.com/photo-1585238341267-1cfec2046a55?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1474&q=80")

        btn5 = st.button("Being obsessive",key=16)
        if btn5:
            assign(q5,"Being obsessive")


    with col18:

        st.image("https://images.unsplash.com/photo-1566217688581-b2191944c2f9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn5 = st.button("Blowing up when criticized",key=17)
        if btn5:
            assign(q5,"Blowing up when criticized")


    with col19:

        st.image("https://images.unsplash.com/photo-1626869300065-3bfc3a8b2e42?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1451&q=80")

        btn5 = st.button("Suppressing problems",key=18)
        
        if btn5:
            assign(q5,"Suppressing problems")


    with col20:

        st.image("https://images.unsplash.com/photo-1550950158-d0d960dff51b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn5 = st.button("Being quick-tempered",key=19)
        
        if btn5:
            assign(q5,"Being quick-tempered")

    st.write(f"You chose-{st.session_state[q5]}")





    q6 = "q6"
    if q6 not in st.session_state:
        st.session_state[q6] = ""

    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("6. You enjoy compliments when-")

    
    col21, col22, col23, col24 = st.columns(4)
    with col21:

        st.image("https://images.unsplash.com/photo-1585238342024-78d387f4a707?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn6 = st.button("Sincere appreciation is shown",key=20)
        if btn6:
            assign(q6,"Sincere appreciation is shown")


    with col22:

        st.image("https://images.unsplash.com/photo-1654722906311-19970c50bed8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1462&q=80")

        btn6 = st.button("The quality of your work is recognized",key=21)
        if btn6:
            assign(q6,"The quality of your work is recognized")


    with col23:

        st.image("https://images.unsplash.com/photo-1628840042765-356cda07504e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn6 = st.button("You are praised with an energetic and enthusiastic manner",key=22)
        
        if btn6:
            assign(q6,"You are praised with an energetic and enthusiastic manner")


    with col24:

        st.image("https://images.unsplash.com/photo-1585828922344-85c9daa264b0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1540&q=80")

        btn6 = st.button("You are praised with actions",key=23)
        
        if btn6:
            assign(q6,"You are praised with actions")

    st.write(f"You chose-{st.session_state[q6]}")





    q7 = "q7"
    if q7 not in st.session_state:
        st.session_state[q7] = ""

    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("7. On a bad day, you might-")

    
    col25, col26, col27, col28 = st.columns(4)
    with col25:

        st.image("https://images.unsplash.com/photo-1607664608695-45aaa6d621fc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn7 = st.button("Complain",key=24)
        if btn7:
            assign(q7,"Complain")


    with col26:

        st.image("https://images.unsplash.com/photo-1614061813295-0e0f82273dc3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn7 = st.button("Become overly indecisive",key=25)
        if btn7:
            assign(q7,"Become overly indecisive")


    with col27:

        st.image("https://images.unsplash.com/photo-1615485737651-580c9159c89a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1481&q=80")

        btn7 = st.button("Fantasize and day-dream",key=26)
        
        if btn7:
            assign(q7,"Fantasize and day-dream")


    with col28:

        st.image("https://images.unsplash.com/photo-1656422046523-469409b2b4d0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn7 = st.button("Become rude",key=27)
        
        if btn7:
            assign(q7,"Become rude")

    st.write(f"You chose-{st.session_state[q7]}")





    q8 = "q8"
    if q8 not in st.session_state:
        st.session_state[q8] = ""


    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("8. What could stress you out-")

    
    col29, col30, col31, col32 = st.columns(4)
    with col29:

        st.image("https://images.unsplash.com/photo-1559916712-ae4427996e1d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")
        
        btn8 = st.button("Incomplete tasks",key=28)
        if btn8:
            assign(q8,"Incomplete tasks")


    with col30:

        st.image("https://images.unsplash.com/photo-1624835020719-deec76c86249?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")
        btn8 = st.button("Small talk",key=29)
        if btn8:
            assign(q8,"Small talk")


    with col31:

        st.image("https://images.unsplash.com/photo-1656031784125-6eb734c24beb?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")
        btn8 = st.button("Lying",key=30)
        
        if btn8:
            assign(q8,"Lying")


    with col32:

        st.image("https://images.unsplash.com/photo-1652448919151-c8be3cfb185b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn8 = st.button("Deadlines",key=31)
        
        if btn8:
            assign(q8,"Deadlines")

    st.write(f"You chose-{st.session_state[q8]}")




    q9 = "q9"
    if q9 not in st.session_state:
        st.session_state[q9] = ""


    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    header312("9. Which job you might prefer-")

    
    col29, col30, col31, col32 = st.columns(4)
    with col29:

        st.image("https://images.unsplash.com/photo-1571809839227-b2ac3d261257?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")
        
        btn9 = st.button("Administrator",key=32)
        if btn9:
            assign(q9,"Administrator")


    with col30:

        st.image("https://images.unsplash.com/photo-1627054886476-0cdee47fde3d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")
        btn9 = st.button("Criminologist",key=33)
        if btn9:
            assign(q9,"Criminologist")


    with col31:

        st.image("https://images.unsplash.com/photo-1626200419537-f07108a01aac?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1524&q=80")
        btn9 = st.button("Journalist",key=34)
        
        if btn9:
            assign(q9,"Journalist")


    with col32:

        st.image("https://images.unsplash.com/photo-1603096285763-ad9a983c6d0d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80")

        btn9 = st.button("Comedian",key=35)
        
        if btn9:
            assign(q9,"Comedian")

    st.write(f"You chose-{st.session_state[q9]}")



    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)

    submit_btn = st.button("Submit test")

    if submit_btn and st.session_state[q1]!="" and st.session_state[q2]!="" and st.session_state[q3]!="" and st.session_state[q4]!="" and st.session_state[q5]!="" and st.session_state[q6]!="" and st.session_state[q7]!="" and st.session_state[q8]!="" and st.session_state[q9]!="":


        gold = 0
        green = 0
        blue = 0
        orange = 0

        if st.session_state[q1]=="Responsibility":
            gold+=1

        elif st.session_state[q1]=="Objectivity":
            green+=1

        elif st.session_state[q1]=="Loyalty":
            blue+=1

        else:
            orange+=1


        if st.session_state[q2]=="Stable":
            gold+=1

        elif st.session_state[q2]=="Superior intellect":
            green+=1

        elif st.session_state[q2]=="Warm":
            blue+=1

        else:
            orange+=1



        if st.session_state[q3]=="Bossy":
            gold+=1

        elif st.session_state[q3]=="Emotionally controlled":
            green+=1

        elif st.session_state[q3]=="Hopelessly naïve":
            blue+=1

        else:
            orange+=1


        if st.session_state[q4]=="Irresponsibility":
            gold+=1

        elif st.session_state[q4]=="Routine":
            green+=1

        elif st.session_state[q4]=="Lying":
            blue+=1

        else:
            orange+=1



        if st.session_state[q5]=="Being obsessive":
            gold+=1

        elif st.session_state[q5]=="Blowing up when criticized":
            green+=1

        elif st.session_state[q5]=="Suppressing problems":
            blue+=1

        else:
            orange+=1



        if st.session_state[q6]=="Sincere appreciation is shown":
            gold+=1

        elif st.session_state[q6]=="The quality of your work is recognized":
            green+=1

        elif st.session_state[q6]=="You are praised with an energetic and enthusiastic manner":
            blue+=1

        else:
            orange+=1



        if st.session_state[q7]=="Complain":
            gold+=1

        elif st.session_state[q7]=="Become overly indecisive":
            green+=1

        elif st.session_state[q7]=="Fantasize and day-dream":
            blue+=1

        else:
            orange+=1



        if st.session_state[q8]=="Incomplete tasks":
            gold+=1

        elif st.session_state[q8]=="Small talk":
            green+=1

        elif st.session_state[q8]=="Lying":
            blue+=1

        else:
            orange+=1


        if st.session_state[q9]=="Administrator":
            gold+=1

        elif st.session_state[q9]=="Criminologist":
            green+=1

        elif st.session_state[q9]=="Journalist":
            blue+=1

        else:
            orange+=1




        choice = max(gold,green,blue,orange)

        if choice == gold:

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type color is-")
            header("Gold")
            header31("Caring")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)


            col1,col2 = st.columns(2)

            with col1:

                st.image("https://images.unsplash.com/photo-1517196084897-498e0abd7c2d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80")
            
            with col2:
                header4("You enjoy making detailed plans and paying attention to details. You feel secure in life because you are responsible and highly predictable. You rarely take unanticipated or unplanned actions. You respect tradition and history as well. You have a high moral standard and strongly adhere to the shared ideas of your family. Whether it's through your profession or by volunteering, you like finding different ways to live out these principles throughout your life. You like being relied upon to assist others.")

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            datab.insert_values(str(dt_string),str(uid),name,gender,option,"Gold")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            


            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Outgoing")
                header4("2. Trusting")
                header4("3. Popular")
                header4("4. High Energy")


            with col4:

                header312("Weaknesses")
                header4("1. Disorganized")
                header4("2. Poor listener")

            st.session_state[q1] = st.session_state[q2] = st.session_state[q3] = st.session_state[q4] = st.session_state[q5] = st.session_state[q6] = st.session_state[q7] = st.session_state[q8] = ""

            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)



        elif choice == green:

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type color is-")
            header("Green")
            header31("Creative")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)
            
            col1,col2 = st.columns(2)

            with col1:

                st.image("https://images.unsplash.com/photo-1598940603846-a1edd0ef2574?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80")
            
            with col2:
                header4("People frequently compliment you on your intelligence. You pride yourself on your work and have an innate urge to do things to the best of your ability. At work, you are the example for everyone else. You actually enjoy working. Even on the weekends, you attempt to cram as much as you can into each day because you can't bear the idea of squandering time. You have a lot of thinking power. You love discussing abstract, intellectual concepts with other people. You adore speculating about the possibilities of the future. You take the view that learning should never cease, and you appreciate picking up new knowledge just for fun.")

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            datab.insert_values(str(dt_string),str(uid),name,gender,option,"Green")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Generous")
                header4("2. Determined")
                header4("3. Strong-willed")
                header4("4. Compassionate")


            with col4:

                header312("Weaknesses")
                header4("1. Hard to please")
                header4("2. Can be moody")

            st.session_state[q1] = st.session_state[q2] = st.session_state[q3] = st.session_state[q4] = st.session_state[q5] = st.session_state[q6] = st.session_state[q7] = st.session_state[q8] = ""
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)



        elif choice == blue:

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type color is-")
            header("Blue")
            header31("Enthusiastic")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://images.unsplash.com/photo-1601436155198-2ebfea8117b0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80")
            
            with col2:
                header4("Generally speaking, you are tolerant, upbeat, and friendly. You strive to see the best in everyone and in every circumstance because you are a really sympathetic and caring person. You possess the ability to maintain composure and manage conflicts between people in stressful situations. Others are inspired by your good outlook. Instead of being the most outspoken or dynamic leader, you are a quiet leader who motivates people with your own dedication and consideration for others. You truly set the bar high.")


            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            datab.insert_values(str(dt_string),str(uid),name,gender,option,"Blue")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Sincere")
                header4("2. High Achiever")
                header4("3. Good Communicator")
                header4("4. Reliable")


            with col4:

                header312("Weaknesses")
                header4("1. Unforgiving")
                header4("2. Judgemental")

            st.session_state[q1] = st.session_state[q2] = st.session_state[q3] = st.session_state[q4] = st.session_state[q5] = st.session_state[q6] = st.session_state[q7] = st.session_state[q8] = ""
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)


        
        else:

            st.markdown("<br>",unsafe_allow_html=True)

            uid = uuid.uuid4()   
            header3(f"Your unique id to see the result again is- {uid}")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)

            header1("Your personality type color is-")
            header("Orange")
            header31("Practical")
            st.balloons()
            st.markdown("<br>",unsafe_allow_html=True)

            col1,col2 = st.columns(2)

            with col1:

                st.image("https://images.unsplash.com/photo-1519849968456-c4918b53e694?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80")
            
            with col2:
                header4("You're frequently characterised by others as charming, entertaining, and vivacious. You naturally attract people, and you don't waste any time making friends. You naturally exhibit extraversion and perform well in social settings. You are also really witty and charming. You are an excellent negotiator with a talent for persuading people to view things your way. Additionally, orange people have a lot of creativity and spontaneity. You surely don't hesitate to take chances. Similar to this, you frequently follow your heart rather than your mind, which might lead to difficulties.")


            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            datab.insert_values(str(dt_string),str(uid),name,gender,option,"Orange")
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            col3,col4 = st.columns(2)
 

            with col3:

                header312("Strengths")
                header4("1. Open-minded")
                header4("2. Optimistic")
                header4("3. Warm")
                header4("4. Competitive")


            with col4:

                header312("Weaknesses")
                header4("1. Impatient")
                header4("2. Insincere")

            st.session_state[q1] = st.session_state[q2] = st.session_state[q3] = st.session_state[q4] = st.session_state[q5] = st.session_state[q6] = st.session_state[q7] = st.session_state[q8] = ""
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown("<br>",unsafe_allow_html=True)
            html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="https://rinkuchhokar-mbti-home-7hdujp.streamlitapp.com/" target="_self" role="button">Play Again</a>
                    </div>
                </div>
                """
            st.markdown(html_code1,unsafe_allow_html=True)





else:
    st.error("All details are required!! ")

st.markdown("<style>.css-16nzq6b{font-size:22px;}</style>",unsafe_allow_html=True)
      

        
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# function to add background image

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

# set_bg_hack("bg.jpg")



