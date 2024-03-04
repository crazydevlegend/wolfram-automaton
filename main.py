import requests
from dotenv import load_dotenv
import os
import argparse

# Load environment variables
load_dotenv()

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
        result = data['queryresult']['pods'][1]['subpods'][0]['plaintext']
        return result
    else:
        return "Failed to retrieve data from Wolfram API."

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Generate a cellular automaton using the Wolfram API.")
    
    # Add arguments
    parser.add_argument("--rule_number", type=int, default=30, help="The rule number for the cellular automaton.")
    parser.add_argument("--steps", type=int, default=10, help="The number of steps to generate.")
    
    # Parse the arguments
    args = parser.parse_args()

    print(generate_cellular_automaton(args.rule_number, args.steps, api_key))