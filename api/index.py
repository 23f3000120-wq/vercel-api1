from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestBody(BaseModel):
    regions: list
    threshold_ms: float

@app.post("/")
def compute(payload: RequestBody):
    result = {}

    for region in payload.regions:
        data = np.random.rand(100) * 200

        result[region] = {
            "avg_latency": float(np.mean(data)),
            "p95_latency": float(np.percentile(data, 95)),
            "avg_uptime": float(np.random.rand()),
            "breaches": int(np.sum(data > payload.threshold_ms))
        }

    return result
