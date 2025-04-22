import streamlit as st
import re

# this app is meant to rate people's linkendIn profiles
st.set_page_config(
    page_title="LinkedIn Profile Rating",
    page_icon=":wrench:",
    layout="wide",
)

st.title("LinkedIn Profile Review")
st.subheader("Get a rating for your LinkedIn profile")


# Intial form
with st.form(key="profile_form"):
    st.write("Please enter your LinkedIn profile link:")
    username = st.text_input(
        "LinkedIn Username", placeholder="your-username"
    )
    submit_button = st.form_submit_button(label="Submit")

# form handling
if submit_button:
    if username:
        if re.fullmatch(r"^(?!.*LinkedIn).{3,100}$", username):
            rating = 4.5  # Simulated rating
            st.write(f"Your LinkedIn profile rating is: {rating}/5")
        else:
            st.error(
                "Invalid username."
            )
    else:
        st.error("Please enter a valid LinkedIn profile link.")





st.markdown(
    """
    This early version was devloped by Jakob Danninger for Prof Ronal Loui's CSDS285
    Source code can be found [here](https://github.com/jdanninger/Jakobs-LinkedIn-App)
    """)
