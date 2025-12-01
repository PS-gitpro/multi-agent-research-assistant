import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, List
import uuid

class BaseAgent(ABC):
    """Base class for all agents in our multi-agent system"""
    
    def __init__(self, name: str):
        self.name = name
        self.agent_id = str(uuid.uuid4())[:8]
        self.logger = logging.getLogger(f"agent.{name}")
        self.logger.info(f"Initialized agent: {name} (ID: {self.agent_id})")
    
    @abstractmethod
    async def process(self, input_data: Any) -> Any:
        """Main processing method to be implemented by subclasses"""
        pass
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status information"""
        return {
            "name": self.name,
            "id": self.agent_id,
            "status": "active"
        }