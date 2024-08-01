import streamlit as st
import base64
import sqlite3

def authenticate_user(username, password):
    conn = sqlite3.connect('users_ss.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users_ss WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()
    return user

with open('bgimg.jpg', "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

st.set_page_config(page_title="Symphony Smith", layout="wide")

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
    .stTitle {{
        color: white; 
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
    .login-links img {{
        width: 30px;
        height: 30px;
        vertical-align: middle;
    }}
    .login-links {{
        text-align: center;
        margin-bottom: 20px;
    }}
    .login-links a {{
        margin: 0 10px;
        color: blue;
        text-decoration: none;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="stApp">', unsafe_allow_html=True)
st.title("Login Page")

st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="login-links">
        <a href="https://accounts.google.com/signin" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Google_%22G%22_logo.svg/150px-Google_%22G%22_logo.svg.png" alt="Google"></a>
        <a href="https://github.com/login" target="_blank"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub"></a>
    </div>
    """,
    unsafe_allow_html=True
)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log In"):
    user = authenticate_user(username, password)
    if user:
        st.success("Login successful!")
    else:
        st.error("Invalid username or password")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
