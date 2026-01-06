#!/bin/bash
set -e

echo "Starting AI Observability Demo Setup..."

# 1. Start Minikube if not running
if ! minikube status | grep -q "Running"; then
  echo "Starting Minikube..."
  minikube start --memory=6000 --cpus=4
else
  echo "Minikube already running"
fi

# 2. Use Minikube Docker daemon
echo "Configuring Docker to use Minikube..."
eval $(minikube docker-env)

# 3. Build Docker images
echo "Building Docker images..."
docker build -t ai-service docker/ai-service
docker build -t mock-service docker/mock-service

# 4. Create namespace
echo "Creating namespace..."
kubectl apply -f kubernetes/namespace.yaml

# 5. Install Prometheus Operator (if not installed)
if ! helm list -n ai-obs | grep -q monitoring; then
  echo "Installing kube-prometheus-stack..."
  helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
  helm repo update

  helm install monitoring prometheus-community/kube-prometheus-stack \
    -n ai-obs \
    --create-namespace \
    -f helm/kube-prometheus-values.yaml
else
  echo "Prometheus Operator already installed"
fi

# 6. Apply application manifests
echo "Deploying application components..."
kubectl apply -f kubernetes/ai-service.yaml
kubectl apply -f kubernetes/mock-service.yaml

# 7. Apply observability CRDs
echo "Applying observability resources..."
kubectl apply -f kubernetes/alertmanager-secret.yaml
kubectl apply -f kubernetes/alertmanager.yaml
kubectl apply -f kubernetes/prometheus-rules.yaml
kubectl apply -f kubernetes/servicemonitor.yaml
kubectl apply -f kubernetes/grafana-dashboard-cm.yaml

echo "Setup complete!"
echo ""
echo "Grafana: kubectl port-forward svc/monitoring-grafana 3000:80 -n ai-obs"
echo "Prometheus: kubectl port-forward svc/monitoring-kube-prometheus-stack-prometheus 9090:9090 -n ai-obs"
