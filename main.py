import streamlit as st
import re
from loading_profiles import get_profile
from deepseek_integration import get_response, get_scores

# this app is meant to rate people's linkendIn profiles
st.set_page_config(
    page_title="LinkedIn Profile Rating",
    page_icon=":wrench:",
    layout="wide",
)

st.title("LinkedIn Profile Review")
st.subheader("Get a rating for your LinkedIn profile")

def write_score(score, label):
    if score >= 7.5:
        st.success(f"{label}: {score}/10 :partying_face:")
    elif score >= 4:
        st.warning(f"{label}: {score}/10 :neutral_face:")
    else:
        st.error(f"{label}: {score}/10 :rotating_light:")

def handle_profile(profile_name):
    profile = get_profile(profile_name)

    if not profile:
        st.error("Profile not found or private :cry:")
        return
    scores = get_scores(get_response(profile))
    st.subheader("Profile Rating")
    write_score(scores['headline'], "Headline")
    write_score(scores['experience'], "Experience")
    write_score(scores['education'], "Education")
    write_score(scores['skills'], "Skills")
    write_score(scores['achievements'], "Achievements & Impact")
    write_score(scores['overall'], "Overall Rating")



# Intial form
with st.form(key="profile_form"):
    st.write("Please enter your LinkedIn username")
    username = st.text_input(
        "LinkedIn Username", placeholder="your-username"
    )
    submit_button = st.form_submit_button(label="Submit")

# form handling
if submit_button:
    st.success("Loading... (this may take a second :pray:)")
    if username:
        if re.fullmatch(r"^(?!.*LinkedIn).{3,100}$", username):
            handle_profile(username)

        else:
            st.error(
                "Invalid username."
            )
    else:
        st.error("Please enter a valid LinkedIn profile link.")


st.markdown(
    """
    This early version was developed by Jakob Danninger for Prof Ronald Loui's CSDS285
    Source code can be found [here](https://github.com/jdanninger/Jakobs-LinkedIn-App)
    """)
