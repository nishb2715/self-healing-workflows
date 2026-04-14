import json
from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def diagnose(failure: dict) -> dict:
    prompt = f"""
You are a workflow diagnosis agent.
A workflow step failed. Analyze and return a JSON with:
- root_cause: short explanation
- suggested_fix: one of [retry, fallback, reroute, re_prompt, abort]
- reasoning: why you chose this fix

Failure details:
Step: {failure['step']}
Error: {failure['error']}

Respond ONLY with valid JSON. No markdown.
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(response.choices[0].message.content)