#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Get optional env file paths from arguments
BACKEND_ENV_PATH=${1:-./backend/api/.env.deploy}
FRONTEND_ENV_PATH=${2:-./web/.env.deploy}

echo "🐳 Enabling Docker inside Minikube..."
eval $(minikube docker-env)

echo "🔨 Building Docker images..."
docker build --no-cache -t backend:local ./backend
docker build --no-cache -t frontend:local ./web

echo "🧹 Deleting previous ConfigMaps..."
kubectl delete configmap backend-env frontend-env --ignore-not-found

echo "🧩 Creating new ConfigMaps from .env files..."
echo "📄 Backend env: $BACKEND_ENV_PATH"
kubectl create configmap backend-env --from-env-file="$BACKEND_ENV_PATH"

echo "📄 Frontend env: $FRONTEND_ENV_PATH"
kubectl create configmap frontend-env --from-env-file="$FRONTEND_ENV_PATH"

echo "📦 Applying Kubernetes manifests..."
kubectl apply -f k8s/backend.yaml
kubectl apply -f k8s/frontend.yaml

echo "✅ Deployment completed."

echo ""
echo "🌐 To access the services, run the following in another terminal:"
echo "▶️  minikube service frontend-service"
echo "▶️  minikube service backend-service"
