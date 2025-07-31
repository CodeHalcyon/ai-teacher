from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
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
    return ChatGoogleGenerativeAI(model='gemini-2.5-flash')
    # llm = HuggingFaceEndpoint(
    #     model='meta-llama/Llama-3.1-8B-Instruct',
    #     task='text-generation'
    # )
    # return ChatHuggingFace(llm=llm)


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
        "Maths": ["Determinants",
  "Matrices",
  "Relations and Functions",
  "Inverse Trigonometric Functions",
  "Continuity and Differentiability",
  "Method of Differentiation",
  "Application of Derivatives",
  "Indefinite Integration",
  "Definite Integration",
  "Application of Integrals",
  "Differential Equations",
  "Vector Algebra",
  "Three-dimensional Geometry",
  "Linear Programming",
  "Probability"],
        "Physics": ["Electric Charges and Fields",
  "Electrostatic Potential and Capacitance",
  "Current Electricity",
  "Moving Charges and Magnetism",
  "Magnetism and Matter",
  "Electromagnetic Induction",
  "Alternating Current",
  "Electromagnetic Waves",
  "Ray Optics and Optical Instruments",
  "Wave Optics",
  "Dual Nature of Radiation and Matter",
  "Atoms",
  "Nuclei",
  "Semiconductor Electronics - Materials, Devices and Simple Circuits"],
        "Chemistry": [ "Solutions",
  "Electrochemistry",
  "Chemical Kinetics",
  "Organic 11th - Revision { GOC & Hydrocarbon }",
  "Haloalkanes and Haloarenes",
  "Alcohols, Phenols and Ethers",
  "Aldehydes, Ketones and Carboxylic Acids",
  "Amines",
  "Biomolecules",
  "Coordination Compounds",
  "The p-Block Elements",
  "The d- and f- block Elements",
  "Salt analysis",
  "The Solid State",
  "Surface Chemistry",
  "General Principles and Processes of Isolation of Metals",
  "Polymers",
  "Chemistry in Everyday Life"]
        },
    "University": {
        "Operating System": [
            "Introduction to Operating Systems (Definition, Functions, Types)",
    "Process Management (Process vs. Program, PCB, Process States)",
    "Threads and Multithreading (User-level vs. Kernel-level, Benefits)",
    "CPU Scheduling Algorithms (FCFS, SJF, Round Robin, Priority, Preemptive vs. Non-preemptive)",
    "Inter-Process Communication (IPC Mechanisms: Pipes, Shared Memory, Message Queues)",
    "Process Synchronization (Race Conditions, Critical Section, Mutexes, Semaphores, Monitors)",
    "Deadlocks (Conditions, Prevention, Avoidance, Detection, Recovery, Banker's Algorithm)",
    "Memory Management (Logical vs. Physical Address, Fragmentation, Paging, Segmentation)",
    "Virtual Memory (Demand Paging, Page Faults, Thrashing, Page Replacement Algorithms)",
    "File Systems (File Allocation Methods, Directory Structures, Inodes)",
    "I/O Systems (Device Drivers, Buffering, Caching, SPOOLing)",
    "System Calls (Purpose and Examples)",
    "Kernel (Types and Functions)",
    "Context Switching",
    "Disk Management and RAID (Disk Scheduling Algorithms, RAID Levels)",
    "Operating System Services and Protection",
    "Concurrency Control (General concepts beyond just processes/threads)",
    "Boot Process and System Startup",
    "Security in Operating Systems (Authentication, Authorization, Access Control)",
    "Distributed Operating Systems (Basic concepts if applicable to the role)"
            ],
        "Computer Networks": [
            "OSI and TCP/IP Models (Layers, Functions, Comparison)",
    "Network Topologies (Bus, Star, Ring, Mesh, Hybrid)",
    "Network Devices (Hubs, Switches, Routers, Bridges, Gateways)",
    "IP Addressing and Subnetting (IPv4, IPv6, CIDR, VLSM)",
    "Data Link Layer Concepts (MAC Addressing, Error Detection/Correction, Flow Control, ARP, RARP)",
    "Ethernet (CSMA/CD, Frame Format)",
    "Routing Algorithms (Distance Vector, Link State, OSPF, BGP)",
    "Transport Layer Protocols (TCP - Connection setup/teardown, Flow Control, Congestion Control; UDP - Connectionless)",
    "Application Layer Protocols (HTTP/HTTPS, FTP, DNS, SMTP, POP3, IMAP, DHCP, SNMP)",
    "Network Security Fundamentals (Firewalls, VPNs, basic Encryption/Decryption concepts)",
    "Wireless Networking (Wi-Fi standards, Bluetooth, Cellular Networks basic concepts)",
    "Network Services (NAT, DHCP, DNS Resolution Process)",
    "Client-Server Model vs. Peer-to-Peer",
    "Network Performance Metrics (Bandwidth, Latency, Throughput)",
    "Packet Switching vs. Circuit Switching",
    "Network troubleshooting tools and techniques (ping, traceroute, netstat)",
    "Socket Programming Basics (if applicable to the role)",
    "Content Delivery Networks (CDNs) - basic understanding",
    "Cloud Networking Concepts (VPCs, Security Groups - if relevant to the role)",
    "Emerging Network Technologies (SDN, NFV - basic awareness)"
            ],
"DBMS": ["Introduction to DBMS (Concepts, Advantages, Architecture - 1-tier, 2-tier, 3-tier)",
    "Data Models (ER Models and Relational Models, Hierarchical, Network, Object-Oriented - basic understanding)",
    "Relational Algebra and Relational Calculus",
    "SQL Fundamentals (DDL, DML, DCL, TCL Commands)",
    "SQL Queries (SELECT statements, Filtering, Sorting, Grouping, Aggregate Functions)",
    "SQL Joins (INNER, LEFT, RIGHT, FULL, SELF Joins)",
    "Subqueries and Common Table Expressions (CTEs)",
    "Normalization and Functional Dependencies (1NF, 2NF, 3NF, BCNF, 4NF, 5NF - with examples)",
    "Database Keys (Primary Key, Foreign Key, Candidate Key, Super Key, Unique Key)",
    "Indexing (Types of Indexes, B-tree, B+ tree, Hashing, Clustered vs. Non-Clustered)",
    "Query Optimization (Explain Plan, Cost-based Optimization, Heuristic Optimization)",
    "Transaction Management (ACID Properties: Atomicity, Consistency, Isolation, Durability)",
    "Concurrency Control (Problems: Lost Update, Dirty Read, Unrepeatable Read, Phantom Read; Solutions: Locking, Timestamping, Optimistic Concurrency Control)",
    "Database Security (Authentication, Authorization, Views, Roles)",
    "Database Backup and Recovery",
    "Stored Procedures, Functions, Triggers, and Cursors",
    "Views (Purpose and Usage)",
    "Data Warehousing and OLAP (Basic concepts, if relevant for the role)",
    "NoSQL Databases (Basic understanding of types and use cases - Key-Value, Document, Column-family, Graph - if relevant)",
    "Distributed Databases (Concepts, Advantages/Disadvantages)"] }
}

options = topics_map[teacher][subject]
topic = st.selectbox("Select a topic", options)

if st.button('Explain'):
    chain = template | model
    
    with st.spinner("Generating..."):
        response = chain.invoke({
            'subject': subject,
            'topic': topic,
            'teacher': teacher
        })
        content = response.content
        if isinstance(content, list):
            for c in content:
                st.write(c)
        else:
            st.write(content)
