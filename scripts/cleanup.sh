#!/bin/bash
set -e

echo "Cleaning AI Observability Demo resources..."

# Delete namespace (this removes everything inside)
kubectl delete namespace ai-obs --ignore-not-found

# Optional: uninstall Prometheus Operator (uncomment if needed)
# helm uninstall monitoring -n ai-obs

# Optional: delete Minikube completely (uncomment if needed)
# minikube delete

echo "Cleanup completed."
