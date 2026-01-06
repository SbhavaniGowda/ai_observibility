from flask import Flask, request, jsonify
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from ai_engine import AIEngine
import prometheus_metrics as pm
import time
import random

app = Flask(__name__)
engine = AIEngine()

# Simulate background metric updates
@app.before_request
def update_gauges():
    # Simulate reading from hardware sensors
    current_gpu = random.uniform(20, 100)
    current_temp = random.uniform(40, 95)
    pm.GPU_UTILIZATION.set(current_gpu)
    pm.GPU_TEMPERATURE.set(current_temp)

@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()
    pm.PREDICTION_REQUESTS.inc()
    
    data = request.json
    gpu = data.get('gpu_util', 50)
    temp = data.get('temp', 60)
    
    is_anomaly, score, cause = engine.predict(gpu, temp)
    
    if is_anomaly:
        pm.ANOMALY_DETECTED.labels(root_cause=cause).inc()
    
    pm.INFERENCE_TIME.observe(time.time() - start_time)
    
    return jsonify({
        "anomaly": is_anomaly,
        "score": score,
        "root_cause": cause
    })

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    engine.train_mock_model()
    app.run(host='0.0.0.0', port=5000)
