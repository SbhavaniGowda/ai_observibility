from flask import Flask, request, jsonify
import time
from prometheus_client import Counter, Gauge, Histogram, generate_latest

app = Flask(__name__)

REQUESTS = Counter("ai_requests_total", "Total inference requests")
ANOMALIES = Counter("ai_anomalies_total", "Detected anomalies", ["cause"])
GPU = Gauge("ai_gpu_utilization", "GPU Utilization %")
TEMP = Gauge("ai_gpu_temperature", "GPU Temperature °C")
LATENCY = Histogram("ai_inference_latency_seconds", "Inference latency")

@app.route("/predict", methods=["POST"])
def predict():
    start = time.time()
    data = request.json or {}

    gpu = float(data.get("gpu", 40))
    temp = float(data.get("temp", 60))

    GPU.set(gpu)
    TEMP.set(temp)
    REQUESTS.inc()

    cause = None
    if gpu > 85:
        cause = "GPU Saturation"
    elif temp > 85:
        cause = "Thermal Throttling"

    if cause:
        ANOMALIES.labels(cause=cause).inc()

    LATENCY.observe(time.time() - start)

    return jsonify({"status": "ok", "anomaly": bool(cause)})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}

app.run(host="0.0.0.0", port=5000)
