# Picture Namer utility agent
## One folder at a time
- from this./ folder:
- ```pip install -r requirement.txt```
- ```python PictureNamer -f <path to directory full of poorly named images>```


# doesn't do anything yet if you stumble in here on main branch...

# Now just prints out potential names. 

# I don't want to leave file writing possibilites alive here at this time, so a "next step will be renaming the file or...seems ott not rename it, and log the na...maybe not ott. TODO/recycle this elsewhere will be part of a pipeline

(image prompt, prompt, configs ? ) -> gen-ai-img -> image to file with stupid name + image-ref
                                                     \ - async  
                                                      ( image prompt, prompt, configs, image-ref ) -> into vec rag db w/embedding
                                                     \ - async
                                                      ( image, config ) -> this -> ( image-ref, description ) -> into vec rag db w/embedding
                                                     \ - async
                                                      (??) -> file store tracking sql db, solid need if I want to reject stuff after the fact/hot ot not review stuff in db.

# tasty for rag because of descriptions...possibly only need vec treatment for description and image ref; save prompts and configs in seperate sql db table. 

# goal would be to drive gen-ai-image input , via a hot or not, per param?, review; available asap...could be available before dscription/which hot or not viewer (optional) sees/wants to see/positive value from seeing...worth learning what comes out of description process.

## Seperate topic
### 

