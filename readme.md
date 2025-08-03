# Study Buddy - Your AI-Powered Exam Preparer

Study Buddy is an interactive web application designed to help students prepare for various exams, from competitive entrance tests like IIT-JEE to university-level computer science courses. It leverages the power of Large Language Models (LLMs) to provide in-depth explanations, key formulas, revision notes, and practice questions on specific topics, tailored to the chosen subject and exam style.

## Project Overview

This project consists of:

* **`ui.py`**: The main Streamlit application script that provides the user interface and orchestrates the interaction with the LLM.
* **`template.json` / `template.py`**: Defines the prompt template used to instruct the LLM, ensuring consistent and high-quality educational content.
* **`requirements.txt`**: Lists all the necessary Python dependencies for running the application.

## Features

* **Customized Learning**: Select your "teacher" (IIT-JEE or University) and then choose a specific subject and topic.
* **Comprehensive Explanations**: The AI acts as an experienced professor, breaking down complex ideas with clarity, precision, and a focus on concepts and problem-solving techniques.
* **Detailed Content**: For each topic, it provides:
    1.  A conceptual explanation.
    2.  Key formulas or principles involved.
    3.  An in-depth explanation of every important sub-topic.
    4.  A quick revision of the topics covered.
    5.  Practice questions with brief hints or answers.
* **Visual Aids**: The AI is prompted to include necessary and relevant figures, diagrams, and tables for quick and clear understanding.
* **Flexible LLM Integration**: The application is set up to easily switch between Google Gemini and Hugging Face models. (Currently configured for `gemini-2.5-flash` by default).

## How it Works

The core of Study Buddy relies on a carefully crafted prompt template and LangChain for LLM orchestration:

1.  **Prompt Definition (`template.json` / `template.py`)**: A `PromptTemplate` is defined, instructing the LLM on its persona (an experienced professor preparing students for exams) and the expected structure and content of the explanation. It takes `teacher`, `subject`, and `topic` as input variables.
2.  **User Interface (`ui.py`)**: A Streamlit interface allows users to select:
    * **Teacher**: "IIT-JEE" or "University".
    * **Subject**: Options dynamically update based on the selected teacher (e.g., "Maths", "Physics", "Chemistry" for IIT-JEE; "Operating System", "Computer Networks", "DBMS" for University).
    * **Topic**: A wide range of specific topics relevant to the chosen subject and teacher are provided as options.
3.  **LLM Interaction**:
    * Upon clicking "Explain", the application loads the defined prompt template.
    * It initializes a language model (defaulting to `gemini-2.5-flash` from `langchain_google_genai`).
    * A LangChain `chain` is created, combining the prompt template and the LLM.
    * The `chain.invoke()` method is called with the user's selected `subject`, `topic`, and `teacher` as inputs to generate the educational content.
    * The generated response from the LLM is then displayed in the Streamlit interface.

## Setup and Installation

To set up and run the Study Buddy application locally, follow these steps:

1.  **Clone the Repository (or save files)**:
    Save all the provided files (`ui.py`, `template.json`, `template.py`, `requirements.txt`, and any other necessary data files like `car.csv`, `Zomato-data.csv` from previous contexts if they are part of this *single* project's broader scope, though they are not directly used by `ui.py` for the "Study Buddy" feature).

2.  **Create a Virtual Environment (Recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    [cite_start]The `requirements.txt` file lists all the necessary libraries[cite: 1].
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables**:
    Create a `.env` file in the project's root directory and add your API keys. For Google Gemini, you'll need:
    ```
    GOOGLE_API_KEY="your_google_api_key_here"
    ```
    If you plan to use Hugging Face, you'd also include:
    ```
    HF_API_TOKEN="your_huggingface_api_token_here"
    ```

5.  **Run the Streamlit Application**:
    ```bash
    streamlit run ui.py
    ```

    This command will open the application in your web browser.

## Project Structure

* **`ui.py`**: The Streamlit application interface.
* **`template.json`**: The JSON representation of the prompt template, created by `template.py`. This is loaded by `ui.py`.
* **`template.py`**: A helper script to define and save the `PromptTemplate` to `template.json`. You would run this once if you needed to regenerate or modify the `template.json` file.
* [cite_start]**`requirements.txt`**: Lists Python package dependencies[cite: 1].

## Extendability

The `ui.py` script is set up to allow easy swapping of LLMs. You can uncomment the `HuggingFaceEndpoint` and `ChatHuggingFace` lines in the `get_model()` function to use a Llama-3.1-8B-Instruct model, provided you have the `HF_API_TOKEN` set up and the `transformers` library installed.

Feel free to expand the `topics_map` in `ui.py` to include more subjects and topics for both IIT-JEE and University categories.
