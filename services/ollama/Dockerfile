# Use the specified base image
FROM ollama/ollama

# Ensure directories exist (optional)
RUN mkdir -p /root/.ollama

# Expose the application port
EXPOSE 11434

# Set the default command if needed (usually already defined in the base image)
CMD ["sh", "-c", "ollama pull nomic-embed-text && ollama pull llama3.2 && ollama run llama3.2"]
