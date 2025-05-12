# ML Full Stack Engineer Challenge

## Overview

This project consists of building a simple full stack application that includes:

- A **REST API** built with **Python (FastAPI)**.
- A **frontend interface** developed with **Vue.js**.

The goal is to demonstrate your skills in backend development, API design, and creating a functional frontend to consume the service.

---

## Features

### REST API

The API provides two main endpoints:

1. **Fixed translation of "Hello. How are you?"**
   - Translates this specific sentence into one of the following languages:
     - Spanish
     - German
     - French
     - Italian
     - Danish
   - If a different sentence or unsupported language is provided, the API should return an error.

2. **Translation to Jeringoza**
   - Accepts any text input and returns its translation into [Jeringoza](https://en.wikipedia.org/wiki/Jeringonza).

---

### Frontend UI

A simple user interface is required for the first endpoint, including the following features:

- A text input field for entering the message to translate.
- A dropdown menu listing the supported target languages.
- Automatic translation triggered 1 second after the user stops typing.
- Display of the translated result in a dedicated area.

> 💡 Design and styling can be minimal — visual polish is not the focus of this challenge.
