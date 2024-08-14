# app.py
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Symphony Smith",
    page_icon="🎵",
    layout="wide",
)

# Define the landing page
def show_landing_page():
    st.image("C:/Users/Madhav/OneDrive/Documents/Attachments/Desktop/ssbg.jpg", use_column_width=True)
    st.markdown(
        """
        <style>
        .orange-text {
            color: orange;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }
        </style>
        """
    )
    st.markdown('<p class="orange-text">Welcome to Symphony Smith!</p>', unsafe_allow_html=True)
    if st.button("Flamy Start"):
        st.experimental_rerun()

# Define the ML model page
def show_ml_page():
    st.title("Symphony Smith ML Model")
    prompt = st.text_input("Enter a prompt:")
    # Implement your ML model here (e.g., using audiocraft library)
    # Display the results

# Main app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ["Home", "ML Model"])

    if page == "Home":
        show_landing_page()
    elif page == "ML Model":
        show_ml_page()

if __name__ == "__main__":
    main()
