from openai import OpenAI
import os
from dotenv import load_dotenv
from loading_profiles import get_profile




def get_response(profile):
    load_dotenv()
    api_key = os.getenv("api_key")
    prompt = os.getenv("prompt")

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


text = """
Here’s a detailed rating of the LinkedIn profile based on the provided JSON-like structure:

### **Headline: 7/10**  
- **Strengths**: Clearly states current academic focus (CS & Econ) and institution (CWRU).  
- **Areas for Improvement**: Could be more dynamic or value-driven (e.g., "Aspiring Technologist & Economist | Passionate About X"). Adding a career aspiration or key skill could make it stand out more.

### **Experience: 9/10**  
- **Strengths**:  
  - Strong variety of roles (editorial, finance, software engineering, teaching).  
  - Descriptions are detailed, with quantifiable impact (e.g., "100,000 clients," "30 sessions with thousands in attendance").  
  - Uses emojis effectively to highlight key contributions.  
- **Areas for Improvement**:  
  - The BNP Paribas role lacks a description (could highlight key projects or skills gained).  
  - Some roles could better emphasize transferable skills (e.g., teamwork, leadership).  

### **Education: 8/10**  
- **Strengths**:  
  - Clear dual-degree path (CS + Econ) from a reputable university.  
  - Includes high school, which may be relevant for international connections (Singapore).  
- **Areas for Improvement**:  
  - Could add GPA (if strong), relevant coursework, or extracurriculars to showcase depth.  

### **Skills: 6/10**  
- **Strengths**:  
  - Relevant technical (Vue.js, Django) and soft skills (Teaching).  
- **Areas for Improvement**:  
  - Limited in number—could add more hard skills (Java, Cypress, Python) and industry-relevant tools.  
  - No endorsements visible in this snippet (encourage colleagues to endorse).  

### **Achievements & Impact: 8/10**  
- **Strengths**:  
  - Certifications (FINRA, Linux Foundation) add credibility.  
  - Quantifiable wins in experience (e.g., "students scored higher," "100,000 clients").  
- **Areas for Improvement**:  
  - Could add standalone "Projects" or "Honors" section for academic/personal achievements.  
  - German B2 is great—could highlight if relevant to career goals.  

### **Overall Rating: 8/10**  
This is a **strong profile** for a student/early-career professional, with clear expertise in CS/Econ and tangible impact in roles. The experience section is particularly standout.  

### **Final Recommendations**:  
1. **Revamp Headline**: Add a career aspiration or unique value proposition.  
2. **Expand Skills**: Include more technical tools (Java, Python, Cypress) and soft skills (Leadership, Agile).  
3. **Add BNP Paribas Description**: Even a brief note on projects/learnings would help.  
4. **Highlight Projects**: If possible, add a "Projects" section for academic/personal work.  
5. **Seek Endorsements**: Boost credibility by getting skills validated by peers/managers.  

**Bonus**: Consider a short "About" section summarizing passions/goals—this helps recruiters quickly understand your trajectory.  

Great foundation—polishing these areas will make it even more competitive!
"""




