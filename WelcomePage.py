import streamlit as st
import base64

with open('bgimg.jpg', "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

st.set_page_config(page_title="Symphony Smith", layout="wide")

st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap');
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
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
            padding: 20px;
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
        .custom-button {{
            font-size: 1.4em;
            padding: 0.6em 0.8em;
            border-radius: 0.5em;
            border: 2px solid #ffd700; 
            background-color: transparent;
            color: #ffd700; 
            cursor: pointer;
            box-shadow: 2px 2px 3px #000000b4;
            transition: background-color 0.3s ease, box-shadow 0.3s ease, color 0.3s ease;
            display: inline-block;
            margin: 20px;
            text-decoration: none;
        }}
        .custom-button:hover {{
            background-color: rgba(255, 215, 0, 0.2);
            color: #ffd700;
            box-shadow: 2px 2px 8px #000000b4; 
        }}
        .custom-button:active {{
            box-shadow: none;
            transform: translateY(1px);
        }}
        .section {{
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 60px 20px;
            box-sizing: border-box;
            flex-direction: column;
        }}
        .button-container {{
            display: flex;
            justify-content: center;
            width: 100%;
        }}
    </style>
""", unsafe_allow_html=True)

html_content = """
<div class="section">
    <div class="container">
        <h1>Welcome to Symphony Smith</h1>
        <h2>Create Your Own Music with AI</h2>
        <p>Unleash your creativity and generate unique music effortlessly with our AI-powered music generator.</p>
        <div class="button-container">
            <a href="/SignupPage.py" class="custom-button">Sign Up</a>
            <a href="/LoginPage.py" class="custom-button">Log In</a>
        </div>
    </div>
</div>
"""

st.markdown(html_content, unsafe_allow_html=True)