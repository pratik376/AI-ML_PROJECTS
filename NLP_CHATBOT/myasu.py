import pdfplumber
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# ========== STEP 1: Extract Text from PDF ==========
def extract_pdf_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

raw_text = extract_pdf_text("sample_course_data.pdf")  # <-- Replace with your own

# ========== STEP 2: Extract Courses ==========
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

courses = extract_courses(raw_text)

# ========== STEP 3: Build FAQ Database ==========
faq_data = []
faq_answers = []
course_code_to_faq = {}

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
        course_code_to_faq[q.lower()] = code

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(faq_data)

# ========== STEP 4: Chat Logic with Memory ==========
last_course_code = None

def detect_course_code(text):
    match = re.search(r'(cs\s?\d{3})', text.lower())
    return match.group(1).replace(" ", "").upper() if match else None

def determine_intent(text):
    # Basic intent detection (can be extended)
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

def answer_user_question_with_context(user_input):
    global last_course_code

    course_code = detect_course_code(user_input)
    intent = determine_intent(user_input)

    if course_code:
        last_course_code = course_code
    elif not course_code and last_course_code:
        # Build implicit question from context
        if intent == "prerequisite":
            user_input = f"What are the prerequisites for {last_course_code}?"
        elif intent == "credits":
            user_input = f"How many credits is {last_course_code}?"
        elif intent == "instructor":
            user_input = f"Who is the instructor for {last_course_code}?"
        elif intent == "description":
            user_input = f"What is {last_course_code}?"
        else:
            return "Can you please specify what you want to know about the course?"

    else:
        return "Please mention a course code like CS101 so I can help you."

    # Search in FAQ
    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, faq_vectors)
    best_idx = similarities.argmax()
    score = similarities[0][best_idx]

    if score < 0.3:
        return "Sorry, I couldn't find a good answer for that."

    return faq_answers[best_idx]

# ========== STEP 5: Run the Chatbot ==========
if __name__ == "__main__":
    print("📚 Course Chatbot Ready! Ask about any CS course (type 'exit' to quit):\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break
        response = answer_user_question_with_context(user_input)
        print(f"Bot: {response}\n")