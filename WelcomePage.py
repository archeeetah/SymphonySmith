import streamlit as st

st.set_page_config(page_title="Symphony Smith", layout="centered")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap');
        .main {
            background-color: orange;
        }
        body {
            font-family: 'Poppins', sans-serif;
            color: #000;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
            padding: 20px;
        }
        h1 {
            font-size: 64px;
            line-height: 1.2;
            color: #eb6b23;
            margin: 20px 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        h2 {
            font-size: 36px;
            color: #eb6b23;
            margin: 20px 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        .welcome-text {
            font-size: 24px;
            color: #fff;
            margin: 20px 0;
        }
        .custom-button {
            font-size: 1.4em;
            padding: 0.6em 0.8em;
            border-radius: 0.5em;
            border: none;
            background-color: #eb6b23; 
            color: #fff; 
            cursor: pointer;
            box-shadow: 2px 2px 3px #000000b4;
            transition: background-color 0.3s ease, box-shadow 0.3s ease, color 0.3s ease;
            display: inline-block;
            margin: 20px;
            text-decoration: none;
        }
        .custom-button:hover {
            background-color: #cf5c1d;
            color: #fff;
            box-shadow: 2px 2px 8px #000000b4; 
        }
        .custom-button:active {
            box-shadow: none;
            transform: translateY(1px);
        }
        .section {
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 60px 20px;
            box-sizing: border-box;
            flex-direction: column;
        }
        .button-container {
            display: flex;
            justify-content: center;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

html_content = """
<div class="section">
    <div class="container">
        <h1>Welcome to Symphony Smith</h1>
        <h2>Create Your Own Music with AI</h2>
        <p class="welcome-text">Unleash your creativity and generate unique music effortlessly with our AI-powered music generator.</p>
        <div class="button-container">
            <a href="#" class="custom-button">Get Started</a>
        </div>
    </div>
</div>
"""

st.markdown(html_content, unsafe_allow_html=True)
