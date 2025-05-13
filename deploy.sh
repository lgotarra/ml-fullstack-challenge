#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "🐳 Enabling Docker inside Minikube..."
eval $(minikube docker-env)

echo "🔨 Building Docker images..."
docker build --no-cache -t backend:local ./backend
docker build --no-cache -t frontend:local ./web

echo "🧹 Deleting previous ConfigMaps..."
kubectl delete configmap backend-env frontend-env --ignore-not-found

echo "🧩 Creating new ConfigMaps from .env files..."
kubectl create configmap backend-env --from-env-file=./backend/api/.env.deploy
kubectl create configmap frontend-env --from-env-file=./web/.env.deploy

echo "📦 Applying Kubernetes manifests..."
kubectl apply -f k8s/backend.yaml
kubectl apply -f k8s/frontend.yaml

echo "✅ Deployment completed."

echo ""
echo "🌐 To access the services, run the following in another terminal:"
echo "▶️  minikube service frontend-service"
echo "▶️  minikube service backend-service"
