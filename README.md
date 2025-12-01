**Multi-Agent Research Assistant**



**Agents Intensive Capstone Project**

A sophisticated multi-agent system that automates research workflows through coordinated AI agents and real AI integration.



**Overview**

**Problem Statement**

Researchers waste significant time on manual information gathering and synthesis. The research process is fragmented and lacks intelligent automation.



**Our Solution**

An intelligent multi-agent system that automates research workflows through agent coordination, parallel execution, and AI-powered analysis using Google Gemini.



**Architecture**



Research Orchestrator (Master Agent)

    -> Search Agent (Information Gathering)

    -> Analysis Agent (Data Processing)

    -> Memory Agent (Session Management)

    -> Gemini AI Tools (Real AI Integration)



**Agent Responsibilities**

* Research Orchestrator: Master coordinator managing sequential workflows and parallel execution
* Search Agent: Information gathering with parallel search capabilities
* Analysis Agent: Data processing and insight extraction
* Memory Agent: Session persistence and state management
* Gemini Tools: AI capabilities for research and analysis



**Features**

**Core Capabilities**

* Multi-Agent Coordination with intelligent workflow management
* Parallel Research execution for multiple simultaneous topics
* Real AI Integration using Google Gemini 2.5 Flash
* Session Management with unique IDs and persistence
* Comprehensive Logging for full system observability
* Scalable Architecture for easy extension



**Advanced Features**

* Sequential Agent Execution with orchestrated workflows
* Parallel Processing of multiple research sessions
* Intelligent Error Handling with graceful degradation
* Real-time AI Responses using Gemini 2.5
* Professional Logging for system monitoring



**Installation**

**Prerequisites**

Python 3.11 or higher

Google Gemini API key (free)



**Quick Start**

1\. Clone the repository

git clone https://github.com/your-username/multi-agent-research-assistant

cd multi-agent-research-assistant



2\. Create virtual environment

python -m venv research\_env

source research\_env/bin/activate  # Windows: research\_env\\Scripts\\activate



3\. Install dependencies

pip install -r requirements.txt



4\. Configure environment

cp .env.example .env

\# Add your Gemini API key to .env file



5\. Run the system

python main.py



**Environment Configuration**

Create .env file:



GEMINI\_API\_KEY=your\_gemini\_api\_key\_here

MAX\_SEARCH\_RESULTS=5

SESSION\_TIMEOUT=3600

LOG\_LEVEL=INFO



Get Your Free Gemini API Key

1. Visit Google AI Studio: https://aistudio.google.com/
2. Sign in with your Google account
3. Create a new API key
4. Add it to your .env file



**Usage**

**Basic Usage**



from agents.research\_orchestrator import ResearchOrchestrator



\# Initialize the system

orchestrator = ResearchOrchestrator()



\# Start a research session

research\_session = await orchestrator.process(

    "impact of AI on climate change mitigation"

)



\# Run parallel research

parallel\_results = await orchestrator.parallel\_research(\[

    "AI in renewable energy",

    "machine learning carbon capture",

    "neural networks climate prediction"

])



**Competition Requirements**

**Demonstrated Requirements**

* Multi-agent System: FULLY DEMONSTRATED (Orchestrator + Search Agent coordination)
* Sequential Agents: FULLY DEMONSTRATED (Clear workflow between agents)
* Parallel Execution: FULLY DEMONSTRATED (3+ simultaneous research sessions)
* Session Management: FULLY DEMONSTRATED (Unique session IDs and state tracking)
* Observability: FULLY DEMONSTRATED (Comprehensive logging system)
* Custom Tools: FULLY DEMONSTRATED (Gemini AI integration framework)



**Technical Details**



**Technology Stack**

* Python 3.11 - Core programming language
* Google Gemini 2.5 - AI/ML capabilities
* Asyncio - Parallel execution and async operations
* Logging - Comprehensive observability
* Pydantic - Data validation and settings management



**Key Design Patterns**

* Strategy Pattern - Different agents for different tasks
* Observer Pattern - Logging and monitoring
* Factory Pattern - Agent creation and management
* Decorator Pattern - Enhanced functionality



**Project Structure**

multi-agent-research-assistant/

├── agents/                    # Multi-agent system

│   ├── base\_agent.py         # Abstract base class

│   ├── research\_orchestrator.py # Master coordinator

│   └── search\_agent.py       # Information gathering

├── tools/                    # Custom tools and utilities

│   └── gemini\_tools.py       # Gemini AI integration

├── memory/                   # Session and state management

├── config/                   # Configuration management

│   └── settings.py           # Application settings

├── main.py                   # Application entry point

├── requirements.txt          # Dependencies

├── .env.example              # Environment template

└── README.md                 # This file



**License**

This project is licensed under the CC-BY-SA 4.0 License - see the LICENSE file for details.



**Competition Compliance**

* Open Source Initiative approved license
* Commercial use allowed
* Modifications and distributions permitted
* Attribution required



**Acknowledgments**

* Google AI for the Gemini API and Agent Development Kit
* Kaggle for hosting the Agents Intensive competition
* AI Research Community for inspiration and best practices
