# AI Code Assistant

This repository provides a small demo of an AI powered assistant that can read,
write and execute code in a controlled working directory. The assistant uses
[Google Gemini](https://ai.google.dev/) through the `google-genai` package and
communicates with the model via function calls.

The included `calculator/` folder contains a simple calculator application that
serves as a playground for the agent.

## Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`
- A `GEMINI_API_KEY` environment variable (can be placed in a `.env` file)

Install the dependencies with:

```
pip install -r requirements.txt
```

## Usage

Run the assistant by supplying a prompt describing what you would like it to do.
Verbose output is optional:

```
python main.py "<your prompt>" [--verbose]
```

Example:

```
python main.py "How do I fix the calculator?" --verbose
```

The agent will plan a sequence of function calls to inspect or modify files
under the working directory and print the final response from Gemini.

## Testing

A small test script is provided to demonstrate the helper functions. Execute it
with:

```
python tests.py
```

The calculator package also contains unit tests which can be run directly:

```
python calculator/tests.py
```
