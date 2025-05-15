#!/bin/bash
set -e  # Exit immediately on error

# Default paths
BACKEND_ENV_PATH="./backend/api/.env.deploy"
FRONTEND_ENV_PATH="./web/.env.deploy"
RESTART_PODS=false

# Parse flags
for arg in "$@"; do
  case $arg in
    --back_env=*)
      BACKEND_ENV_PATH="${arg#*=}"
      shift
      ;;
    --front_env=*)
      FRONTEND_ENV_PATH="${arg#*=}"
      shift
      ;;
    --restart)
      RESTART_PODS=true
      shift
      ;;
    *)
      echo "❌ Unknown argument: $arg"
      echo "Usage: ./deploy.sh [--back_env=PATH] [--front_env=PATH] [--restart]"
      exit 1
      ;;
  esac
done

# Show selected config
echo "🛠️  Deployment configuration:"
echo "  📄 Backend env:  $BACKEND_ENV_PATH"
echo "  📄 Frontend env: $FRONTEND_ENV_PATH"
echo "  🔁 Restart pods: $RESTART_PODS"
echo ""

echo "🐳 Enabling Docker inside Minikube..."
eval $(minikube docker-env)

# Generate unique temporary env file for frontend
TIMESTAMP=$(date +%s)
FRONTEND_ENV_BASENAME="temp_env_$TIMESTAMP"
TEMP_ENV_PATH="./web/$FRONTEND_ENV_BASENAME"

echo "📝 Copying frontend env to $TEMP_ENV_PATH..."
cp "$FRONTEND_ENV_PATH" "$TEMP_ENV_PATH"

echo "🔨 Building Docker images..."
docker build --no-cache -t backend:local --build-arg ENV_FILE="${BACKEND_ENV_PATH}" ./backend
docker build --no-cache -t frontend:local --build-arg ENV_FILE="$FRONTEND_ENV_BASENAME" ./web

# Cleanup temporary env file after build
rm "$TEMP_ENV_PATH"

echo "🧹 Deleting previous ConfigMaps..."
kubectl delete configmap backend-env frontend-env --ignore-not-found

echo "🧩 Creating new ConfigMaps from .env files..."
kubectl create configmap backend-env --from-env-file="$BACKEND_ENV_PATH"
kubectl create configmap frontend-env --from-env-file="$FRONTEND_ENV_PATH"

echo "📦 Applying Kubernetes manifests..."
kubectl apply -f k8s/backend.yaml
kubectl apply -f k8s/frontend.yaml

if [ "$RESTART_PODS" = true ]; then
  echo "🔥 Restarting pods..."
  kubectl delete pod -l app=frontend --ignore-not-found
  kubectl delete pod -l app=backend --ignore-not-found
fi

echo "✅ Deployment completed."

echo ""
echo "🌐 To access the services, run the following in another terminal:"
echo "▶️  minikube service frontend-service"
echo "▶️  minikube service backend-service"
