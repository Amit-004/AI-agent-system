import json
from fastapi import FastAPI
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse

from src.safety import check
from src.core.classifier import classify
from src.agents.portfolio_health import run as portfolio_health_run


app = FastAPI(title="AI Microservice")


class QueryRequest(BaseModel):
    query: str
    user: dict = {}
    session_id: str | None = None


async def stream_response(request: QueryRequest):
    try:
        safety = check(request.query)

        if safety.blocked:
            yield {
                "event": "safety_block",
                "data": json.dumps({
                    "blocked": True,
                    "message": safety.message
                })
            }
            return

        result = classify(request.query)

        yield {
            "event": "classification",
            "data": json.dumps({
                "agent": result.agent,
                "entities": result.entities
            })
        }

        if result.agent == "portfolio_health":
            response = portfolio_health_run(request.user)
        else:
            response = {
                "agent": result.agent,
                "entities": result.entities,
                "message": f"{result.agent} agent is not implemented in this build."
            }

        yield {
            "event": "response",
            "data": json.dumps(response)
        }

        yield {
            "event": "done",
            "data": json.dumps({"status": "completed"})
        }

    except Exception as e:
        yield {
            "event": "error",
            "data": json.dumps({"message": str(e)})
        }


@app.post("/query")
async def query(request: QueryRequest):
    return EventSourceResponse(stream_response(request))