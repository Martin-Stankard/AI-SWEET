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
 - to host Flowise embeddings. 
 - https://localhost:8089/
 - part of profile flowise   

### qdrant untested
 - for vector embeddings/fancy rag
 - https://localhost:6333
 - https://localhost:6334
 - default profile until further notice.

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

* get flowise manifold working in open webui
* use qdrant for a vector store even though csv agents are likely it for my rags needs for a while...
* Pydantic deep dive analyzing this: [YouTube Video](https://youtu.be/pC17ge_2n0Q?si=vzgZlxL1x-60r5MY)
* Think about a scraper tool
* Pie in the sky....test the --profile pipelines++ config "nightly". I am positive if I don't use it for a week, I will watch a 1 hour update and build process fail.

* Here are some instances of `flowise` images used in `docker-compose.yml` files, may analyze:

- [bigbeartechworld/big-bear-casaos](https://github.com/bigbeartechworld/big-bear-casaos/blob/2e0f6b31759f81d075feddec71127d6a5c77c030/Apps/flowise/docker-compose.yml#L1-L87)
- [coleam00/ai-agents-masterclass](https://github.com/coleam00/ai-agents-masterclass/blob/f1c4ef0911ec005b7e09f1805e4aea212386864f/local-ai-packaged/docker-compose.yml#L1-L102)
- [meliani/docker-library](https://github.com/meliani/docker-library/blob/a0cad113993b71f533e65c88d2e534e1cee3814d/apps/flowise/docker-compose.yml#L1-L26)
- [sciencemediacenter/lab-scicar2024-workshop](https://github.com/sciencemediacenter/lab-scicar2024-workshop/blob/4e40ca2c53c602b6a764f31fc9d372c9f0abe306/examples/flowise/docker-compose.yml#L1-L36)
- [yorch/docker-compose-services](https://github.com/yorch/docker-compose-services/blob/78b0e5d45dd9332f4a687392b034a32a6b747341/flowise/docker-compose.yml#L1-L53)
- [ragincajunbanjo/runtipi-appstore](https://github.com/ragincajunbanjo/runtipi-appstore/blob/1cf3d0f10109e2c18c4b5b59fe47d80a8f347f64/apps/flowise/docker-compose.yml#L1-L53)
