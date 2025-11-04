# Build stage
FROM node:20-alpine AS build
WORKDIR /app
ENV NODE_ENV=production
COPY services/api/package*.json ./
RUN npm ci --only=production
COPY services/api/dist /app

# Runtime stage (smaller base)
FROM node:20-alpine
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
WORKDIR /app
COPY --from=build /app /app
RUN chown -R appuser:appgroup /app
USER appuser
EXPOSE 3000
CMD ["node", "server.js"]
