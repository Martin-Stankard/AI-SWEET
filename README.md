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

Then a nuke repull time test. test 103.
- pulled and go test103
- good test...same wait for webui to start AND....it is NOT finding my local ollama llama3.2 model

TODO (after hike) 
- ...unistall local ollama and all models :( 
- goog "ollama docker persist local model download"
- redo nuke test104
- Then focus on ollama-docker gpu biz