import streamlit as st
import google.generativeai as genai
import os

# Set up the Gemini API key from environment variables or Streamlit secrets
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Gemini API key not found. Please set it as an environment variable or in Streamlit secrets.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-pro')

def load_prompt():
    """Loads the prompt from a separate file."""
    try:
        with open("prompt.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        st.error("Prompt file 'prompt.txt' not found.")
        return None

def analyze_content(content, keyword, prompt_template):
    """
    Analyzes the content using the Gemini API and the provided prompt.
    """
    if not prompt_template:
        return "Error: Prompt template is missing."

    full_prompt = prompt_template.replace("{{content}}", content).replace("{{keyword}}", keyword)

    try:
        with st.spinner("Analyzing content..."):
            response = model.generate_content(full_prompt)
            return response.text
    except Exception as e:
        return f"An error occurred: {e}"

st.set_page_config(page_title="SEO & Content Quality Analyzer", layout="wide")
st.title("SEO & Content Quality Analyzer")
st.subheader("Leverage AI to refine your content for quality and search engine optimization.")

# User inputs
content_input = st.text_area("Paste your content here:", height=400, help="The article or text you want to analyze.")
keyword_input = st.text_input("Target Keyword:", help="The primary keyword you are trying to rank for.")

# The magic button
if st.button("Analyze Content", type="primary"):
    if content_input and keyword_input:
        prompt_template = load_prompt()
        if prompt_template:
            result = analyze_content(content_input, keyword_input, prompt_template)
            st.markdown(result)
    else:
        st.warning("Please provide both content and a target keyword.")

st.sidebar.markdown(
    """
    ## How It Works
    This app uses the Gemini 2.5 Pro API to analyze your content against a custom prompt. It provides a detailed review based on core SEO and quality rating guidelines, including:
    - **Grammar & Spelling**
    - **Google Quality Rater Guidelines**
    - **E-E-A-T (Experience, Expertise, Authoritativeness, Trust)**
    - **Content Uniqueness & Effort**
    - **Likelihood of Ranking for your Keyword**

    Simply paste your content, add your target keyword, and let the AI do the analysis.
    """
)
