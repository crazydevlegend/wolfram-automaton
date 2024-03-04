import requests
from dotenv import load_dotenv
import os


# Retrieve API key from environment variables
api_key = os.getenv('WOLFRAM_APP_ID')


def generate_cellular_automaton(rule_number, steps, api_key):
    """
    Generates a cellular automaton using the Wolfram API.

    Parameters:
    - rule_number: An integer representing the rule number for the cellular automaton.
    - steps: An integer representing the number of steps to generate.
    - api_key: Your Wolfram API key as a string.

    Returns:
    - The result of the cellular automaton generation as a string.
    """
    # Construct the query URL
    query_url = f"http://api.wolframalpha.com/v2/query?input=Rule{rule_number}%20cellular%20automaton%20{steps}%20steps&format=plaintext&output=JSON&appid={api_key}"

    # Make the request to the Wolfram API
    response = requests.get(query_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the cellular automaton result
        # Note: The path to the result might vary based on the API response structure
        result = data['queryresult']['pods'][1]['subpods'][0]['plaintext']
        return result
    else:
        return "Failed to retrieve data from Wolfram API."

rule_number = 30  # Example rule number
steps = 50  # Example number of steps
print(generate_cellular_automaton(rule_number, steps, api_key))