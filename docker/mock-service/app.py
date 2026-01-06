import requests, time

while True:
    for _ in range(5):
        requests.post("http://ai-service:5001/predict", json={"gpu": 45, "temp": 60})
        time.sleep(2)
    for _ in range(3):
        requests.post("http://ai-service:5001/predict", json={"gpu": 95, "temp": 92})
        time.sleep(2)
