# Self-Healing Workflows

A modular Python system that automatically detects, diagnoses, and recovers from workflow failures using rule-based logic and LLM-powered agents.

## Architecture
Execution → Monitor → Failure Detection → AI Diagnosis → Recovery → Validation
## Scenarios

| Command | Failure Simulated | Recovery Method |
|---|---|---|
| `python main.py api` | API timeout | Exponential backoff → fallback API |
| `python main.py data` | Schema mismatch | LLM field remapper |
| `python main.py agent` | Hallucinated output | Validator agent → strict re-prompt |

## Setup

1. Clone the repo and create a virtual environment
```bash
git clone <your-repo-url>
cd self-healing-workflows
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory