# Translation API

This project is a simple translation API built with **FastAPI**. It includes a RESTful interface for text translation and a basic frontend (located in the `./web` folder, not covered here).

All backend code is located in the `./backend` directory.

## 🚀 Features

- Translate a fixed phrase ("Hello. How are you?") into five languages.
- Translate any input text into *Jeringoza*.
- Simple FastAPI server ready for development.

## ✅ Prerequisites

Before running the project, ensure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/) – dependency and virtual environment manager

Install `uv` globally via pip:

```bash
pip install uv
```

## 📦 Installation

From the `./backend` directory:

### 1. Sync dependencies using `uv`

This will create and populate a `.venv` environment automatically:

```bash
uv sync
```

### 2. Activate the virtual environment

```bash
source .venv/bin/activate
```

## 🧪 Running the API in Development Mode

With the virtual environment activated, start the development server:

```bash
fastapi dev api/main.py
```

This will launch the FastAPI app with automatic reload on file changes.