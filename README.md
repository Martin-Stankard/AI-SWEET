# AI-SWEET
docker-compose up ( TODO, on change, as is, add --build)

- (TODO expects a local adjacent private repo folder /stuff//input//output)
-- (how to guarantee data isn't moved from priv to here here)
Works:
- (seconds) qdrant docs @ http://localhost:6333/dashboard#/welcome
- (seconds) alpine-http file server @ http://localhost:8081/
- (seconds) nginx index.html served @ http://localhost:8082/
- (seconds) ollama @ http://localhost:11434/
- (3min) open web ui @ localhost:3000 

So far so good. TODO, clean all docker bits except images...time test. test101 
- 30 sec to open webui banner...may need kick at localhost3000...
- 2 min then checked links, aok except 3000.
- seems live at "INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)"

test 102
- delete all artifacts except images.
- docker compose build   : time: almost instant
- docker compose up    : time: a minute or two to open-webui after webui banner| INFO:     connection open
- time to pass all endpoint tests: about 2 minutes to build everything...mostly waiting for open web ui.

Then a nuke repull time test. test 103.
- pulled and go test103