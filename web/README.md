# Translation Web App

This is a simple frontend built with **Vue 3** and **TypeScript**. It connects to the FastAPI backend and allows users to request translations through a single-page interface.

All frontend code is located in the `./web` directory.

## 🚀 Features

- Text input area with automatic translation trigger
- Language selector (dropdown) to choose the target language
- Real-time display of translation results
- Error handling for failed API responses

## ✅ Prerequisites

Before running the project, ensure you have the following installed:

- [Node.js 18+](https://nodejs.org/)
- [npm 9+](https://www.npmjs.com/)

## 📦 Installation

From the `./web` directory:

### 1. Install dependencies

```bash
npm install
```

## 🧪 Running the App in Development Mode

To start the local development server:

```bash
npm run dev
```
This will launch the Vue app and open it in your browser, typically at [http://localhost:5173](http://localhost:5173).

Make sure the backend is also running and accessible for API requests.

## 🔗 Backend

The corresponding FastAPI backend can be found in the `./backend` directory. Please refer to its [README](../backend/README.md) for setup instructions.