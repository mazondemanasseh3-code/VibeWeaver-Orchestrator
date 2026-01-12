import os
from dotenv import load_dotenv
from orchestrator import Orchestrator

load_dotenv() # Loads your ANTHROPIC_API_KEY from .env

def run_orchestration():
    orchestrator = Orchestrator()
    
    # Starting a new task
    inputs = {"task": "Analyze 2026 market trends for AI agents."}
    result = orchestrator.app.invoke(inputs)
    
    print("\nFINAL RESULT:")
    print(result["final_output"])

if __name__ == "__main__":
    run_orchestration()
