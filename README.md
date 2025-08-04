# GenMail-Generative-AI-for-email-personalization

# 📩 Cold Email Generator – End-to-End LLM & GenAI Project

## Overview
The **Cold Email Generator** is an end-to-end **LLM & GenAI** tool that helps software and AI services companies automatically generate **personalized cold emails** for potential clients in seconds.  

It uses **`meta-llama/llama-4-scout-17b-16e-instruct`** via **Groq API** for fast inference, **ChromaDB** as a vector database to store portfolio data, and **LangChain** for building AI-powered workflows. The tool comes with a **Streamlit-based UI** for ease of use.

---

## Features
- **URL-based job scraping** – Paste a job posting link, and the tool will automatically extract the role, skills, and description.
- **Portfolio integration** – Matches job requirements with your personal projects stored in **ChromaDB**.
- **Personalized cold email generation** – Generates tailored cold emails in seconds.
- **End-to-end workflow** – From job scraping → context retrieval → email generation → ready-to-send format.
- **Interactive UI** – Built with **Streamlit** for quick and easy usage.

---

## Tech Stack
- **[meta-llama/llama-4-scout-17b-16e-instruct](https://huggingface.co/meta-llama/llama-4-scout-17b-16e-instruct)** – Large language model for text generation
- **[Groq API](https://groq.com/)** – Ultra-fast LLM inference
- **[LangChain](https://www.langchain.com/)** – AI workflow orchestration
- **[ChromaDB](https://www.trychroma.com/)** – Vector database for storing and retrieving portfolio/project data
- **[Streamlit](https://streamlit.io/)** – Web UI framework
- **Python** – Core language
---

## 📂 Project Structure
```bash
ColdEmailGenerator/
│
├── app/                     # Streamlit app scripts
├── chains.py                # LangChain workflows
├── main.py                  # Main entry point
├── portfolio.py              # Portfolio/project data loader
├── utils.py                  # Helper functions
├── resource/                # Additional resources
├── vectorstore/             # ChromaDB persistent storage
├── .env                     # Environment variables
└── README.md                # Project documentation
