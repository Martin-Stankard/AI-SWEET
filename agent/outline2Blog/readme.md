# converts a nested bullet list into a pithy blog type of essay
## Possibly done for now. Produces 4 candidate blogs per outline. 
### atm, prompts are super simple. 


```python ./outline2Blog.py```
- put a simple, one collumn list in outline.txt 

algorithm....I like 4 models on ollama, research no rag, no flowise...

[ 
  llama3.2:latest - 3ish,
  mistral:latest  - 7ish,
  qwen:7B         - 8ish,
  llama3.1        - 8ish 
]

So foreach model,

Using local Ollama-bottleneck so flat program flow/ no async multithreading. There is 4 great opportunities, each with a 3x here. 
- Fun TODO might be some 3rd party WWW api key use, multithreading opportunities down the road.

boom boom boom, out pops four candidates.
- Pick from 4++ is better than any notion of "llm chooses 'best'".

TODO: I pick 1 of 4; get another 4x critique script. pick critiques and go lol...4x again. Subtle changes from critiques being the goal. 

TODO: abstracting out THIS outline AND blog component to....llm feeder "a2b" is a real move.
foreach writing prompt per '>'.
feature > tests > comments > code ..... just 3 writing prompts...can even be a call to write writing prompt given a and b; 
'critique' and 'rewrite' can solidify as generic prompts each leap '>' 
That happens here...overnight, wake up to unit tests; copy this to https://github.com/Martin-Stankard/docker-compose-gold/tree/main/agent