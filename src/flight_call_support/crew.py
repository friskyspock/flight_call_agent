from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from flight_call_support.llm import llm
from flight_call_support.tools.flight_apis import FetchFlightsTool

@CrewBase
class FlightCallAgent():
    """FlightCallAgent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

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
    def flight_task(self):
        return Task(
            description=(
                "The user wants to travel from {origin} to {destination} on {date}.\n"
                "Here is the flight data fetched from the API:\n{flight_data}\n\n"
                "Use this information to list the available flights in a clear and readable format."
            ),
            expected_output="Formatted list of flights with airline, times, and price.",
            agent=self.flight_search_agent(),
            tools=[FetchFlightsTool()]
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