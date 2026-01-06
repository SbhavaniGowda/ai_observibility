#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT"

echo "🧹 Cleaning AI Observability Demo resources..."

kubectl delete namespace ai-obs --ignore-not-found

# Optional cleanup (commented on purpose)
# helm uninstall monitoring -n ai-obs
# minikube delete

echo "✅ Cleanup completed."
