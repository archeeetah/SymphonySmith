import streamlit as st



primary_color = "#FFA07A"  
background_color = "#000000"  
text_color = "#FFFFFF"  

font = "sans serif"


st.set_page_config(page_title="Symphony Smith", page_icon=":guitar:", layout="wide")


st.markdown("""
<style>
   .main {
        background-image: url("https://tse2.mm.bing.net/th?id=OIP.KrazIXoG0JkawYlanbZlugHaEK&pid=Api&P=0&h=180");
        background-size: cover;
        background-position: center;
    }
</style>
""", unsafe_allow_html=True)



st.markdown("""
<p style="font-size: 100px; font-weight: bold; color: """ + text_color + """ ; text-align: center;">
  <span style="color: #000000">Symphony</span> <span style="color: """ + text_color + """ ">Smith</span>
</p>
""", unsafe_allow_html=True)


states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
selectbox_label = "Explore music of 29 states of India"
selected_state = st.selectbox(selectbox_label, states, index=0)


genres = ["Classical", "Folk", "Rock", "Pop", "Hip-Hop", "Electronic", "Jazz", "Blues", "Country", "R&B", "Metal", "Indie", "Fusion"]

selectbox_label_genres = "Discover Your Favorite Genre"
selected_genre = st.selectbox(selectbox_label_genres, genres, index=0)



time_button = st.selectbox("Duration of Music",options=['1','2','3'])


st.markdown("""
<style>
    div.stButton > selectbox:first-child {
        background-color: """ + primary_color + """;
        color: """ + text_color + """;
        font-size: 20px;
        height: 3em;
        width: 30em;
        border-radius: 10px 10px 10px 10px;
    } 
  .css-2trqyj:focus:not(:active) {
        border-color: #ffffff;
        box-shadow: none;
        color: #ffffff;
        background-color: #0066cc;
    }
  .css-2trqyj:focus:active {
        background-color: #0066cc;
        border-color: #ffffff;
        box-shadow: none;
        color: #ffffff;
    }
   .selectbox {
        background-color: """ + primary_color + """;
        color: """ + text_color + """;
        font-size: 18px;
        border-radius: 10px 10px 10px 10px;
        padding: 10px;
    }
  .selectbox option {
        background-color: """ + background_color + """;
        color: """ + text_color + """;
    }
  .selectbox option:hover {
        background-color: """ + primary_color + """;
        color: """ + text_color + """;
    }
</style>""", unsafe_allow_html=True)


st.markdown("""
<p style="font-size: 18px; color: #FFFFFF; text-align: center;">
    "Music is the divine way to tell beautiful, poetic things to the heart." - Pablo Casals
</p>
""", unsafe_allow_html=True)