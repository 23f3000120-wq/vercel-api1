import json
import numpy as np

def handler(request):
    data = request.get_json()

    regions = data["regions"]
    threshold = data["threshold_ms"]

    result = {}

    for r in regions:
        values = np.random.rand(100) * 200

        result[r] = {
            "avg_latency": float(np.mean(values)),
            "p95_latency": float(np.percentile(values, 95)),
            "avg_uptime": float(np.random.rand()),
            "breaches": int(np.sum(values > threshold))
        }

    return json.dumps(result)
