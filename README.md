
# Valura AI Microservice — Assignment

## Overview

This project implements a simplified version of Valura’s AI microservice — an intelligence layer designed to act as a co-investor for users. The system processes financial queries, ensures safety, classifies intent, routes to the correct agent, and streams responses back to the user using Server-Sent Events (SSE).

---

## Architecture

The request pipeline follows:

User Query → Safety Guard → Intent Classifier → Agent Router → Response (SSE)

### Components

1. Safety Guard  
- Runs first (no LLM, no network)  
- Blocks harmful financial queries such as insider trading, market manipulation, money laundering, guaranteed returns, and reckless advice  
- Returns category-specific responses  

2. Intent Classifier  
- Rule-based classifier (LLM-free for testability)  
- Routes queries to agents like portfolio_health, market_research, investment_strategy, financial_planning, risk_assessment  
- Extracts entities like tickers  

3. Portfolio Health Agent  
- Fully implemented agent  
- Computes concentration risk, performance (mocked), benchmark comparison (mocked)  
- Provides beginner-friendly insights  
- Handles empty portfolios gracefully  

4. HTTP Layer (FastAPI)  
- Endpoint: `/query`  
- Uses Server-Sent Events (SSE)  
- Events: classification, response, done  

# Valura AI — Team Lead Project Assignment

You have been given access to this repository as part of the Valura AI team lead hiring process.

**Read [`ASSIGNMENT.md`](ASSIGNMENT.md) in full before writing a single line of code.**

---

## What you're building

An AI agent ecosystem that helps a novice investor **build, monitor, grow, and protect** their portfolio. See [`ASSIGNMENT.md`](ASSIGNMENT.md) for the full mission, scope, and constraints.


## Setup
Requirements: Python 3.11+

Installation:

git clone <repo-url>  
cd <repo-name>  

python -m venv venv  

Windows:  
venv\Scripts\activate  

macOS/Linux:  
source venv/bin/activate  

pip install -r requirements.txt  

---

## Run Tests

python -m pytest -v  

Expected output:  
7 passed  

---

## Run Server

python -m uvicorn src.main:app --reload  

Open in browser:  
http://127.0.0.1:8000/docs  

---

## Example Request

{
  "query": "how is my portfolio doing",
  "user": {
    "portfolio": [
      {"ticker": "NVDA", "value": 60000},
      {"ticker": "AAPL", "value": 20000},
      {"ticker": "MSFT", "value": 20000}
    ]
  }
}

---

## Streaming Output (SSE)

event: classification  
event: response  
event: done  

---




## Video Walkthrough

(video link here)


https://drive.google.com/file/d/1VzPR_MlcRdTNMkByeXUFl7iUBcOaBIGS/view?usp=sharing


---


**Requirements:** Python 3.11+, an OpenAI API key.



```bash
git clone <your-classroom-repo-url>
cd <repo-name>

python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

pip install -r requirements.txt

cp .env.example .env
# Fill in OPENAI_API_KEY
```

Use `gpt-4o-mini` while developing to keep costs down. Evaluation runs against `gpt-4.1`.

---

## Running Tests

```bash
pytest tests/ -v
```

Tests must pass without an `OPENAI_API_KEY` set — mock the LLM. We will run `pytest tests/ -v` on your repo.

---

## Repository Structure

When you submit, your repository must contain:

```
README.md   ← overwrite this with your own (setup, decisions, library choices, video link)
src/        ← all code
tests/      ← all tests, must pass with pytest
```

`fixtures/`, `pytest.ini`, `requirements.txt`, `.env.example`, and `.github/` are part of the scaffold — leave them in place. Do not delete `ASSIGNMENT.md`.

---

## Submission

- Push commits **throughout** your work — we read the git log
- Your `README.md` must:
  - Explain how to run your code
  - List every required environment variable
  - Document the non-obvious decisions you made
  - Link your defence video (≤ 10 min — see `ASSIGNMENT.md`)
- Deadline: **3 days** from the date you accepted this assignment
- Defence video: due within **24 hours** of your final commit

---

## Environment

You self-host everything. We do not provide credentials. See `.env.example` for the variables you'll need.

