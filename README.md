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

This project contains hello world pipeline files and docker-runs the open-webui/pipelines. 
To configure, (TODO, can I stick that into envs in the compose.yml?) 
Navigate to the Settings > Connections > OpenAI API section in Open WebUI.
Add new API URL to http://host.docker.internal:9099 and the API key to  ```python
0p3n-w3bu!
``` . Your pipelines should now be active.
* ./Pipelines/filterPipelineHelloWorld

### TODOs
* working on this https://zohaib.me/extending-openwebui-using-pipelines/ ....basic open webui pipeline hello world,
* pydantic deep dive analyzing this https://youtu.be/pC17ge_2n0Q?si=vzgZlxL1x-60r5MY
* think about a scraper tool


