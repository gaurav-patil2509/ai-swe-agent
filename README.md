# AI Software Engineer Agent

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
cp .env.example .env            # then edit .env with your real LLM_API_KEY
```

## Run

```bash
uvicorn app.main:app --reload
```

Visit:
- http://127.0.0.1:8000/api/v1/health
- http://127.0.0.1:8000/docs  (auto-generated OpenAPI docs)
