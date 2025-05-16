FROM node:18-bookworm-slim AS builder

WORKDIR /app

# Copy the application into the container.
COPY . /app

# Set build-time variable for the env file path
ARG ENV_FILE=.env.deploy

# Copy the environment file to the expected location inside the image
COPY ${ENV_FILE} /app/.env

# Install the application dependencies.
RUN npm install

# Build the application.
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
# Copy the nginx configuration file.
COPY --from=builder /app/nginx.conf /etc/nginx/nginx.conf

# Expose the port 80 for the container
EXPOSE 80

# Run the application.
CMD ["nginx", "-g", "daemon off;"]
