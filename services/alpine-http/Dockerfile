FROM alpine:latest
RUN apk add --no-cache python3 py3-pip
WORKDIR /app
COPY . /app
CMD ["python3", "-m", "http.server", "8000"]
