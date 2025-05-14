# 🛠️ Local Kubernetes Deployment Guide

This project consists of two services:

- `backend`: Located in `./backend`, with its Dockerfile and deployment template.
- `frontend`: Located in `./web`, also with its own Dockerfile and deployment template.

Both services are deployed locally using **Minikube**, **Docker**, and **Kubernetes**.

---

## 🚀 Deployment Steps

1. **Start Minikube (if not running yet)**

    ```bash
    minikube start
    ```

2. **Deploy the stack**
    Run the provided script:

    ```bash
    ./deploy.sh
    ```

    You can optionally pass custom paths to the backend and frontend `.env` files:

    ```bash
    ./deploy.sh ./custom/backend.env ./custom/frontend.env
    ```

    This script performs the following actions:

    - Enables Docker inside the Minikube environment.
    - Builds Docker images for both backend and frontend (`backend:local` and `frontend:local`).
    - Deletes existing Kubernetes `ConfigMaps` (if any).
    - Creates new `ConfigMaps` from the corresponding `.env.deploy` files:
      - `./backend/api/.env.deploy` → used by the backend
      - `./web/.env.deploy` → used by the frontend
    - Applies the Kubernetes manifests:
      - `k8s/backend.yaml`
      - `k8s/frontend.yaml`

---

## 🌐 Accessing the Services

To access the deployed services in your browser, use:

```bash
minikube service frontend-service
minikube service backend-service
```



These commands will open the browser or show you the local URL for each service.

---

## 🔄 Redeploying a Single Service After Changes

If you make changes to either the backend or frontend and want to redeploy only that service, follow the steps below:

> ⚠️ Note: Kubernetes will not automatically restart a pod even if the local Docker image with the same tag (e.g., `backend:local`) has been rebuilt. To ensure the new image is used, you must delete the existing pod manually or use unique image tags to force updates.


### ✅ Backend

```bash
# Enable Docker inside Minikube
eval $(minikube docker-env)

# Rebuild the image
docker build --no-cache -t backend:local ./backend

# Recreate the config map
kubectl delete configmap backend-env --ignore-not-found
kubectl create configmap backend-env --from-env-file=./backend/api/.env.deploy

# Re-apply the manifest
kubectl apply -f k8s/backend.yaml

# Delete the running pod to ensure the new image is used
kubectl delete pod -l app=backend
```

> 💡 Alternatively, consider using unique tags for your Docker images (e.g., `backend:local-<timestamp>`) and updating the Kubernetes manifest accordingly. This avoids the need to delete the pod manually.

### ✅ Frontend

```bash
# Enable Docker inside Minikube
eval $(minikube docker-env)

# Rebuild the image
docker build --no-cache -t frontend:local ./web

# Recreate the config map
kubectl delete configmap frontend-env --ignore-not-found
kubectl create configmap frontend-env --from-env-file=./web/.env.deploy

# Re-apply the manifest
kubectl apply -f k8s/frontend.yaml

# Delete the running pod to ensure the new image is used
kubectl delete pod -l app=frontend
```
> 💡 As with the backend, using a unique tag for each build can automate the update process.

---

## 🧼 Cleaning Up

To delete all Kubernetes resources created during deployment:

```bash
kubectl delete -f k8s/backend.yaml
kubectl delete -f k8s/frontend.yaml
kubectl delete configmap backend-env frontend-env
```

To stop Minikube:

```bash
minikube stop
```
---

## 📁 Project Structure (Relevant Paths)
```bash
.
├── backend/
│   ├── Dockerfile
│   └── api/
│       └── .env.deploy
├── web/
│   ├── Dockerfile
│   └── .env.deploy
├── k8s/
│   ├── backend.yaml
│   └── frontend.yaml
├── deploy.sh
└── README.md
```

---

## 📎 Notes

- Ensure that your Kubernetes manifests (`k8s/*.yaml`) reference the image names `backend:local` and `frontend:local`.
- The `ConfigMaps` are mounted or injected into the containers according to how your manifests are written.