import streamlit as st

st.set_page_config(page_title="Symphony Smith", page_icon=":guitar:", layout="wide")

st.markdown(
    """
    <style>
    .main {
        background-color: orange;
        font: sans-serif
    }
    .stTextInput > div > div > input {
        color: black;  
    }
    .stTitle {
        color: white; 
    }
    .stButton > button {
        color: black;  
    }
    .login-links img {
        width: 30px;
        height: 30px;
        vertical-align: middle;
    }
    .login-links {
        text-align: center;
        margin-bottom: 20px;
    }
    .login-links a {
        margin: 0 10px;
        color: blue;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Login Page")

st.markdown('<div class="login-box">', unsafe_allow_html=True)

# Links for Google and GitHub login
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

if st.button("Login"):
    if username == "admin" and password == "password":
        st.success("Login successful!")
    else:
        st.error("Invalid username or password")

st.markdown('</div>', unsafe_allow_html=True)
