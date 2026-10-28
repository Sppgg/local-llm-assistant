# Local LLM Assistant — Python & Ollama

A lightweight, command-line AI assistant built with Python and Ollama, running IBM Granite 3.3 locally.

## Overview

This project explores how to integrate a locally hosted Large Language Model (LLM) into a Python application.

The assistant allows users to load text files as context, send prompts to the model, customize instructions, and generate responses without relying on a cloud-based inference API.

Developed as a practical learning project to explore local AI inference and LLM integration.

## Features

- Local LLM inference using Ollama
- IBM Granite 3.3 2B Instruct model
- Text file loading for contextual analysis
- Configurable system and user prompts
- Adjustable temperature
- Interactive command-line menu
- Local response logging

## Tech Stack

- Python
- Ollama
- IBM Granite 3.3 2B Instruct

## Getting Started

**1. Install Ollama**

Download and install Ollama from https://ollama.com.

**2. Download the model**

```bash
ollama pull ibm/granite3.3:2b-instruct-q4_K_M
```

**3. Install Python dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Run the application**

```bash
python main.py
```

Make sure Ollama is running locally.

## How It Works

1. The user loads a UTF-8 text file.
2. Python reads the file and incorporates its contents into the prompt.
3. The application sends the request to Ollama.
4. Granite generates a response locally.
5. The response is displayed in the terminal and can be saved to a local history file.

## Limitations

This is a learning project, not a production-ready application.

- Document context is provided directly in the prompt.
- There is no vector database or semantic retrieval system.
- The assistant does not fine-tune or train the language model.
- Response quality depends on the model and available hardware.

## Project Context

Developed as part of a Python and generative AI learning exercise, with additional improvements for interactive configuration, error handling, and response logging.

## Future Improvements

- Conversation memory
- Support for additional document formats
- Document search using RAG
- Simple web interface

## Author

Sara — Applied AI, Python & Geospatial Technologies