# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import load_prompt
# from dotenv import load_dotenv
# import streamlit as st
# load_dotenv()
# template = load_prompt("template.json")
# st.header('Study Buddy')

# model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

# # user_input = st.text_input(label='Enter a prompt', max_chars=100)
# teacher = st.selectbox(
#     label="Select a teacher",
#     options=["IIT-JEE", "University"]
# )
# subject=[]
# options=[]
# if teacher == "IIT-JEE":
#     subject = st.selectbox(
#         label="Select a subject",
#         options=["Maths", "Physics", "Chemistry"]
#     )
# if teacher == 'University':
#     subject = st.selectbox(
#         label="Select a subject",
#         options=["Operating System", "Computer Networks", "DBMS"]
#     )
    

# if subject == "Maths":
#     options=["Quadratic Equations and Complex Numbers", 
#              "Permutation and Combination & Binomial Theorem",
#              "Calculus (Limits, Continuity, Differentiability, Integration)",
#              "Coordinate Geometry (Straight Lines, Circles, Parabola, Ellipse, Hyperbola)",]
# if subject == "Physics":
#     options=["Kinematics and Laws of Motion",
#              "Work, Energy and Power",
#              "Current Electricity and Circuits",
#              "Ray and Wave Optics",]
# if subject == "Chemistry":
#     options=["Periodic Table and Periodicity",
#              "Chemical Bonding and Molecular Structure",
#              "Chemical Kinetics",
#              "Thermodynamics",
#              "Mole Concept and Stoichiometry"]
# if subject == "Operating System":
#     options=["Process Management and Scheduling",
#              "Threads and Concurrency",
#              "Memory Management (Paging, Segmentation, Virtual Memory",
#              "Deadlocks: Detection, Prevention, and Avoidance",
#              "File Systems and I/O Management"]
# if subject == "Computer Networks":
#     options=["OSI and TCP/IP Models",
#              "IP Addressing and Subnetting",
#              "Routing Algorithms (Distance Vector, Link State)",
#              "Transport Layer Protocols (TCP, UDP)",
#              "Application Layer Protocols (HTTP, FTP, DNS, etc.)"]
# if subject == "DBMS":
#     options=["ER Models and Relational Models",
#              "SQL and Relational Algebra",
#              "Normalization and Functional Dependencies",
#              "Transaction Management and Concurrency Control",
#              "Indexing and Query Optimization"]

# topic = st.selectbox(
#     label="Select a topic",
#     options=options
# )

# prompt = template.invoke({
#     'subject': subject,
#     'topic':topic,
#     'teacher':teacher
# })

# if st.button('press me!'):
#     response = model.invoke(prompt)
#     content = response.content

#     # If content is a list, write each item; otherwise, write it directly
#     if isinstance(content, list):
#         for c in content:
#             st.write(c)
#     else:
#         st.write(content)


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
st.header('Study Buddy')

@st.cache_data
def load_my_prompt():
    return load_prompt("template.json")

@st.cache_resource
def get_model():
    return ChatGoogleGenerativeAI(model='gemini-2.5-pro')

model = get_model()
template = load_my_prompt()

teacher = st.selectbox("Select a teacher", ["IIT-JEE", "University"])

subject_options = {
    "IIT-JEE": ["Maths", "Physics", "Chemistry"],
    "University": ["Operating System", "Computer Networks", "DBMS"]
}
subject = st.selectbox("Select a subject", subject_options[teacher])

topics_map = {
    "IIT-JEE": {
        "Maths": ["Quadratic Equations and Complex Numbers", 
        "Permutation and Combination & Binomial Theorem",
        "Calculus (Limits, Continuity, Differentiability, Integration)",
        "Coordinate Geometry (Straight Lines, Circles, Parabola, Ellipse, Hyperbola)"],
        "Physics": ["Kinematics and Laws of Motion", "Work, Energy and Power",
                    "Current Electricity and Circuits", "Ray and Wave Optics"],
        "Chemistry": ["Periodic Table and Periodicity", "Chemical Bonding and Molecular Structure", "Chemical Kinetics", "Thermodynamics", "Mole Concept and Stoichiometry"]
        },
    "University": {
        "Operating System": ["Process Management and Scheduling", "Threads and Concurrency",
        "Memory Management (Paging, Segmentation, Virtual Memory",
        "Deadlocks: Detection, Prevention, and Avoidance",
        "File Systems and I/O Management"],
        "Computer Networks": ["OSI and TCP/IP Models", "IP Addressing and Subnetting",
"Routing Algorithms (Distance Vector, Link State)",
"Transport Layer Protocols (TCP, UDP)",
"Application Layer Protocols (HTTP, FTP, DNS, etc.)"],
"DBMS": ["ER Models and Relational Models", "SQL and Relational Algebra",
"Normalization and Functional Dependencies",
"Transaction Management and Concurrency Control",
"Indexing and Query Optimization"] }
}

options = topics_map[teacher][subject]
topic = st.selectbox("Select a topic", options)

prompt = template.invoke({
    'subject': subject,
    'topic': topic,
    'teacher': teacher
})

if st.button('press me!'):
    with st.spinner("Generating..."):
        response = model.invoke(prompt)
        content = response.content
        if isinstance(content, list):
            for c in content:
                st.write(c)
        else:
            st.write(content)
