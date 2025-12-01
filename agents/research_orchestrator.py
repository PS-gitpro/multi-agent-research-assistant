from .base_agent import BaseAgent
from .search_agent import SearchAgent
from typing import Dict, Any, List
import asyncio
import uuid

class ResearchOrchestrator(BaseAgent):
    """Master agent that coordinates research workflow"""
    
    def __init__(self):
        super().__init__("research_orchestrator")
        self.research_sessions = {}
        self.search_agent = SearchAgent()
    
    async def process(self, query: str) -> Dict[str, Any]:
        """Process a research query using multiple agents"""
        self.logger.info(f"Processing research query: {query}")
        
        # Create research session
        session_id = str(uuid.uuid4())[:8]
        research_session = {
            "session_id": session_id,
            "query": query,
            "status": "initialized",
            "agents_involved": ["search_agent"],
            "results": {}
        }
        
        self.research_sessions[session_id] = research_session
        
        # Step 1: Use Search Agent to find information
        self.logger.info("Coordinating with Search Agent...")
        search_data = {"query": query, "max_results": 3}
        search_results = await self.search_agent.process(search_data)
        
        research_session["status"] = "search_completed"
        research_session["results"]["search"] = search_results
        
        # Step 2: Prepare for analysis (we'll add Analysis Agent next)
        research_session["agents_involved"].append("analysis_agent")
        research_session["status"] = "ready_for_analysis"
        
        self.logger.info(f"Research session {session_id} completed search phase")
        self.logger.info(f"Found {search_results.get('total_found', 0)} search results")
        
        return research_session
    
    async def parallel_research(self, queries: List[str]) -> Dict[str, Any]:
        """Conduct research on multiple topics in parallel"""
        self.logger.info(f"Starting parallel research for {len(queries)} topics")
        
        tasks = [self.process(query) for query in queries]
        results = await asyncio.gather(*tasks)
        
        return {
            "research_sessions": len(queries),
            "results": {result["session_id"]: result for result in results}
        }