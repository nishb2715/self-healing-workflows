from core.planner_agent import PlannerAgent
from rag.rag_engine import RAGEngine
from utils.logger import log_event

from workflows.api_workflow import run_api_workflow
from workflows.schema_workflow import run_schema_workflow
from workflows.ai_workflow import run_ai_workflow


planner = PlannerAgent()
rag = RAGEngine()


def run_system(failure_type):
    print(f"\nRunning workflow for: {failure_type}")

    # Step 1: Check RAG memory
    past_solution = rag.retrieve_solution(failure_type)

    if past_solution:
        print("⚡ Using learned recovery:", past_solution)
        log_event("RAG", "USED", past_solution)

    # ✅ IMPORTANT: NO RETURN HERE

    # Step 2: Planner creates plan
    plan = planner.create_plan(failure_type)
    log_event("Planner", "CREATED", str(plan))

    # Step 3: Execute workflows
    if failure_type == "api_failure":
        log_event("SYSTEM", "START", "Executing API workflow")
        run_api_workflow()

    elif failure_type == "schema_mismatch":
        log_event("SYSTEM", "START", "Executing Schema workflow")
        run_schema_workflow()

    elif failure_type == "ai_hallucination":
        log_event("SYSTEM", "START", "Executing AI workflow")
        run_ai_workflow()

    else:
        log_event("SYSTEM", "ERROR", f"Unknown failure type: {failure_type}")
        return

    # Step 4: Store learning
    rag.store_failure(failure_type, "Recovered successfully")
    log_event("RAG", "STORED", failure_type)


if __name__ == "__main__":
    run_system("api_failure")
    run_system("schema_mismatch")
    run_system("ai_hallucination")