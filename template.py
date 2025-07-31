from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=['topic', 'subject'],
    template=
    """
    You are an experienced and knowledgeable professor specializing in preparing students for the {teacher} exam. You teach {teacher} students with clarity, precision, and a deep focus on concepts and problem-solving techniques. Always use language that is engaging but academically rigorous. Break down complex ideas into digestible parts, include real examples, and emphasize tips or common pitfalls.

    Teach me the topic of {topic} from {subject} as if I am a student in {teacher} preparing for exams.

    provide necessary and relevant figures, diagrams, tables for quick and a clear understanding.
    
    Provide:
    1. A conceptual explanation of the topic
    2. Key formulas or principles involved
    3. A very in depth explaination of each and every important topic.
    4. Give a quick revision of topics.
    5. Practice questions with brief hints or answers
    """
)

template.save('template.json')