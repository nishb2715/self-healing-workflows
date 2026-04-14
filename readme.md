# 🚀 Self-Healing Workflows System

## 📌 Overview
This project implements a **self-healing workflow system** that can automatically detect, diagnose, recover, and validate failures in automated pipelines.

It combines **rule-based logic + AI-based reasoning** to build a resilient system that minimizes manual intervention.

---

## 🎯 Features

### 🔹 1. API Failure Handling
- Retry mechanism with exponential backoff
- Automatic fallback to backup API
- Output validation

---

### 🔹 2. Schema Mismatch Detection
- Detects incorrect data fields
- Automatically maps incorrect schema to expected schema
- Continues processing without failure

---

### 🔹 3. AI Hallucination Detection
- Uses a real LLM (Groq) to generate responses
- Validates output using rule-based checks
- Automatically corrects incorrect responses

---

### 🔹 4. Planner Agent
- Decides execution steps dynamically
- Controls workflow execution

---

### 🔹 5. RAG-based Learning
- Stores past failures and solutions
- Retrieves solutions for similar failures
- Improves system performance over time

---

### 🔹 6. Observability Dashboard
- Built using Streamlit
- Displays:
  - System metrics
  - Workflow activity
  - Real-time logs

---

## 🏗️ System Architecture
Execution → Monitoring → Detection → Diagnosis → Recovery → Validation → Learning (RAG)

---

## ⚙️ Tech Stack

- Python 3
- Groq API (LLM)
- Streamlit (Dashboard)
- Requests (API handling)
- JSON (RAG storage)
- python-dotenv

---

## 📂 Project Structure
self-healing-workflows/
│
├── core/ # Core agents (planner, monitor, recovery, validator)
├── workflows/ # Workflow implementations
├── rag/ # Memory (RAG system)
├── observability/ # Dashboard and logs
├── utils/ # Logger and helpers
├── main.py # Entry point
├── .env # API keys
├── requirements.txt


---

## ▶️ How to Run

### 1. Activate virtual environment
self\Scripts\activate

### 2. Install dependencies
pip install -r requirements.txt


### 3. Add Groq API Key
Create `.env` file:
GROQ_API_KEY=your_api_key_here


---

### 4. Run system
python main.py


---

### 5. Run dashboard
streamlit run observability/dashboard.py


---

## 🧠 Key Concepts Used

- Self-healing systems
- Exponential backoff
- Fallback strategies
- LLM-as-a-Judge pattern
- Agent-based architecture
- Retrieval-Augmented Generation (RAG)
- Observability and logging

---

## 🚀 Future Improvements

- Integration with orchestration tools like Apache Airflow
- Advanced vector database (FAISS) for RAG
- Real-time alerting system
- Failure prediction using ML

---

## 💡 Conclusion

This project demonstrates how combining **traditional engineering techniques with AI-based reasoning** can create resilient and intelligent systems capable of handling failures autonomously.

---

## 👩‍💻 Author
Nishtha Mishra