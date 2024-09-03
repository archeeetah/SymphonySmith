import streamlit as st
import base64

with open('bgimg.jpg', "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

st.set_page_config(page_title="Symphony Smith", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "WelcomePage"

def welcome_page():
    st.markdown(f"""
        <style>
            .main {{
                background-image: url('data:image/jpeg;base64,{encoded_image}');
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
                background-color: #ff0000;
                color: black;
                border-radius: 10px;
                text-align: center; 
                line-height: 100vh;
            }}
            h1 {{
                font-size: 64px;
                line-height: 1.2;
                color: #ffd700;
                margin: 20px 0;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            }}
            h2 {{
                font-size: 36px;
                color: #ffd700;
                margin: 20px 0;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            }}
            p {{
                font-size: 24px;
                color: #ffd700;
                margin: 20px 0;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
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

    go_button = st.button("Go Ahead", help='Click to start')
    if go_button:
        st.session_state.page = "MainPage"

def main_page():
    st.markdown(f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded_image}");
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
            .stAudio {{
                background-color: rgba(0, 0, 0, 0.6);
                padding: 10px;
                border-radius: 10px;
            }}
            h1 {{
                color: #FFD700; 
            }}
            p {{
                color: #FFD700; 
            }}
        </style>
    """, unsafe_allow_html=True)

    st.title("Symphony Smith - AI-Powered Song Generator")

    user_prompt = st.text_area("Enter your music prompt below:", height=150)

    generate_button = st.button("Generate Song", help="Click to generate a song based on your prompt")

    song_placeholder = st.empty()

    if generate_button:
        song_file_path = "path_to_generated_song.mp3"

        song_placeholder.markdown(
            f"""
            <audio controls class="stAudio">
                <source src="{song_file_path}" type="audio/mpeg">
                Your browser does not support the audio element.
            </audio>
            """,
            unsafe_allow_html=True,
        )
    
    back_button = st.button("Back", help="Click to go back")
    if back_button:
        st.session_state.page = "WelcomePage"

if st.session_state.page == "WelcomePage":
    welcome_page()
elif st.session_state.page == "MainPage":
    main_page()
