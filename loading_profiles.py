from linkedin_api import Linkedin
import streamlit as st


def get_profile(profile_id):
    email = st.secrets["email"]
    password = st.secrets["pw"]

    api = Linkedin(email, password)
    returnMe = {}
    try:
        profile = api.get_profile(profile_id)
        if not profile:
            return None
        returnMe['headline'] = profile.get('headline')

        # cleaning extra data out of expereince
        exerpience = profile.get('experience')
        if exerpience:
            for exp in exerpience:
                exp.pop('entityUrn', None)
                exp.pop('geoLocationName', None)
                exp.pop('geoUrn', None)
                exp.pop('region', None)
                exp.pop('companyUrn', None)
                exp.pop('companyLogoUrl', None)
        returnMe['experience'] = exerpience

        education = profile.get('education')
        if education:
            for edu in education:
                keys_to_keep = {'degreeName', 'schoolName', 'fieldOfStudy'}
                keys_to_remove = set(edu.keys()) - keys_to_keep
                for key in keys_to_remove:
                    edu.pop(key, None)
        returnMe['education'] = education

        skills = profile.get('skills')
        if skills:
            for skill in skills:
                skill.pop('entityUrn', None)
                skill.pop('proficiency', None)
                skill.pop('endorsements', None)
        returnMe['skills'] = skills

        certs = profile.get('certifications')
        if certs:
            for cert in certs:
                keys_to_keep = {'authority', 'name'}
                keys_to_remove = set(cert.keys()) - keys_to_keep
                for key in keys_to_remove:
                    cert.pop(key, None)
        returnMe['certifications'] = certs
        return returnMe
    except Exception as e:
        print(f"Error fetching profile: {e}")
        return None






