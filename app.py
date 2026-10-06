import streamlit as st
import random

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Placement Preparation Platform",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "aptitude_score" not in st.session_state:
    st.session_state.aptitude_score = 0

if "coding_score" not in st.session_state:
    st.session_state.coding_score = 0

if "interview_score" not in st.session_state:
    st.session_state.interview_score = 0

if "questions_attempted" not in st.session_state:
    st.session_state.questions_attempted = 0

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("🎓 Placement Platform")

page = st.sidebar.radio(
    "Choose a Module",
    [
        "🏠 Home",
        "📄 Resume Analyzer",
        "🧠 Aptitude Practice",
        "💻 Coding Practice",
        "🛠️ Interview Preparation",
        "🤖 AI Assistant",
        "📊 Performance Dashboard",
        "💡 Placement Tips"
    ]
)

# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------

if page == "🏠 Home":

    st.title("🎓 AI Placement Preparation Platform")

    st.subheader("Prepare smarter. Practice better. Get placed.")

    st.write(
        "Welcome to the AI Placement Preparation Platform. "
        "This platform helps students prepare for placements "
        "through aptitude, coding, interview and resume practice."
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Aptitude Score", st.session_state.aptitude_score)

    with col2:
        st.metric("Coding Score", st.session_state.coding_score)

    with col3:
        st.metric("Interview Score", st.session_state.interview_score)

    st.markdown("---")

    st.subheader("📚 Available Modules")

    st.write("📄 Resume Analyzer")
    st.write("🧠 Aptitude Practice")
    st.write("💻 Coding Practice")
    st.write("🛠️ Interview Preparation")
    st.write("🤖 AI Assistant")
    st.write("📊 Performance Dashboard")
    st.write("💡 Placement Tips")

# ---------------------------------------------------------
# RESUME ANALYZER
# ---------------------------------------------------------

elif page == "📄 Resume Analyzer":

    st.title("📄 Resume Analyzer")

    st.write(
        "Upload your resume to check basic resume sections."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file is not None:

        st.success(
            f"Resume uploaded: {uploaded_file.name}"
        )

        file_name = uploaded_file.name.lower()

        if file_name.endswith(".txt"):

            text = uploaded_file.read().decode(
                "utf-8",
                errors="ignore"
            )

            st.subheader("Resume Preview")

            st.text_area(
                "Resume Content",
                text,
                height=250
            )

            text_lower = text.lower()

            sections = {
                "Education": [
                    "education",
                    "degree",
                    "b.tech",
                    "bachelor"
                ],
                "Skills": [
                    "skills",
                    "python",
                    "java",
                    "sql",
                    "c++"
                ],
                "Projects": [
                    "projects",
                    "project"
                ],
                "Experience": [
                    "experience",
                    "internship",
                    "intern"
                ],
                "Contact": [
                    "email",
                    "phone",
                    "mobile"
                ]
            }

            st.subheader("📋 Resume Analysis")

            found = 0

            for section, keywords in sections.items():

                if any(
                    keyword in text_lower
                    for keyword in keywords
                ):

                    st.success(
                        f"✅ {section} section detected"
                    )

                    found += 1

                else:

                    st.warning(
                        f"⚠️ Consider adding {section} information"
                    )

            score = int(
                (found / len(sections)) * 100
            )

            st.metric(
                "Resume Completeness Score",
                f"{score}%"
            )

        else:

            st.info(
                "PDF/DOCX file detected. "
                "Basic file upload is working."
            )

# ---------------------------------------------------------
# APTITUDE PRACTICE
# ---------------------------------------------------------

elif page == "🧠 Aptitude Practice":

    st.title("🧠 Aptitude Practice")

    st.write(
        "Test your aptitude skills."
    )

    questions = [

        {
            "question": "What is 20% of 250?",
            "options": ["40", "50", "60", "70"],
            "answer": "50"
        },

        {
            "question": "If 5x = 45, what is x?",
            "options": ["5", "7", "9", "11"],
            "answer": "9"
        },

        {
            "question": "Which number comes next: 2, 4, 8, 16, ?",
            "options": ["20", "24", "32", "36"],
            "answer": "32"
        },

        {
            "question": (
                "A train travels 60 km in 1 hour. "
                "How far will it travel in 3 hours?"
            ),
            "options": [
                "120 km",
                "150 km",
                "180 km",
                "200 km"
            ],
            "answer": "180 km"
        },

        {
            "question": "What is the average of 10, 20 and 30?",
            "options": ["15", "20", "25", "30"],
            "answer": "20"
        }
    ]

    question = random.choice(questions)

    st.subheader("Question")

    st.write(question["question"])

    selected = st.radio(
        "Select your answer:",
        question["options"],
        key="aptitude_question"
    )

    if st.button("Check Answer"):

        st.session_state.questions_attempted += 1

        if selected == question["answer"]:

            st.success("🎉 Correct Answer!")

            st.session_state.aptitude_score += 1

        else:

            st.error("❌ Wrong Answer")

            st.info(
                f"Correct answer: {question['answer']}"
            )

    st.markdown("---")

    st.info(
        f"Your Aptitude Score: "
        f"{st.session_state.aptitude_score}"
    )

# ---------------------------------------------------------
# CODING PRACTICE
# ---------------------------------------------------------

elif page == "💻 Coding Practice":

    st.title("💻 Coding Practice")

    st.write(
        "Practice basic programming problems."
    )

    coding_questions = [

        {
            "question": (
                "Which data type is used to store "
                "True or False in Python?"
            ),
            "answer": "bool"
        },

        {
            "question": (
                "Which keyword is used to define a "
                "function in Python?"
            ),
            "answer": "def"
        },

        {
            "question": (
                "Which symbol is used for comments "
                "in Python?"
            ),
            "answer": "#"
        }
    ]

    coding_question = random.choice(
        coding_questions
    )

    st.subheader("Coding Question")

    st.write(
        coding_question["question"]
    )

    answer = st.text_input(
        "Enter your answer:"
    )

    if st.button("Check Coding Answer"):

        st.session_state.questions_attempted += 1

        if answer.strip().lower() == coding_question["answer"]:

            st.success("🎉 Correct Answer!")

            st.session_state.coding_score += 1

        else:

            st.error("❌ Wrong Answer")

            st.info(
                f"Correct answer: "
                f"{coding_question['answer']}"
            )

# ---------------------------------------------------------
# INTERVIEW PREPARATION
# ---------------------------------------------------------

elif page == "🛠️ Interview Preparation":

    st.title("🛠️ Interview Preparation")

    st.write(
        "Practice common placement interview questions."
    )

    interview_questions = [

        "Tell me about yourself.",

        "What are your strengths?",

        "What are your weaknesses?",

        "Why should we hire you?",

        "Where do you see yourself in five years?",

        "Explain Object-Oriented Programming.",

        "What is inheritance in Java?",

        "What is polymorphism?",

        "What is DBMS?",

        "What is the difference between primary key and foreign key?"
    ]

    selected_question = random.choice(
        interview_questions
    )

    st.subheader("Interview Question")

    st.info(selected_question)

    answer = st.text_area(
        "Write your answer:"
    )

    if st.button("Submit Interview Answer"):

        if answer.strip():

            st.success(
                "Answer submitted successfully!"
            )

            st.session_state.interview_score += 1

        else:

            st.warning(
                "Please enter an answer."
            )

# ---------------------------------------------------------
# AI ASSISTANT
# ---------------------------------------------------------

elif page == "🤖 AI Assistant":

    st.title("🤖 AI Placement Assistant")

    st.write(
        "Ask questions related to placement preparation."
    )

    user_question = st.text_area(
        "Ask your question:"
    )

    if st.button("Get Guidance"):

        if user_question.strip():

            question = user_question.lower()

            if "java" in question:

                response = (
                    "For Java interviews, prepare OOP concepts, "
                    "inheritance, polymorphism, constructors, "
                    "exception handling, collections and threads."
                )

            elif "resume" in question:

                response = (
                    "Keep your resume simple and professional. "
                    "Include education, skills, projects, "
                    "certifications and contact details."
                )

            elif "aptitude" in question:

                response = (
                    "Practice percentages, ratios, averages, "
                    "profit and loss, time and work, "
                    "probability and logical reasoning."
                )

            elif "interview" in question:

                response = (
                    "Practice self-introduction, technical "
                    "questions, HR questions and project "
                    "explanation."
                )

            else:

                response = (
                    "Prepare aptitude, coding, technical "
                    "subjects, projects, resume and HR "
                    "interview questions regularly."
                )

            st.success("AI Guidance")

            st.write(response)

        else:

            st.warning(
                "Please enter a question."
            )

# ---------------------------------------------------------
# PERFORMANCE DASHBOARD
# ---------------------------------------------------------

elif page == "📊 Performance Dashboard":

    st.title("📊 Performance Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Aptitude",
            st.session_state.aptitude_score
        )

    with col2:

        st.metric(
            "Coding",
            st.session_state.coding_score
        )

    with col3:

        st.metric(
            "Interview",
            st.session_state.interview_score
        )

    st.markdown("---")

    st.subheader("📈 Overall Progress")

    total_score = (
        st.session_state.aptitude_score
        + st.session_state.coding_score
        + st.session_state.interview_score
    )

    st.metric(
        "Total Score",
        total_score
    )

    st.metric(
        "Questions Attempted",
        st.session_state.questions_attempted
    )

# ---------------------------------------------------------
# PLACEMENT TIPS
# ---------------------------------------------------------

elif page == "💡 Placement Tips":

    st.title("💡 Placement Tips")

    tips = [

        "📚 Study aptitude every day.",

        "💻 Practice coding problems regularly.",

        "📝 Keep your resume updated.",

        "🎤 Practice your self-introduction.",

        "🧠 Revise OOP, DBMS, OS and Computer Networks.",

        "🚀 Build and explain at least one good project.",

        "💬 Improve communication skills.",

        "📅 Follow a daily placement preparation schedule.",

        "🔎 Research the company before the interview.",

        "😊 Stay confident during interviews."
    ]

    for tip in tips:

        st.write(tip)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.sidebar.markdown("---")

st.sidebar.info(
    "AI Placement Preparation Platform\n\n"
    "Developed for student placement preparation."
)