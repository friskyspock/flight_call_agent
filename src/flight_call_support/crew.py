from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from flight_call_support.llm import llm
from flight_call_support.tools.flight_apis import FetchFlightsTool, FetchFlightsToolInput

@CrewBase
class FlightCallAgent():
    """FlightCallAgent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def extraction_agent(self) -> Agent:
        return Agent(
            role="Information Extraction Agent",
            goal="Extract relevant information from the user's query",
            backstory="You're a meticulous assistant that can understand and extract key details from user queries.",
            llm=llm,
            verbose=True
        )

    @agent
    def flight_search_agent(self) -> Agent:
        return Agent(
        role="Flight Search Agent",
        goal="Help users find available flights between cities on a given date",
        backstory="You're a flight assistant that can explain and list available flight options.",
        llm=llm,
        verbose=True
    )

    @task
    def extraction_task(self):
        return Task(
            description=(
                "The user has asked the following question: {user_query}\n"
                "Extract the origin city, destination city, and date from this query."
            ),
            expected_output="JSON with keys: origin, destination, date",
            output_pydantic=FetchFlightsToolInput,
            agent=self.extraction_agent()
        )

    @task
    def flight_task(self):
        return Task(
            description=(
                "The user wants to travel from {extraction_task.origin} to {extraction_task.destination} on {extraction_task.date}.\n"
                "Use the FetchFlightsTool to get flight data and then list the available flights in a clear and readable format."
            ),
            expected_output="Formatted list of flights with airline, times, and price.",
            agent=self.flight_search_agent(),
            tools=[FetchFlightsTool()],
            context=[self.extraction_task()]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the FlightCallAgent crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
