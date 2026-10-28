# Local LLM Assistant

**A lightweight, locally hosted AI assistant built with Python, Ollama, and IBM Granite 3.3.**

A command-line application for interacting with a Large Language Model (LLM), analyzing text-based context, and experimenting with prompt configuration — without relying on cloud inference APIs.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-222222)
![IBM Granite](https://img.shields.io/badge/IBM-Granite_3.3-6929C4)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

This project explores how to integrate a locally running LLM into a Python application using the Ollama Python library.

The assistant provides a simple interactive menu where users can load text files, configure prompts, submit queries, and receive AI-generated responses.

It was initially developed as a practical exercise in Python and Generative AI, with additional functionality to improve usability and explore local AI inference.

### Project objectives

- Understand how Python communicates with a locally hosted LLM.
- Explore the role of system prompts, user prompts, and temperature.
- Incorporate external text as contextual information.
- Practice file handling, error management, and modular programming.
- Build a foundation for future LLM-powered applications.

---

## Features

| Feature | Description |
|---|---|
| Local LLM inference | Run IBM Granite through Ollama |
| Interactive CLI | Navigate the application using a terminal menu |
| Context loading | Import UTF-8 `.txt` files |
| Custom prompts | Modify system and user instructions |
| Temperature control | Adjust the model's response variability |
| Response logging | Save queries and responses locally |
| Error handling | Handle missing files and common execution errors |

## Tech Stack

**Language:** Python 3.10+

**LLM runtime:** Ollama

**Language model:** IBM Granite 3.3 2B Instruct (Q4_K_M)

**Python library:** `ollama`

**Interface:** Command-line interface (CLI)

---

## Project Structure

```text
local-llm-assistant/
├── main.py
├── contexto.txt
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

The application can also generate a local `historial.txt` file to store queries and responses. This file is excluded from version control.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sppgg/local-llm-assistant.git
cd local-llm-assistant
```

Alternatively, download the repository as a ZIP file from GitHub.

### 2. Install Ollama

Download and install Ollama:

https://ollama.com/download

Make sure the Ollama service is running.

### 3. Download the language model

```bash
ollama pull ibm/granite3.3:2b-instruct-q4_K_M
```

The quantized model requires approximately 1.5 GB of disk space for its download. Runtime memory requirements depend on the model configuration and context length.

### 4. Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

---

## Usage

When the application starts, the following menu appears:

```text
--- MENÚ ASISTENTE LOCAL ---

1. Cargar archivo de contexto
2. Enviar consulta al LLM
3. Modificar configuración
4. Ver configuración actual
0. Salir
```

### Example workflow

**Step 1 — Load a document**

Select option `1` and enter:

```text
contexto.txt
```

**Step 2 — Submit a query**

Select option `2` and enter a question, for example:

```text
Identify the main practical applications described in the document.
```

**Step 3 — Review the response**

The assistant sends the prompt and document context to Granite through Ollama.

The generated answer is displayed in the terminal.

**Step 4 — Explore prompt configuration**

Use option `3` to modify the system prompt, user prompt, or temperature.

---

## How It Works

The application follows a straightforward inference pipeline:

```text
User
  |
  v
Python CLI
  |
  v
Load text context
  |
  v
Build system and user messages
  |
  v
Ollama Python Client
  |
  v
IBM Granite 3.3 (Local Inference)
  |
  v
Generated Response
  |
  +--> Terminal output
  |
  +--> Local response history
```

### Key components

**`leer_contexto()`**

Reads text files using UTF-8 encoding and handles file-related errors.

**`consultar_ollama()`**

Builds the messages, communicates with Ollama, and retrieves the model-generated response.

**`main()`**

Manages the interactive menu, application configuration, and user input.

### Model configuration

```python
{
    "modelo": "ibm/granite3.3:2b-instruct-q4_K_M",
    "temperatura": 0.2,
    "num_ctx": 8192
}
```

A low temperature encourages more predictable output, while the context window determines the maximum number of tokens available during inference.

---

## Local Inference and Privacy

The model runs locally through Ollama, allowing prompts and responses to be processed without sending them to an external LLM inference API.

An internet connection is required for the initial installation and model download.

Local execution does not automatically guarantee complete system security or privacy. Users should still review logs, file access, and any sensitive information included in documents.

---

## Limitations

This is an educational prototype rather than a production-ready assistant.

- Text context is included directly in the prompt.
- The application does not implement a vector database or Retrieval-Augmented Generation (RAG).
- Context size is limited by the model's available context window.
- The model may generate inaccurate or incomplete responses.
- Conversation history is not automatically reused as model memory.
- The interface is currently terminal-based.

---

## Future Improvements

Potential extensions include:

- Persistent conversation memory.
- Support for PDF and additional document formats.
- Semantic document retrieval using embeddings.
- RAG integration for larger document collections.
- A lightweight web interface using Streamlit.
- Automated response evaluation and testing.

---

## Learning Outcomes

This project provided hands-on experience with:

- Python application structure and functions.
- Local LLM deployment.
- Model inference through a Python client.
- Prompt construction and configuration.
- Context-based question answering.
- File handling and response logging.
- Understanding the limitations of small local language models.

---

## Author

**Sara P. | Applied AI · Python · Geospatial Technologies**

[GitHub Profile](https://github.com/Sppgg)

*Built as part of a practical Python and Generative AI learning project.*

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
