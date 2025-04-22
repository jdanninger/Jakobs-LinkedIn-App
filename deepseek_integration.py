from openai import OpenAI
import streamlit as st
from loading_profiles import get_profile


def get_response(profile):
    api_key = st.secrets["api_key"]
    prompt = st.secrets["prompt"]

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    content = prompt + "\n" + str(profile)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are helping a user with their LinkedIn profile."},
            {"role": "user", "content": content},
        ],
        stream=False
    )
    print (response.choices[0].message.content)
    return response.choices[0].message.content

# get_response(profile)



def get_scores(output_text):
    returnMe = {}
    #Headline
    headline = output_text.split("Headline")[1]
    headline = headline.split("/10")[0]
    headline = headline.split("Score: ")[1]
    returnMe['headline'] = float(headline.strip())

    #Experience
    experience = output_text.split("Experience")[1]
    experience = experience.split("/10")[0]
    experience = experience.split("Score: ")[1]
    returnMe['experience'] = float(experience.strip())

    #Education
    education = output_text.split("Education")[1]
    education = education.split("/10")[0]
    education = education.split("Score: ")[1]
    returnMe['education'] = float(education.strip())

    #Skills
    skills = output_text.split("Skills")[1]
    skills = skills.split("/10")[0]
    skills = skills.split("Score: ")[1]
    returnMe['skills'] = float(skills.strip())

    #Achievements and Impact
    achievements = output_text.split("Achievements & Impact")[1]
    achievements = achievements.split("/10")[0]
    achievements = achievements.split("Score: ")[1]
    returnMe['achievements'] = float(achievements.strip())

    #Overall Rating
    overall = output_text.split("Overall Rating:")[1]
    overall = overall.split("/10")[0]
    returnMe['overall'] = float(overall.strip())

    return returnMe

