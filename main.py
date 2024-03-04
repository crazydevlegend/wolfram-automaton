import requests
from dotenv import load_dotenv
import os
import argparse
import matplotlib.pyplot as plt
import numpy as np
import json

# Load environment variables
load_dotenv()

# Retrieve API key from environment variables
api_key = os.getenv('WOLFRAM_APP_ID')
print(api_key)

def generate_cellular_automaton(rule_number, steps, api_key):
    """
    Generates a cellular automaton using the Wolfram API.

    Parameters:
    - rule_number: An integer representing the rule number for the cellular automaton.
    - steps: An integer representing the number of steps to generate.
    - api_key: Your Wolfram API key as a string.

    Returns:
    - The result of the cellular automaton generation as a 2D list.
    """
    # Construct the query URL
    query_url = f"http://api.wolframalpha.com/v2/query?input=Rule{rule_number}%20cellular%20automaton%20{steps}%20steps&format=plaintext&output=JSON&appid={api_key}"

    # Make the request to the Wolfram API
    response = requests.get(query_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Find the "Evolution result" pod
        evolution_result_pod = next((pod for pod in data['queryresult']['pods'] if pod['id'] == 'EvolutionResult'), None)
        if evolution_result_pod:
            # Extract the plaintext content
            result = evolution_result_pod['subpods'][0]['plaintext']
            
            # Convert plaintext result to a 2D list for visualization
            lines = result.split('\n')
            # Filter out any lines that are not part of the automaton pattern
            lines = [line for line in lines if line.strip() and not line.strip().isdigit() and not 'steps' in line]
            automaton = []
            for line in lines:
                row = []
                for char in line:
                    if char == '1':
                        row.append(1)
                    elif char == '0':
                        row.append(0)
                if row:  # Ensure the row is not empty
                    automaton.append(row)
            return automaton
        else:
            print("Evolution result pod not found.")
            return None
    else:
        print("Failed to retrieve data from Wolfram API.")
        return None

def visualize_automaton(automaton):
    """
    Visualizes a cellular automaton using matplotlib.

    Parameters:
    - automaton: A 2D list representing the cellular automaton.
    """
    automaton_array = np.array(automaton)
    plt.imshow(automaton_array, cmap='Greys', interpolation='nearest')
    plt.show()

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Generate and visualize a cellular automaton using the Wolfram API.")
    
    # Add arguments
    parser.add_argument("--rule_number", type=int, default=30, help="The rule number for the cellular automaton.")
    parser.add_argument("--steps", type=int, default=50, help="The number of steps to generate.")
    
    # Parse the arguments
    args = parser.parse_args()

    automaton = generate_cellular_automaton(args.rule_number, args.steps, api_key)
    if automaton:
        print(automaton)
        visualize_automaton(automaton)
    else:
        print("Failed to generate cellular automaton.")