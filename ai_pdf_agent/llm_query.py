import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def query_openai_model(prompt):
    """Queries the OpenAI model for answers based on context."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use gpt-3.5-turbo or gpt-4 based on your subscription
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        raise RuntimeError(f"Error querying OpenAI API: {e}")
