# converts a nested bullet list into a pithy blog type of essay
# WIP 

python ./outline2Blog.py
- put outline in config.json
-- keys don't matter / good place for comments maybe
-- respects links
-- Limit!!! 2 levels. This is a product blaster. Just won't look, just won't care implementation.
- estimate a 2.83 sentence to bullet, magic number BULLET2SENTENCE
- outputs to output001.txt


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
- original writer takes 3x critiques and ? if over magic number CRITS=5, random sample 5 unless they ordered???idk bout that.
- implementation goal, I don't care who each writer is, each is of a comparable ability and it is like preference in fractal noise images. Four candidate writers, each with a 3 editor review bored. 

Using Ollama-bottleneck so flat program flow/ no async multithreading and here there is 4 great opportunities, each with a 3x here. Fun TODO might be some WWW api key use.

boom boom boom, out pops four candidates

TODO: I pick 1 of 4; get another 4x critique script. pick critiques and go lol...4x again. Subtle changes from critiques being the goal. 