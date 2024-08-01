import streamlit as st
import base64
import sqlite3

def create_user(username, email, password):
    conn = sqlite3.connect('users_ss.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
    conn.commit()
    conn.close()
    
with open('bgimg.jpg', "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

st.set_page_config(page_title="Symphony Smith", layout="centered")

st.markdown(
    f"""
    <style>
    .main {{
        background-image: url('data:image/jpeg;base64,{encoded_image}');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        color: white;
    }}
    body {{
        font-family: 'Times New Roman', Times, serif;
        color: #fff;
    }}
    h1 {{
        font-size: 48px;
        line-height: 1.2;
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
    .stTextInput > div > div > input {{
        color: black;
    }}
    .stButton > button {{
        background: none;
        border: 2px solid #ffd700;
        color: #ffd700;
        padding: 0.6em 0.6em;
        border-radius: 0.5em;
        cursor: pointer;
        transition: background-color 0.3s ease, color 0.3s ease;
    }}
    .stButton > button:hover {{
        background-color: rgba(255, 215, 0, 0.3);
        color: white;
    }}
    .stButton > button:active {{
        background-color: rgba(255, 215, 0, 0.5);
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="container">', unsafe_allow_html=True)
st.title("Sign Up for Symphony Smith")

st.markdown('<p>Create your account to start creating music with AI.</p>', unsafe_allow_html=True)

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Sign Up"):
    if password == confirm_password:
        try:
            create_user(username, email, password)
            st.success("Sign up successful!")
        except sqlite3.IntegrityError:
            st.error("Username already exists.")
    else:
        st.error("Passwords do not match.")

st.markdown('</div>', unsafe_allow_html=True)
