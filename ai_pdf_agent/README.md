AI PDF Agent for Question Answering and Slack Integration

Project Overview
This project is an AI-powered agent that extracts text from PDF documents, processes questions, and answers them using OpenAI's `gpt-4o-mini` model. The agent can post the results to a specified Slack channel, making it easy for teams to access information quickly.

Features
- PDF Text Extraction: Extracts text content from PDF files for analysis.
- Question Answering: Processes user-provided questions to find exact or contextual answers.
- Slack Integration: Posts the results directly to a specified Slack channel.
- Modular Design: Code structured for maintainability and scalability.

Project Structure
```
ai_pdf_agent/
│
├── main.py                 Main script to run the application
├── pdf_extractor.py        Module for extracting text from PDFs
├── question_processor.py   Module for processing and finding answers to questions
├── llm_query.py            Module for querying the OpenAI LLM
├── slack_integration.py    Module for posting results to Slack
├── .env                    File for storing environment variables (API keys, etc.)
├── README.md               Project documentation
└── requirements.txt        List of dependencies
```
Setup Instructions
1. Prerequisites
- Python 3.7 or higher installed on your system.
- An active OpenAI account with an API key.
- A Slack account and workspace with a Slack app configured.

2. Create and Activate a Virtual Environment
Open your Command Prompt or PowerShell and run the following commands:
```
python -m venv venv
venv\Scripts\activate
```

3. Install Dependencies
Ensure you are in the `ai_pdf_agent` directory and run:
```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

4. Configure Environment Variables
Create a `.env` file in the project root and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key
SLACK_TOKEN=your_slack_token
```

5. Running the Project
Run the `main.py` script to start the program:
```
python main.py
```
Usage
1. Place your PDF file in the project directory.
2. Modify `main.py` to specify the PDF path, questions, and Slack channel.
3. Run the script, and the agent will extract text, answer questions, and post results to Slack.

Example Workflow
1. The user provides a PDF document and a list of questions.
2. The agent extracts text from the PDF and searches for answers.
3. If an exact answer is found, it is returned; otherwise, OpenAI's `gpt-4o-mini` model is used to generate contextual answers.
4. The results are formatted and posted to the specified Slack channel.
Modules Explanation
 `pdf_extractor.py`
Extracts text from PDF files using `pdfplumber`.

 `question_processor.py`
Processes questions using simple keyword matching and NLP techniques with `spaCy`.

 `llm_query.py`
Queries the OpenAI LLM for answers when exact matches are not found.

 `slack_integration.py`
Uses `slack_sdk` to post results to Slack in a formatted message.
Enhancements and Future Work
- Confidence Scoring: Implement a confidence threshold for OpenAI-generated answers.
- Parallel Processing: Add concurrency for processing large PDF files.
- Web Interface: Create a web-based frontend for easier use.
Troubleshooting
- Ensure your `.env` file is correctly configured and not committed to version control.
- Check if the Slack bot is added to the desired channel.
- Verify that the Python virtual environment is activated.
Security Notes
- API keys should be kept secure and never committed to version control. Use `.gitignore` to exclude the `.env` file.
- Rotate your keys periodically to maintain security.
License
This project is licensed under the MIT License. See the `LICENSE` file for details.
Contact
For questions or feedback, please reach out to [your_email@example.com] or create an issue in this repository.
 
