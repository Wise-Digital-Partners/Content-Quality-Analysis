SEO & Content Quality Analyzer
==============================

This is a web application built with Streamlit and Python that leverages the Google Gemini 2.5 Pro API to analyze content for quality and search engine optimization (SEO) features. The app provides a detailed report based on Google's Quality Rater Guidelines and the content's potential to rank for a specific keyword.

Features
--------

-   **Comprehensive Content Analysis:** Evaluates content for grammar, spelling, and readability.

-   **Quality Rater Guidelines Assessment:** Analyzes content against key criteria like E-E-A-T (Experience, Expertise, Authoritativeness, and Trust), originality, and user experience.

-   **SEO & Keyword Analysis:** Determines how well the content aligns with a target keyword and assesses its likelihood of ranking.

-   **Actionable Recommendations:** Provides prioritized recommendations for improving the content's quality and SEO performance.

-   **Modular Design:** The analysis prompt is stored in a separate file (`prompt.txt`), making it easy to update and customize.

Technologies Used
-----------------

-   **Python:** The core programming language for the application.

-   **Streamlit:** Used to create the interactive user interface.

-   **Google Gemini 2.5 Pro API:** The large language model powering the content analysis.

Setup and Deployment
--------------------

### 1\. Prerequisites

-   Python 3.8 or higher

-   A Google Gemini API Key

### 2\. File Structure

Ensure your project directory contains the following two files:

-   `app.py`: The main Streamlit application script.

-   `prompt.txt`: The text file containing the custom prompt for the Gemini model.

### 3\. Installation

Install the required Python packages using `pip`:

```
pip install streamlit google-generativeai

```

### 4\. API Key Configuration

To use the Gemini API, you must set your API key. Streamlit provides a secure way to manage secrets.

1.  Create a folder named `.streamlit` in your project's root directory.

2.  Inside the `.streamlit` folder, create a file named `secrets.toml`.

3.  Add your API key to this file in the following format:

    ```
    GEMINI_API_KEY = "your_api_key_here"

    ```

Alternatively, you can set it as an environment variable in your deployment environment.

### 5\. Running the Application

To run the app locally, navigate to your project directory in the terminal and execute the following command:

```
streamlit run app.py

```

The application will open in your web browser.

### 6\. Deployment on Streamlit Community Cloud

This app is ready for deployment on the Streamlit Community Cloud.

1.  Push your code to a public GitHub repository.

2.  Go to the Streamlit Community Cloud dashboard.

3.  Click "New app" and connect it to your GitHub repository.

4.  Configure your repository, branch, and file path.

5.  Add your `GEMINI_API_KEY` to the app's secrets in the advanced settings.

6.  Click "Deploy!"

Enjoy your content analysis!
