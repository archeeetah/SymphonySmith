import streamlit as st
import base64

with open('bgimg.jpg', "rb") as image_file:
    encoded_image_1 = base64.b64encode(image_file.read()).decode()
    
with open('bgimg2.jpg', "rb") as image_file:
    encoded_image_2 = base64.b64encode(image_file.read()).decode()

# Set page configuration
st.set_page_config(page_title="Symphony Smith", layout="wide")

# Session state to manage pages
if "page" not in st.session_state:
    st.session_state.page = "WelcomePage"

# Welcome page function
def welcome_page():
    st.markdown(f"""
        <style>
            .main {{
                background-image: url('data:image/jpeg;base64,{encoded_image_1}');
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                color: white;
            }}
            body {{
                color: #fff;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                text-align: center;
                padding: 20px;
            }}
            .stButton > button {{
                background-color: #ffd700;
                color: black;
                border-radius: 10px;
                padding: 10px 20px;
            }}
            .stButton > button:hover {{
                background-color: rgba(255, 215, 0, 0.8);
                color: white;
            }}
            h1 {{
                font-size: 64px;
                line-height: 1.2;
                color: #fff;
                margin: 20px 0;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            }}
            h2 {{
                font-size: 36px;
                color: #fff;
                margin: 20px 0;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            }}
            p {{
                font-size: 24px;
                color: #fff;
                margin: 20px 0;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            }}
            .button-container {{
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
        <div class="container">
            <h1>Welcome to Symphony Smith</h1>
            <h2>Create Your Own Music with AI</h2>
            <p>Unleash your creativity and generate unique music effortlessly with our AI-powered music generator.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 1, 1]) 

    with col1:
        pass
    with col2:
        pass
    with col3:
        pass
    with col4:
        go_button = st.button("Go Ahead", help='Click to start')
    with col5:
        pass
    with col6:
        pass
    with col7:
        pass
    
    if go_button:
        st.session_state.page = "MainPage"

# Main page function
def main_page():
    st.markdown(f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded_image_2}");
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                color: #FFD700; 
            }}
            .stTextInput > div > div > textarea {{
                background-color: rgba(255, 255, 255, 0.8);
                color: black; 
                border-radius: 10px;
            }}
            .stButton > button {{
                background-color: #ffd700;
                color: black;
                border-radius: 10px;
                padding: 10px 20px;
            }}
            .stButton > button:hover {{
                background-color: rgba(255, 215, 0, 0.8);
                color: white;
            }}
            h1 {{
                color: #fff; 
            }}
        </style>
    """, unsafe_allow_html=True)

    st.title("Symphony Smith - AI-Powered Song Generator")

    user_prompt = st.text_area("", height=150)

    generate_button = st.button("Generate Song", help="Click to generate a song based on your prompt")
    back_button = st.button("Back", help="Click to go back")

    if generate_button:
        st.session_state.page = "GeneratedMusicPage"
    elif back_button:
        st.session_state.page = "WelcomePage"

# Generated music page with Streamlit PLAY, PAUSE, STOP, and Back buttons
def generated_music_page():
    st.markdown(f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded_image_2}");
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                color: #FFD700; 
            }}
            h1 {{
                color: #fff;
                text-shadow: 4px 4px 10px black;
                margin-top: 100px;
                font-size: 50px;
                text-align: center;
            }}
            .center {{
                display: flex;
                justify-content: center;
            }}
            .stButton > button {{
                background-color: #ffd700;
                color: black;
                border-radius: 10px;
                padding: 10px 20px;
                margin: 0 10px; /* Add space between buttons */
            }}
            .stButton > button:hover {{
                background-color: rgba(255, 215, 0, 0.8);
                color: white;
            }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>Here's Your Generated Music</h1>", unsafe_allow_html=True)

    # Columns for buttons
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1]) 

    with col1:
        play = st.button('PLAY', help="Click to listen to the music")
    with col2:
        pause = st.button('PAUSE', help="Click to temporarily stop the music")
    with col3:
        stop = st.button('STOP', help="Click to permanently stop the music")
    with col4:
        back_button = st.button('BACK', help="Click to go back")
    with col5:
        close_button = st.button('CLOSE', help="Click to close")

    # Inject JavaScript to control the audio based on button clicks
    st.markdown("""
        <audio id="audioPlayer" controls style="display:none;">
            <source src="path_to_your_audio_file.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        <script>
            var audio = document.getElementById('audioPlayer');
        </script>
    """, unsafe_allow_html=True)

    # Play button
    if play:
        st.markdown("""
            <script>
                var audio = document.getElementById('audioPlayer');
                audio.play();
                audio.style.display = "block";  // Make the audio visible when playing
            </script>
        """, unsafe_allow_html=True)

    # Pause button
    if pause:
        st.markdown("""
            <script>
                var audio = document.getElementById('audioPlayer');
                audio.pause();
            </script>
        """, unsafe_allow_html=True)

    # Stop button (stop = pause + reset currentTime to 0)
    if stop:
        st.markdown("""
            <script>
                var audio = document.getElementById('audioPlayer');
                audio.pause();
                audio.currentTime = 0;
            </script>
        """, unsafe_allow_html=True)

    # Navigation buttons
    if back_button:
        st.session_state.page = "MainPage"
    
    if close_button:
        st.session_state.page = "ThankYouPage"
        st.experimental_rerun()

# Thank you page function
def thank_you_page():
    st.markdown(f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded_image_1}");
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                color: #FFD700; 
            }}
            h1 {{
                color: #fff;
                text-align: center;
                margin-top: 100px;
                font-size: 50px;
                text-shadow: 4px 4px 10px black;
            }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>Thank You for Choosing Us!</h1>", unsafe_allow_html=True)

# Page navigation logic
if st.session_state.page == "WelcomePage":
    welcome_page()
elif st.session_state.page == "MainPage":
    main_page()
elif st.session_state.page == "GeneratedMusicPage":
    generated_music_page()
elif st.session_state.page == "ThankYouPage":
    thank_you_page()
