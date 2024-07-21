from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq

@CrewBase
class FinancialAnalystCrew():
    """FinancialAnalystCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self)-> None:
        self.groq_llm = ChatGroq(temperature=0, model_name='mixtral-8x7b-32768')