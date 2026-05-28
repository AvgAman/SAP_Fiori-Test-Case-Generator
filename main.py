import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="SAP Fiori Test Case Generator",
    layout="wide"
)

st.title("SAP Fiori Regression Test Case Generator")

# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Prompt Template
template = """
You are an SAP Fiori QA expert.

Generate detailed regression test cases.

Requirement:
{input}

Generate:
1. Positive test cases
2. Negative test cases
3. Boundary test cases
4. Regression scenarios

Format:
- Test Case ID
- Scenario
- Steps
- Expected Result
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | llm

# Input Box
user_input = st.text_area(
    "Enter SAP Fiori Requirement",
    height=250,
    placeholder="Enter SAP Fiori requirement here..."
)

# Button
if st.button("Generate Test Cases"):

    if user_input.strip() == "":
        st.warning("Please enter requirement")
    else:

        with st.spinner("Generating test cases..."):

            response = chain.invoke({
                "input": user_input
            })

            st.text_area(
                "Generated Test Cases",
                value=response.content,
                height=500
            )