from langgraph.graph import StateGraph, END
from typing import TypedDict, List

# Define the shared state that agents will update
class AgentState(TypedDict):
    task: str
    plan: List[str]
    worker_results: List[str]
    final_output: str

class Orchestrator:
    def __init__(self):
        # Initialize the graph
        self.workflow = StateGraph(AgentState)
        
        # Add nodes (The "Manager" and "Workers")
        self.workflow.add_node("planner", self.plan_tasks)
        self.workflow.add_node("researcher", self.research_node)
        self.workflow.add_node("writer", self.writer_node)
        
        # Define the flow
        self.workflow.set_entry_point("planner")
        self.workflow.add_edge("planner", "researcher")
        self.workflow.add_edge("researcher", "writer")
        self.workflow.add_edge("writer", END)
        
        self.app = self.workflow.compile()

    def plan_tasks(self, state: AgentState):
        print("---PLANNING PHASE---")
        return {"plan": ["Find data", "Summarize findings"]}

    def research_node(self, state: AgentState):
        print("---RESEARCHING---")
        return {"worker_results": ["Research data points found..."]}

    def writer_node(self, state: AgentState):
        print("---WRITING FINAL OUTPUT---")
        return {"final_output": "The finalized enterprise report."}
