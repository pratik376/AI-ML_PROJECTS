# Note: this project is developed by Pratik Babariya and only they are allowed to change this code .... thanks for your attention


# myvenv\Scripts\activate
import streamlit as st
import pdfplumber
import re
import spacy
import base64
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

# ------------------- Helper functions -------------------

def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def display_header(img_file):
    bin_str = get_base64_of_bin_file(img_file)
    st.markdown(
        f"""
        <div style="text-align:center; margin-bottom:20px;">
            <img src="data:image/png;base64,{bin_str}" width="400">
        </div>
        """,
        unsafe_allow_html=True
    )

display_header("my_asu.png")

@st.cache_data
def extract_pdf_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

@st.cache_data
def extract_courses(text):
    course_pattern = re.findall(r'(CS\d{3})\s*-\s*(.*?)\n(.*?)(?=\nCS\d{3}|$)', text, re.DOTALL)
    courses = {}
    for code, name, rest in course_pattern:
        prerequisites = re.findall(r'Prerequisite[s]*: (.*)', rest)
        credits = re.findall(r'Credit[s]*: (\d+)', rest)
        instructor = re.findall(r'Instructor[s]*: (.*)', rest)
        courses[code.upper()] = {
            "name": name.strip(),
            "description": rest.strip(),
            "prerequisites": prerequisites[0] if prerequisites else "None",
            "credits": credits[0] if credits else "Unknown",
            "instructor": instructor[0] if instructor else "Unknown"
        }
    return courses

def detect_course_code(text):
    match = re.search(r'(cs\s?\d{3})', text.lower())
    return match.group(1).replace(" ", "").upper() if match else None

def determine_intent(text):
    text = text.lower()
    if "prerequisite" in text:
        return "prerequisite"
    elif "credit" in text or "duration" in text:
        return "credits"
    elif "instructor" in text or "teacher" in text:
        return "instructor"
    elif "what is" in text or "description" in text or "about" in text:
        return "description"
    else:
        return "unknown"

def prepare_faq_data(courses):
    faq_data = []
    faq_answers = []
    for code, info in courses.items():
        entries = [
            (f"What is {code}?", f"{code} - {info['name']}: {info['description']}"),
            (f"What are the prerequisites for {code}?", f"Prerequisites for {code}: {info['prerequisites']}"),
            (f"How many credits is {code}?", f"{code} has {info['credits']} credits."),
            (f"Who is the instructor for {code}?", f"Instructor for {code} is {info['instructor']}."), 
        ]
        for q, a in entries:
            faq_data.append(q)
            faq_answers.append(a)
    return faq_data, faq_answers

def answer_user_question(user_input, vectorizer, faq_vectors, faq_data, faq_answers, last_course_code):
    course_code = detect_course_code(user_input)
    intent = determine_intent(user_input)

    if course_code:
        last_course_code = course_code
    elif not course_code and last_course_code:
        if intent == "prerequisite":
            user_input = f"What are the prerequisites for {last_course_code}?"
        elif intent == "credits":
            user_input = f"How many credits is {last_course_code}?"
        elif intent == "instructor":
            user_input = f"Who is the instructor for {last_course_code}?"
        elif intent == "description":
            user_input = f"What is {last_course_code}?"
        else:
            return "Please clarify your question.", last_course_code
    else:
        return "Please mention a course code like CS101 so I can help you.", last_course_code

    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, faq_vectors)
    best_idx = similarities.argmax()
    score = similarities[0][best_idx]

    if score < 0.3:
        return "Sorry, I couldn't find a good answer for that.", last_course_code

    return faq_answers[best_idx], last_course_code

# ------------------- Streamlit UI -------------------

st.set_page_config(page_title="University Course Chatbot", layout="centered")

# ASU-styled CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #FFF8E1, white);
    }
    .user-msg {
        background-color: #FFC627;
        color: black;
        padding: 10px 15px;
        border-radius: 20px;
        margin: 8px 0;
        text-align: right;
        max-width: 75%;
        margin-left: auto;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.2);
    }
    .bot-msg {
        background-color: #8C1D40;
        color: white;
        padding: 10px 15px;
        border-radius: 20px;
        margin: 8px 0;
        text-align: left;
        max-width: 75%;
        margin-right: auto;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("Ask me about courses like CS101, CS102, etc. I can answer things like prerequisites, credits, or instructors.")

uploaded_file = st.file_uploader("📄 Upload your course PDF", type="pdf")

if uploaded_file:
    text = extract_pdf_text(uploaded_file)
    courses = extract_courses(text)
    faq_data, faq_answers = prepare_faq_data(courses)
    vectorizer = TfidfVectorizer().fit(faq_data)
    faq_vectors = vectorizer.transform(faq_data)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "last_course_code" not in st.session_state:
        st.session_state.last_course_code = None

    # Display previous chat
    for sender, msg in st.session_state.chat_history:
        if sender == "user":
            st.markdown(f'<div class="user-msg">{msg}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-msg">{msg}</div>', unsafe_allow_html=True)

    # ------------------- Fixed bottom input -------------------
    def handle_input():
        user_input = st.session_state.user_input
        if not user_input:
            return

        # Append user message
        st.session_state.chat_history.append(("user", user_input))

        # Generate bot response
        response, updated_code = answer_user_question(
            user_input,
            vectorizer,
            faq_vectors,
            faq_data,
            faq_answers,
            st.session_state.last_course_code
        )
        st.session_state.last_course_code = updated_code
        st.session_state.chat_history.append(("assistant", response))

        # Clear input safely
        st.session_state.user_input = ""  # ✅ no rerun needed

    st.markdown('<div style="position: fixed; bottom: 10px; width: 90%;">', unsafe_allow_html=True)
    st.text_input(
        "Ask me anything about a course...",
        key="user_input",
        on_change=handle_input
    )
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("Please upload a course syllabus PDF to begin.")
