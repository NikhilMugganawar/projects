
# AI PDF Agent for Question Answering

## Project Overview
This project is an AI-powered agent that extracts text from PDF documents, processes questions, and answers them using OpenAI's `gpt-3.5-turbo` or other supported models. The agent is built using Streamlit, providing an interactive web application for users to upload PDFs, input questions, and view answers directly on the web interface.

## Features
- **PDF Text Extraction**: Extracts text content from PDF files for analysis.
- **Question Answering**: Processes user-provided questions to find exact or contextual answers.
- **Web Interface**: Allows users to interact with the application through a user-friendly web interface built with Streamlit.
- **Modular Design**: Code structured for maintainability and scalability.

## Project Structure
```
ai_pdf_agent/
│
├── app.py                # Main Streamlit application
├── pdf_extractor.py      # Module for extracting text from PDFs
├── question_processor.py # Module for processing and finding answers to questions
├── llm_query.py          # Module for querying the OpenAI LLM
├── .env                  # File for storing environment variables (API keys, etc.)
├── README.md             # Project documentation
└── requirements.txt      # List of dependencies
```

## Setup Instructions

### 1. Prerequisites
- Python 3.7 or higher installed on your system.
- An active OpenAI account with an API key.

### 2. Create and Activate a Virtual Environment
Open your Command Prompt or PowerShell and run the following commands:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
Ensure you are in the `ai_pdf_agent` directory and run:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Configure Environment Variables
Create a `.env` file in the project root and add your API keys:
```env
OPENAI_API_KEY=your_openai_api_key
```

### 5. Running the Streamlit Application
Run the Streamlit app:
```bash
streamlit run app.py
```
Access the application in your web browser at the URL provided by Streamlit.

## Usage
1. **Upload a PDF file** through the web interface.
2. **Enter your questions** in the provided text area, one question per line.
3. **Submit the form**, and the agent will extract text, answer questions, and display the results on the web page.

## Example Workflow
1. The user uploads a PDF document and enters a list of questions.
2. The agent extracts text from the PDF and searches for answers.
3. If an exact answer is found, it is returned; otherwise, OpenAI's `gpt-3.5-turbo` model is used to generate contextual answers.
4. The results are displayed on the web application.

## Modules Explanation

### `pdf_extractor.py`
Extracts text from PDF files using `pdfplumber`.

### `question_processor.py`
Processes questions using simple keyword matching and NLP techniques with `spaCy`.

### `llm_query.py`
Queries the OpenAI LLM for answers when exact matches are not found.

## Enhancements and Future Work
- **Confidence Scoring**: Implement a confidence threshold for OpenAI-generated answers.
- **Parallel Processing**: Add concurrency for processing large PDF files.
- **CLI Support**: Enhance the application to run via the command line as well.

## Troubleshooting
- Ensure your `.env` file is correctly configured and not committed to version control.
- Verify that the Python virtual environment is activated.
- Make sure your OpenAI API key is valid and has sufficient quota.

## Security Notes
- **API keys** should be kept secure and never committed to version control. Use `.gitignore` to exclude the `.env` file.
- Rotate your keys periodically to maintain security.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or feedback, please reach out to [your_email@example.com] or create an issue in this repository.
