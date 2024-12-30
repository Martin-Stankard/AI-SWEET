# AI-SWEET
docker-compose up ( TODO, on change, as is, add --build)

- (TODO expects a local adjacent private repo folder /stuff//input//output)
-- (how to guarantee data isn't moved from priv to here here)
Works:
- qdrant docs @ http://localhost:6333/dashboard#/welcome
- alpine-http file server @ http://localhost:8081/
- nginx index.html served @ http://localhost:8082/
- ollama @ http://localhost:11434/
- open web ui @ localhost:3000 

This works...
- docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main

-SUCCESS, minus worrisome throwaway local password manager dialog

TEST
- Replace with open-webui.docker file and docker-compose touch up from that docker run command. Git Push test100 here...
