from groq import Groq
from config import GROQ_API_KEY
from workflows.monitor import log_info, log_error

client = Groq(api_key=GROQ_API_KEY)

QUESTION = "What is the capital of Australia?"
WRONG_ANSWER_TRIGGER = True

def agent_answer(question, strict=False):
    system = "You are a geography assistant. Answer in one word only." if strict else "You are a helpful assistant."
    if not strict and WRONG_ANSWER_TRIGGER:
        return "Sydney"
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        max_tokens=64,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content.strip()

def validator_agent(question, answer):
    prompt = f"""Is '{answer}' the correct answer to: '{question}'?
Reply ONLY with YES or NO."""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        max_tokens=10,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip().upper().rstrip(".")

def run():
    log_info("=== Scenario: Agent Hallucination ===")
    answer = agent_answer(QUESTION, strict=False)
    log_info(f"Agent answered: {answer}")
    verdict = validator_agent(QUESTION, answer)
    log_info(f"Validator verdict: {verdict}")
    if verdict != "YES":
        log_error("Hallucination detected. Re-prompting with strict agent...")
        corrected = agent_answer(QUESTION, strict=True)
        log_info(f"Corrected answer: {corrected}")
    else:
        log_info("Answer validated.")

if __name__ == "__main__":
    run()