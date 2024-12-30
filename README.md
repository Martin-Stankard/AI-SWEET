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

So far so good. TODO, clean all docker bits except images...time test. test101 
- 30 sec to open webui banner...may need kick at localhost3000...
- 2 min then checked links, aok except 3000.
- seems live at "INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)"

test 102
- delete all artifacts except big ollama and webui images.
- docker compose build   : time:
- docker compose up    : time:
- time to pass all endpoint tests: 

Then a nuke repull time test.