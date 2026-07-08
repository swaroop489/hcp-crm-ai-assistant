# An AI-powered Healthcare Professional (HCP) Customer Relationship Management system

An AI-powered Customer Relationship Management (CRM) system for Healthcare Professionals (HCPs) that enables pharmaceutical sales representatives to log doctor interactions using natural language instead of manually filling forms. The application uses a LangGraph-based AI agent with Groq LLM to understand user intent, execute tools, and automatically populate the CRM interaction form.

---

## Problem Statement

Pharmaceutical field representatives interact with multiple Healthcare Professionals (HCPs) every day. After each visit, they must manually fill CRM forms containing meeting details such as doctor name, discussion topics, sentiment, materials shared, outcomes, and follow-up actions.

Manual data entry is:
- Time-consuming
- Repetitive
- Error-prone
- Difficult after multiple meetings

---

## Solution

This project introduces an **AI-First CRM** where users interact with an AI assistant through natural language.

Instead of manually filling the interaction form, users simply describe the meeting in the chat. The LangGraph agent analyzes the request, selects the appropriate tool, extracts structured information using the Groq LLM, and automatically updates the interaction form.

Example:

> "Today I met Dr. Smith. We discussed Product X, shared brochures, and the doctor showed positive interest. Schedule a follow-up in two weeks."

The AI automatically fills:
- HCP Name
- Date & Time
- Topics Discussed
- Materials Shared
- Sentiment
- Outcomes
- Follow-up Actions

---

## Features

- AI-powered interaction logging
- Automatic form population
- Natural language editing of existing interactions
- HCP information lookup
- AI-generated follow-up recommendations
- AI-generated meeting summaries
- Persistent interaction history using SQL database
- Modern React-based user interface

---

# LangGraph Tools

The LangGraph agent dynamically selects and executes tools based on user intent.

### 1. Log Interaction 

Extracts structured meeting information from natural language and populates the interaction form.

Example:

> "Today I met Dr. Smith and discussed Product X."

---

### 2. Edit Interaction 

Updates only the specified fields without modifying the remaining interaction details.

Example:

> "Actually the doctor's name is Dr. John and sentiment should be negative."

---

### 3. Search HCP

Retrieves previously stored information about a Healthcare Professional.

Returns information such as:
- Previous interactions
- Specialization
- Hospital
- Products discussed

---

### 4. Recommend Follow-up

Analyzes the latest interaction and generates intelligent follow-up recommendations.

Example:
- Schedule next visit
- Send product brochure
- Share clinical trial documents

---

### 5. Generate Interaction Summary

Creates a concise summary of the meeting for quick review and reporting.

---

# Project Architecture

```
React UI
      │
      ▼
Redux Store
      │
      ▼
FastAPI Backend
      │
      ▼
LangGraph Agent
      │
      ▼
Groq LLM (Gemma2-9B)
      │
      ▼
Tool Execution
      │
      ▼
PostgreSQL / MySQL
      │
      ▼
Updated CRM Form
```

---

# Tech Stack

## Frontend

- React
- Redux Toolkit
- Tailwind CSS
- Axios
- Google Inter Font

## Backend

- FastAPI
- Python
- SQLAlchemy
- PostgreSQL / MySQL

## AI

- LangGraph
- LangChain
- Groq API
- Gemma2-9B-It

---

# Project Structure

```
ai-first-crm-hcp/

├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── redux/
│   │   ├── services/
│   │   ├── pages/
│   │   └── App.jsx
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── database/
│   │   ├── models/
│   │   ├── services/
│   │   ├── schemas/
│   │   └── main.py
│   └── requirements.txt
│
├── README.md
└── screenshots/
```

---

# Workflow

1. User enters a natural language prompt in the AI Assistant.
2. FastAPI sends the prompt to the LangGraph agent.
3. LangGraph identifies the user's intent.
4. The appropriate tool is selected.
5. Groq LLM extracts structured information.
6. The database is updated.
7. Redux updates the interaction form automatically.
8. The updated form is displayed to the user.

---

# Installation

## Frontend

```bash
cd frontend

npm install

npm run dev
```

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

# Future Enhancements

- Voice note transcription
- OCR support for business cards
- Calendar integration
- Email follow-up generation
- Analytics dashboard
- Multi-user authentication
- Interaction history search

---
