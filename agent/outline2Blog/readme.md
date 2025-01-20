# converts a nested bullet list into a pithy blog type of essay
# Possibly done for now. Produces 4 candidate blogs per outline. 
# atm, prompts are super simple. 


python ./outline2Blog.py

algorithm....I like 4 models on ollama, research no rag, no flowise...

[ 
  llama3.2:latest - 3ish,
  mistral:latest  - 7ish,
  qwen:7B         - 8ish,
  llama3.1        - 8ish 
]

Ok so...foreach model,
- write 1st pass, you are a writer, no search, no rag
- random order the remaining three models
- critique with a list of improvements x 3  ; simple, bullets, why
- original writer model takes 3x critiques TODO, can be upsophisticated keeping writer model in chat, for 1 2 write-rewrite, while all of the citique requests are one and done. 
- implementation goal, I don't care who each writer is, each is of a comparable ability and it is like preference in fractal noise images. Four candidate writers, each with a 3 editor review bored. 

Using Ollama-bottleneck so flat program flow/ no async multithreading and here there is 4 great opportunities, each with a 3x here. Fun TODO might be some WWW api key use multithreading opportunities down the road.

boom boom boom, out pops four candidates

TODO: I pick 1 of 4; get another 4x critique script. pick critiques and go lol...4x again. Subtle changes from critiques being the goal. 

TODO: abstracting out THIS outline AND blog component to....llm feeder a 2 b is a real move.
feature > tests > comments > code ..... just 3 writing prompts...can even be a call to write writing prompt given a and b; critique an rewrite can solidify as generic prompts ... probably copy this to https://github.com/Martin-Stankard/docker-compose-gold/tree/main/agent