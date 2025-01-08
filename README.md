## AI-SWEET: An Ollama + OpenWebui Docker Compose for Windows + NVIDIA 
===============

### Overview

AI-SWEET is a custom Docker Compose setup designed for local development and testing. It provides a convenient way to run multiple services simultaneously, leveraging the power of Docker containers.

### Running AI-SWEET

To start the services, run the following command:
```bash
git clone https://github.com/Martin-Stankard/AI-SWEET.git
cd ./AI-SWEET
docker-compose up --build
```
Point your browser to `http://localhost:8080`.

### Pipelines

```docker compose --profile pipelines up```

although, just to be safe:

```docker compose --profile pipelines up --build```

This project contains a hello world filter pipeline and docker-runs the open-webui/pipelines project. 

To configure:
1. make sure the pipelines service is running via ```docker ps```
1. Navigate to the Admin Panel > Settings > Connections > OpenAI API section in Open WebUI.
2. Add new API URL to `http://host.docker.internal:9099` and the API key to `0p3n-w3bu!`.

Your pipelines should now be active.
- `./Pipelines/filterPipelineHelloWorld`: Good feedback in pipelines services log AND baseline OpenWebUI llm use.

### Flowise

```docker compose --profile flowise up```

although, just to be safe:

```docker compose --profile flowise up --build```



### Add Google Search to Web-UI

To add Google search functionality:
1. Start here: [Programmable Search Engine](https://programmablesearchengine.google.com/about/).
2. Create a new search engine.
3. Navigate to the Admin Panel > Settings > Web Search.
4. Enable "Web Search Engine".
5. From the Google search engine you created, get the "Google PSE Engine Id" and the "Google PSE API Key". (Keep that secret)
6. Save settings.
7. These seem to expire.

*IMPORTANT*: In the Web UI, normal chat interface, there is a '+'. Choose Web search there.

### TODOs

* Need docker profile feature worked in, May never use pipelines
* Bringing Flowise here
* Pydantic deep dive analyzing this: [YouTube Video](https://youtu.be/pC17ge_2n0Q?si=vzgZlxL1x-60r5MY)
* Think about a scraper tool
* Pie in the sky....test the --profile pipelines++ config "nightly". I am positive if I don't use it for a week, I will watch a 1 hour update and build process fail.


