from flight_call_support.crew import FlightCallAgent
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    
    try:
        FlightCallAgent().crew().kickoff(inputs={"user_query": "Find me a flight from Ahmedabad to Hyderabad on 2023-09-10"})
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")