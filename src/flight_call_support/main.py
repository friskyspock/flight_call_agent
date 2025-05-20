from flight_call_support.crew import FlightCallAgent
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'origin': "Ahmedabad",
        'destination': "Hyderabad",
        'date': "2023-09-10"
    }
    
    try:
        FlightCallAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")