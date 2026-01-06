chmod +x scripts/setup.sh
chmod +x scripts/cleanup.sh


eval $(minikube docker-env)

docker build -t ai-service docker/ai-service
docker build -t mock-service docker/mock-service

kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/ai-service.yaml
kubectl apply -f kubernetes/mock-service.yaml

kubectl apply -f kubernetes/alertmanager-secret.yaml
kubectl apply -f kubernetes/alertmanager.yaml
kubectl apply -f kubernetes/prometheus-rules.yaml
kubectl apply -f kubernetes/servicemonitor.yaml
kubectl apply -f kubernetes/grafana-dashboard-cm.yaml
