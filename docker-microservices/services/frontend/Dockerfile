# Build stage
FROM node:20-alpine AS build
WORKDIR /app
COPY services/frontend/package*.json ./
RUN npm ci
COPY services/frontend/ .
RUN npm run build

# Serve with nginx (runtime)
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
# serve static with minimal config
COPY deploy/nginx/frontend.conf /etc/nginx/conf.d/default.conf
# read-only root for security
RUN mkdir -p /var/cache/nginx && chown -R nginx:nginx /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
