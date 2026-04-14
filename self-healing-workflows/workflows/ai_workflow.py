from groq import Groq
import os
from dotenv import load_dotenv
from utils.logger import log_event

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_response():
    log_event("AI", "START", "Generating response from LLM")

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "What is the capital of India?"}
        ]
    )

    return completion.choices[0].message.content


def validate_response(response):
    if "New Delhi" in response:
        return True
    return False


def run_ai_workflow():
    response = generate_response()
    log_event("AI", "GENERATED", response)

    if not validate_response(response):
        log_event("AI", "HALLUCINATION", "Incorrect response detected")

        corrected = "The capital of India is New Delhi"
        log_event("AI", "CORRECTED", corrected)

        return corrected

    log_event("AI", "SUCCESS", "Response is valid")
    return response