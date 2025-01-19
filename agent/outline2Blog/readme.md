# converts a nested bullet list 

python ./outline2Blog.py
- put outline in config.json
-- keys don't matter
-- respects links
-- Limit!!! 2 levels. This is a product blaster. Just won't look, just won't care implementation.
- estimate a 3.13 sentence to bullet, magic number BULLET2SENTENCE
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
- original writer takes 3x critiques and ? if over magic number CRITS=5, random sample 5.

boom boom boom, out pops four candidates

TODO: I pick 1 of 4; get another 4x critique script. pick critiques and go lol...4x again. Subtle changes from critiques being the goal.