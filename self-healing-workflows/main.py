import sys
from scenarios import api_failure, data_pipeline, agent_failure

SCENARIOS = {
    "api": api_failure.run,
    "data": data_pipeline.run,
    "agent": agent_failure.run,
}

if __name__ == "__main__":
    scenario = sys.argv[1] if len(sys.argv) > 1 else "api"
    if scenario not in SCENARIOS:
        print(f"Unknown scenario. Choose from: {list(SCENARIOS.keys())}")
    else:
        SCENARIOS[scenario]()