## AI-SWEET: An Ollama + Open Webui + profile-toggleable-goodies Docker Compose for Windows + NVIDIA 
===============

### Overview
- This is for local, on your own, private computer. Lots of bad api-key practices here, this is like lab equipment atm.
- AI-SWEET is a "Docker Compose up" minimal default, local ollama-openwebui-flowise docker system  for feature extension and access. 

### Running AI-SWEET

To start the services, run the following command:
```bash
git clone https://github.com/Martin-Stankard/AI-SWEET.git
cd ./AI-SWEET
docker-compose up
```
Point your browser to `http://localhost:8080`.
Flowise is at `http://localhost:3000`.

### Pipelines
## Powerful, dangerous stuff as it executes user input raw python code.

To configure:
1. make sure the pipelines service is running via ```docker ps```
1. Navigate to the Admin Panel > Settings > Connections > OpenAI API section in Open WebUI.
2. Add new API URL: `http://host.docker.internal:9099` and API key: `0p3n-w3bu!`. Test button available under settings, should be green

Your pipelines should now be active. Load into admin settings > pipelines. 
- `./Pipelines/filterPipelineHelloWorld.py`: This offers good feedback in pipelines services log AND baseline OpenWebUI llm use. 
- `./Pipelines/flowise_agentflow_test001.py`: Find and change API_URL ( from flowise flow embed dialogue ) and self.name, to mathch a flow named "test001". Select in open-webui, needs a Flowise project to work

### Flowise

Flowise `http://localhost:3000`. 
- I recomend this to continue: https://youtu.be/9TaRksXuLWY?si=PXheDAWPwM2wB-99 ( AWESOME Flowise training, vast subject )
- Immediate open web-ui test project, import `./Flowise/agentflow_test001 Agents.json` for immediate pipeline feedback ( it just analyzes  whether your question requires "search" or "no search". TODO, clean up logging/use autocomplete in webui. )

### qdrant TODO, no api key rag vector db, hopefully.
 - for vector embeddings/fancy rag
 - http://localhost:6333/dashboard#/collections

 ### postgres and pgadmin
 - for record manager on flowise knowledge base "upsert"
 - http://localhost:8888/browser/     

### Add Google Search via Open Web-UI settings

To add Google search functionality:
1. Start here: [Google Programmable Search Engine](https://programmablesearchengine.google.com/about/)
2. Create a new search engine
3. Navigate to the Open-Webui Admin Panel > Settings > Web Search
4. Enable "Web Search Engine"
5. From the Google search engine you created, get the "Google PSE Engine Id" and the "Google PSE API Key". (Keep that secret)
6. Save settings
7. These seem to expire and have usage limits, so consider early if debugging.
8. Same credentials for a flowise Google custom search tool.

*IMPORTANT*: In the Open Web UI, normal chat interface, there is a '+'. Choose Web search there.

### TODOs
Possibly done after qdrant/rag process is streamlined
