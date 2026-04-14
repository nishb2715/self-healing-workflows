class PlannerAgent:
    def __init__(self):
        pass

    def create_plan(self, failure_type):
        plans = {
            "api_failure": [
                "retry",
                "fallback_api",
                "validate"
            ],
            "schema_mismatch": [
                "detect_schema",
                "llm_remap",
                "validate"
            ],
            "ai_hallucination": [
                "generate",
                "validate",
                "re_prompt"
            ]
        }

        return plans.get(failure_type, [])