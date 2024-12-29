# Use the specified image from GitHub Container Registry
FROM ghcr.io/open-webui/open-webui:ollama

# Set environment variables (if needed)
ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility

# Ensure the directories are created in the container (optional)
RUN mkdir -p /root/.ollama /app/backend/data

# Expose the necessary port
EXPOSE 8080

# Set the default command to start the application
#CMD ["start"]  # Replace "start" with the actual start command if needed
