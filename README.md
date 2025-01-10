## AI-SWEET: An Ollama + Open Webui + profile-toggleable-goodies Docker Compose for Windows + NVIDIA 
===============

### Overview

AI-SWEET is a "Docker Compose up" minimal defauly setup designed for local development and testing. Because I forget long commands 

### Running AI-SWEET

To start the services, run the following command:
```bash
git clone https://github.com/Martin-Stankard/AI-SWEET.git
cd ./AI-SWEET
docker-compose up
```
Point your browser to `http://localhost:8080`.

### Pipelines

```docker compose --profile pipelines up```

This project contains a hello world filter pipeline 

To configure:
1. make sure the pipelines service is running via ```docker ps```
1. Navigate to the Admin Panel > Settings > Connections > OpenAI API section in Open WebUI.
2. Add new API URL: `http://host.docker.internal:9099` and API key: `0p3n-w3bu!`.

Your pipelines should now be active.
- `./Pipelines/filterPipelineHelloWorld.py`: Load into admin settings > pipelines. Good feedback in pipelines services log AND baseline OpenWebUI llm use. Powerful, dangerous stuff as it executes user input raw python code.

### Flowise

```docker compose --profile flowise up```

Point your browser to `http://localhost:3000`. 
- I recomend this to continue: https://youtu.be/9TaRksXuLWY?si=PXheDAWPwM2wB-99 ( AWESOME Flowise training, vast subject )
- TODO, include a --profile flowise-solution service that hosts a "live, dynamic load embed?" index.html minimalist flowise solution server. Include importable bit.
-- problem, need to clean importable demo whatever to embed. Something useful like a rag input scrubber > just search. nginx.index.html || full react shebang

### nginx untested
 - to host Flowise embeddings. https://localhost:8089/
 - part of profile flowise   

### qdrant untested
 - for vector embeddings/fancy rag
 - https://localhost:6333
 - https://localhost:6334


### Add Google Search via Open Web-UI settings

To add Google search functionality:
1. Start here: [Google Programmable Search Engine](https://programmablesearchengine.google.com/about/)
2. Create a new search engine
3. Navigate to the Open-Webui Admin Panel > Settings > Web Search
4. Enable "Web Search Engine"
5. From the Google search engine you created, get the "Google PSE Engine Id" and the "Google PSE API Key". (Keep that secret)
6. Save settings
7. These seem to expire and have usage limits, so consider early if debugging

*IMPORTANT*: In the Web UI, normal chat interface, there is a '+'. Choose Web search there.

### TODOs

* Bringing Flowise here
* Pydantic deep dive analyzing this: [YouTube Video](https://youtu.be/pC17ge_2n0Q?si=vzgZlxL1x-60r5MY)
* Think about a scraper tool
* Pie in the sky....test the --profile pipelines++ config "nightly". I am positive if I don't use it for a week, I will watch a 1 hour update and build process fail.


