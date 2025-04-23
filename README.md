# CSDS 285 Final Project

## What It Does

**Jakob’s LinkedIn Review** provides a rating and feedback on a person’s LinkedIn profile. It does this by:

- Parsing the profile into a JSON-like structure
- Asking DeepSeek to rate it on specific attributes

**Live site**: [https://jakobs-linkedin-reviewer.ngrok.app/](https://jakobs-linkedin-reviewer.ngrok.app/)

---

## How It Works

- The codebase is primarily written in **Python**
- Shell scripts are used for setup
- The website uses **Streamlit**, which enables markdown-style text and form handling

### Process:

1. User submits their LinkedIn profile
2. A web scraper logs into a **burner LinkedIn account**
3. The scraper extracts:
   - Headline
   - Experience
   - Education
   - Other relevant data
4. A profile object is created from the data
5. The object is trimmed and sent to **DeepSeek** for evaluation
6. DeepSeek responds in a specific format
7. The response is parsed and displayed on the page

---

## How It’s Hosted

The web app is hosted on a **personal Raspberry Pi 4B** running Linux.

[https://jakobs-linkedin-reviewer.ngrok.app/](https://jakobs-linkedin-reviewer.ngrok.app/)

---

## Why Host It Personally?

- Avoid exposing **API keys** and **LinkedIn login info** on CWRU’s EECSLab server
- DeepSeek API **blocks CWRU traffic**
  - (Try loading [https://platform.deepseek.com/](https://platform.deepseek.com/) from Case Wireless!)
- EECSLab servers **don't allow installing Python dependencies**
- LinkedIn **doesn’t block scrapers** from Jakob’s personal Wi-Fi
- It’s a good way to **learn Linux server configuration**

---

## How to Host It

### Step 1:
Install Raspberry Pi OS (Lite recommended)  
➡ [Download OS](https://www.raspberrypi.com/software/operating-systems/)

### Step 2:
Boot the Raspberry Pi with the OS. Ensure it has **internet access**.

### Step 3:
Run `initial_setup.sh`  
This script:
- Installs Python
- Installs software for reverse proxying
- Clones the codebase
- Installs Python dependencies

> 💡 Jakob avoids port forwarding due to security concerns and uses a **reverse proxy** (e.g., ngrok)

---

### Step 4:
Create a folder named `.streamlit` with a `secrets.toml` file containing:

```toml
api_key = "your_deepseek_key"
pw = "linkedin_password"
email = "linkedin_email"
prompt = "deepseek_prompt_text"
