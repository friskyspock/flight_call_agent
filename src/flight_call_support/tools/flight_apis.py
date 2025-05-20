import requests
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class FetchFlightsToolInput(BaseModel):
    """Input schema for Fetch Flights Tool."""
    origin: str = Field(..., description="Origin city")
    destination: str = Field(..., description="Destination city")
    date: str = Field(..., description="Date of travel")

class FetchFlightsTool(BaseTool):
    name: str = "Fetch Flights"
    description: str = "Fetches flight data from an API based on the provided origin, destination, and date."
    args_schema: Type[BaseModel] = FetchFlightsToolInput

    def _run(self, origin: str, destination: str, date: str) -> str:
        url = f"http://127.0.0.1:8001/flights?origin={origin}&destination={destination}&date={date}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text  # or response.json() if your API returns structured data
            else:
                return f"API Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Request failed: {e}"

class FetchFlightStatusToolInput(BaseModel):
    """Input schema for Fetch Flight Status Tool."""
    flight_number: str = Field(..., description="Flight number")

class FetchFlightStatusTool(BaseTool):
    name: str = "Fetch Flight Status"
    description: str = "Fetches the status of a flight from an API based on the provided flight number."
    args_schema: Type[BaseModel] = FetchFlightStatusToolInput

    def _run(self, flight_number: str) -> str:
        url = f"http://127.0.0.1:8001/flight-status/{flight_number}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text  # or response.json() if your API returns structured data
            else:
                return f"API Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Request failed: {e}"