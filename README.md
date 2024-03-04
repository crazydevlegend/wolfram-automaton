# Cellular Automaton Generator

This repository contains a Python script for generating cellular automata using the Wolfram Alpha API. It demonstrates how to programmatically access and utilize the Wolfram Alpha API to create complex cellular automaton patterns based on specified rules and steps.

## Features

- **Generate Cellular Automata**: Create cellular automata patterns by specifying a rule number and the number of steps to generate.
- **Wolfram Alpha API Integration**: Utilizes the Wolfram Alpha API to compute cellular automata, showcasing how to interact with external APIs in Python.
- **Environment Variable Support**: Safely stores and accesses the Wolfram Alpha API key using environment variables.
- **Command Line Arguments**: Allows users to specify the rule number and the number of steps for the automaton generation through command line arguments.

## Prerequisites

Before you can run the script, you need to have the following:

- Python 3.x installed on your system.
- A valid Wolfram Alpha API key. You can obtain one by signing up at [Wolfram Alpha Developer](https://developer.wolframalpha.com/portal/myapps/).

## Installation

1. Clone this repository to your local machine using:
```bash
git clone https://github.com/crazydevlegend/wolfram-automaton.git
```

2. Navigate into the project directory:
```bash
cd wolfram-automaton
```

3. Install the required Python packages:
```bash
pip install -r requirements.txt
```


## Configuration

1. Create a `.env` file in the root directory of the project.
2. Add your Wolfram Alpha API key to the `.env` file as follows:

```plaintext
WOLFRAM_APP_ID=your-api-key
```

   Replace `your-api-key` with your actual API key.

## Usage

To generate a cellular automaton, run the `main.py` script with Python:
```bash
python main.py --rule_number <rule_number> --steps <steps>
```
- `--rule_number`: The rule number for the cellular automaton (e.g., 30).
- `--steps`: The number of steps to generate for the automaton (e.g., 50).

By default, if no arguments are provided, the script generates a cellular automaton using Rule 30 with 50 steps.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.