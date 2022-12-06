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
          <source src="https://cdn.dribbble.com/users/707385/screenshots/14377516/media/9a68bb26b982a38364df6804ec149a73.mp4")>
          Your browser does not support HTML5 video.
        </video>


        """

st.markdown(video_html, unsafe_allow_html=True)



def header(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:60px;border-radius:2%;font-weight:bolder;font-family:lato;">{url}</p>', unsafe_allow_html=True)



header("User Page")

# image = Image.open('home.jpg')

# st.image(image, caption='Stock Price')


def header1(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:30px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

header1("Enter your unique id")


def header3(url):
    st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


def text(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:16px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header4(url):
 st.markdown(f'<p style=color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


def header31(url):
 st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:25px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header312(url):
 st.markdown(f'<p style=color:#ffffff;font-size:25px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


# Login Page-

unique_id = st.text_input("UID")


# user-details

user_details = db.fetch_details()

st.markdown("<br>",unsafe_allow_html=True)


found = 0


res = ""

for i in range(len(user_details)):

    if user_details[i]["key"]==unique_id:
        found = 1
        res = user_details[i]["Personality Type"]
        break

if found > 0:


    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)

    if res == "ESTJ":

        header1("Your personality type-")
        header(res)
        header1("Extraverted Sensing Thinking Judging")
        header31("Executive")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://assets-metrostyle.abs-cbn.com/prod/metrostyle/attachments/0103cade-f05c-498c-b7de-954c77524279_fullsizephoto968194.jpg")
        
        with col2:
            header4("ESTJs are hardworking traditionalists, eager to take charge in organizing projects and people. Orderly, rule-abiding, and conscientious, ESTJs like to get things done, and tend to go about projects in a systematic, methodical way.")


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
        

        



    elif res == "ENTJ":

        header1("Your personality type-")
        header(res)
        header1("Extraverted Intuitive Thinking Judging")
        header31("Commander")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://i.pinimg.com/736x/0c/f4/ba/0cf4ba53a0a1ebcf7ab5468616f83b57.jpg")
        
        with col2:
            header4("ENTJs are strategic leaders, motivated to organize change. They are quick to see inefficiency and conceptualize new solutions, and enjoy developing long-range plans to accomplish their vision. They excel at logical reasoning and are usually articulate and quick-witted.")
        

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
        
        



    elif res == "ESFJ":

        header1("Your personality type-")
        header(res)
        header1("Extraverted Sensing Feeling Judging")
        header31("Caregiver")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://pbs.twimg.com/media/EejEZ0cUcAAhBHq.jpg")
        
        with col2:
            header4("ESFJ, also known as 'The Caregiver' or 'The Consul,' is one of the 16 personality types identified by the Myers-Briggs Type Indicator. People with an ESFJ personality type tend to be outgoing, loyal, organized, and tender-hearted. ESFJs gain energy from interacting with other people.")
        

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

        



        
    elif res == "ENFJ":

        header1("Your personality type-")
        header(res)
        header1("Extraverted Intuitive Feeling Judging")
        header31("Giver")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://media.timeout.com/images/105875926/750/422/image.jpg")
        
        with col2:
            header4("ENFJ indicates a person who is energized by time spent with others (Extraverted), who focuses on ideas and concepts rather than facts and details (iNtuitive), who makes decisions based on feelings and values (Feeling) and who prefers to be planned and organized rather than spontaneous and flexible (Judging).")
        

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

        header1("Your personality type-")
        header(res)
        header1("Introverted Sensing Thinking Judging")
        header31("Logistician")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://3.bp.blogspot.com/-4V0TX-nahtc/VJ7WbxtIwdI/AAAAAAAABrw/eyzcUbxYMFI/s1600/10609472_1497427670512774_7223601241914768748_n.jpg")
        
        with col2:
            header4("ISTJ indicates a person who is energized by time spent alone (Introverted), who focuses on facts and details rather than ideas and concepts (Sensing), who makes decisions based on logic and reason (Thinking) and who prefers to be planned and organized rather than spontaneous and flexible (Judging).")
        
 
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
        
        




    elif res == "ISFJ":

        header1("Your personality type-")
        header(res)
        header1("Introverted Sensing Feeling Judging")
        header31("Nurturer")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://www.kdramalove.com/Just-Between-Lovers_MomDaughter.jpg")
        
        with col2:
            header4(" ISFJ stands for introverted, sensing, feeling, judging. This personality type is given the nickname 'The Protector' or 'The Defender,' and for good reason. 2 People who have ISFJ personalities are known for being warm-hearted, responsible, and reserved. The ENTP personality type is the opposite.")
        

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
                <a class="btn btn-success" href="http://localhost:8501/" target="_self" role="button">Play Again</a>
            </div>
            """
        st.markdown(html_code1,unsafe_allow_html=True)
        




    elif res == "INTJ":

        header1("Your personality type-")
        header(res)
        header1("Introverted Intuitive Thinking Judging")
        header31("Scientist")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://media.starbiz.net/2020/08/upcoming-drama-alice-stills-kim-hee-sun-intelligent-scientist.jpg")
        
        with col2:
            header4("People with an INTJ personality type tend to be confident, analytical, and ambitious in their behavior. They love to pursue knowledge and tend to be very logically minded. They are independent thinkers focused on solving the world's problems.")
        

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
        




    elif res == "INFJ":

        header1("Your personality type-")
        header(res)
        header1("Introverted Intuitive Feeling Judging")
        header31("Advocate")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://dramaswithasideofkimchi.com/wp-content/uploads/2018/06/img_5314.jpg")
        
        with col2:
            header4("Scoring as an INFJ means that your personality type is best described as Introverted, Intuitive, Feeling, and Judging. Sometimes referred to as the 'Advocate' or the 'Idealist,' people with this personality type often feel misunderstood.")
        

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
        




    elif res == "ESTP":

        header1("Your personality type-")
        header(res)
        header1("Extraverted Sensing Thinking Perceiving")
        header31("Entrepreneur")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://i.pinimg.com/originals/55/d6/d3/55d6d3d3425f9572162db1ccd2d5d3d7.jpg")
        
        with col2:
            header4("ESTP indicates a person who is energized by time spent with others (Extraverted), who focuses on facts and details rather than ideas and concepts (Sensing), who makes decisions based on logic and reason (Thinking) and who prefers to be spontaneous and flexible rather than planned and organized (Perceiving).")
        
   
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
        
        




    elif res == "ESFP":

        header1("Your personality type-")
        header(res)
        header1("Extraverted Sensing Feeling Perceiving")
        header31("Entertainer")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://pbs.twimg.com/media/ELTUTE-U4AYWoWB.jpg")
        
        with col2:
            header4("People with ESFP personality types are often described as spontaneous, resourceful, and outgoing. They love being the center of attention and are often described as entertainers or “class clowns.” ESFP is the opposite of the INTJ personality type.")
        


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
        
        



    elif res == "ENTP":

        header1("Your personality type-")
        header(res)
        header1("Extraverted Intuitive Thinking Perceiving")
        header31("Debater")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://4.bp.blogspot.com/-SvcwyAQitWE/Wra30rGidmI/AAAAAAAACwM/R8uxpnB_CuQ8RJZVZahhACbXPa_yzHyjgCLcBGAs/s1600/Go%2BHye%2BRan%2BMisty.png")
        
        with col2:
            header4("A Debater (ENTP) is a person with the Extraverted, Intuitive, Thinking, and Prospecting personality traits. They tend to be bold and creative, deconstructing and rebuilding ideas with great mental agility. They pursue their goals vigorously despite any resistance they might encounter.")

    
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
        
        




    elif res == "ENFP":

        header1("Your personality type-")
        header(res)
        header1("Extraverted Intuitive Feeling Perceiving")
        header31("Inspirer")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://1739752386.rsc.cdn77.org/data/images/full/247919/melancholia.jpg")
        
        with col2:
            header4("ENFPs are people-centered creators with a focus on possibilities and a contagious enthusiasm for new ideas, people and activities. Energetic, warm, and passionate, ENFPs love to help other people explore their creative potential.")

     
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
        




    elif res == "ISTP":

        header1("Your personality type-")
        header(res)
        header1("Introverted Sensing Thinking Perceiving")
        header31("Virtuoso")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://kdramadiary.com/wp-content/uploads/2021/04/seo-in-guk-pipeline-kdramadiary.jpg")
        
        with col2:
            header4("A Virtuoso (ISTP) is someone with the Introverted, Observant, Thinking, and Prospecting personality traits. They tend to have an individualistic mindset, pursuing goals without needing much external connection. They engage in life with inquisitiveness and personal skill, varying their approach as needed.")
        

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
        
        




    elif res == "ISFP":

        header1("Your personality type-")
        header(res)
        header1("Introverted Sensing Feeling Perceiving")
        header31("Artist")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://media.starbiz.net/2020/10/16-times-iu-had-us-feeling-super-soft-in-the-fluffiest-over-sized-sweaters-3.jpg")
        
        with col2:
            header4("ISFPs are gentle caretakers who live in the present moment and enjoy their surroundings with cheerful, low-key enthusiasm. They are flexible and spontaneous, and like to go with the flow to enjoy what life has to offer. ISFPs are quiet and unassuming, and may be hard to get to know.")
        

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
        
        




    elif res == "INTP":

        header1("Your personality type-")
        header(res)
        header1("Introverted Intuitive Thinking Perceiving")
        header31("Thinker")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://kdramadiary.com/wp-content/uploads/2020/09/hyun-bin-summer-ad-kdramadiary-f.jpg")
        
        with col2:
            header4(" People who score as INTP are often described as quiet and analytical. They enjoy spending time alone, thinking about how things work and coming up with solutions to problems. INTPs have a rich inner world and would rather focus their attention on their internal thoughts rather than the external world.")

    
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
        
        



    elif res=="INFP":

        header1("Your personality type-")
        header(res)
        header1("Introverted Intuitive Feeling Perceiving")
        header31("Idealist")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://m.media-amazon.com/images/M/MV5BMmUwMTIxMjctZDk1OS00Y2M4LTlkMzAtNjNlNmM0YzU1NGIyXkEyXkFqcGdeQXVyODA4ODIwNDM@._V1_.jpg")
        
        with col2:
            header4("The INFP personality type is often described as an 'idealist' or 'mediator' personality. People with this kind of personality tend to be introverted, idealistic, creative, and driven by high values. INFPs also have strong interests in making the world a better place.")
        

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
        



    elif res == "Lion":

        header1("Your personality type animal-")
        header("Lion")
        header31("Strong")

        st.markdown("<br>",unsafe_allow_html=True)


        col1,col2 = st.columns(2)

        with col1:

            st.image("https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1386&q=80")
        
        with col2:
            header4("Lions are leaders. They are usually the bosses at work...or believe they are! They are decisive, bottom-line people who observe rather than watch or listen. They enjoy solving problems. They are typically individualists who seek out new adventures and opportunities.")

   
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

    
        



    elif res == "Otter":

        header1("Your personality type animal-")
        header("Otter")
        header31("Smart")

        st.markdown("<br>",unsafe_allow_html=True)
        
        col1,col2 = st.columns(2)

        with col1:

            st.image("https://images.unsplash.com/photo-1595703013566-db085ae93c04?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1376&q=80")
        
        with col2:
            header4("Otters are exuberant, fun-seeking individuals who enjoy talking! They are excellent motivators and require an environment in which they can speak freely and vote on major decisions. Because of their outgoing personalities, otters make excellent networkers—they usually know a lot of people who know a lot of people.")

        
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

        
        



    elif res == "Loyal":

        header1("Your personality type animal-")
        header("Golden Retriever")
        header31("Loyal")

        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://images.unsplash.com/photo-1633722715463-d30f4f325e24?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80")
        
        with col2:
            header4("These people can be described in one word: LOYAL. They are so devoted that they can endure the most emotional pain and punishment in a relationship and still remain committed. They are excellent listeners, empathetic, and encouraging.")

       
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

        
        


    
    elif res == "Beaver":

        header1("Your personality type animal-")
        header("Beaver")
        header31("Practical")
        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://images.unsplash.com/photo-1544878221-efc436f31748?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80")
        
        with col2:
            header4("Beavers have a strong desire to do things correctly and according to the rules. They are, in fact, the type of people who read instruction manuals. They excel at quality control in the office and will provide quality control in any situation or field that requires accuracy, such as accounting, engineering, and so on.")


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

        
        



    elif res == "Gold":

        header1("Your personality type color is-")
        header("Gold")
        header31("Caring")
        st.markdown("<br>",unsafe_allow_html=True)


        col1,col2 = st.columns(2)

        with col1:

            st.image("https://images.unsplash.com/photo-1517196084897-498e0abd7c2d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80")
        
        with col2:
            header4("You enjoy making detailed plans and paying attention to details. You feel secure in life because you are responsible and highly predictable. You rarely take unanticipated or unplanned actions. You respect tradition and history as well. You have a high moral standard and strongly adhere to the shared ideas of your family. Whether it's through your profession or by volunteering, you like finding different ways to live out these principles throughout your life. You like being relied upon to assist others.")


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

        
        



    elif res == "Green":

        header1("Your personality type color is-")
        header("Green")
        header31("Creative")
        st.markdown("<br>",unsafe_allow_html=True)
        
        col1,col2 = st.columns(2)

        with col1:

            st.image("https://images.unsplash.com/photo-1598940603846-a1edd0ef2574?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80")
        
        with col2:
            header4("People frequently compliment you on your intelligence. You pride yourself on your work and have an innate urge to do things to the best of your ability. At work, you are the example for everyone else. You actually enjoy working. Even on the weekends, you attempt to cram as much as you can into each day because you can't bear the idea of squandering time. You have a lot of thinking power. You love discussing abstract, intellectual concepts with other people. You adore speculating about the possibilities of the future. You take the view that learning should never cease, and you appreciate picking up new knowledge just for fun.")

    
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

        
        



    elif res == "Blue":

        header1("Your personality type color is-")
        header("Blue")
        header31("Enthusiastic")
        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://images.unsplash.com/photo-1601436155198-2ebfea8117b0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80")
        
        with col2:
            header4("Generally speaking, you are tolerant, upbeat, and friendly. You strive to see the best in everyone and in every circumstance because you are a really sympathetic and caring person. You possess the ability to maintain composure and manage conflicts between people in stressful situations. Others are inspired by your good outlook. Instead of being the most outspoken or dynamic leader, you are a quiet leader who motivates people with your own dedication and consideration for others. You truly set the bar high.")

        
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

        
        


    
    else:

        header1("Your personality type color is-")
        header("Orange")
        header31("Practical")
        st.markdown("<br>",unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:

            st.image("https://images.unsplash.com/photo-1519849968456-c4918b53e694?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80")
        
        with col2:
            header4("You're frequently characterised by others as charming, entertaining, and vivacious. You naturally attract people, and you don't waste any time making friends. You naturally exhibit extraversion and perform well in social settings. You are also really witty and charming. You are an excellent negotiator with a talent for persuading people to view things your way. Additionally, orange people have a lot of creativity and spontaneity. You surely don't hesitate to take chances. Similar to this, you frequently follow your heart rather than your mind, which might lead to difficulties.")


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

        
        


    found = 0


elif unique_id!="":      

    st.error("UID not found!!")


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




st.markdown("<style>.css-16nzq6b{font-size:22px;}</style>",unsafe_allow_html=True)
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


