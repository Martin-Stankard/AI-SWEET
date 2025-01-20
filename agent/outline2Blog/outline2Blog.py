import argparse
import json
import os
import docker
import requests
import ollama

#magic number globals
MYMODELS = ["llama3.1:8b", "qwen:7b", "mistral:latest", "llama3.2:latest"]
OUTLINECOUNT = 1
critiquePrompt = ""
rewritePrompt = ""

#TODO time ollama calls? / got thos token numbers...not here, today

def check_ollama_container():
    client = docker.from_env()
    try:
        container = client.containers.get('ollama')
        if (container.status == 'running'): 
            print("Ollama container is running.")
            return True
        else:
            print("Ollama container is not running.")
            return False
    except docker.errors.NotFound:
        print("Ollama container not found.")
        return False

def check_models():
    response = requests.get('http://localhost:11434/api/tags')
    if (response.status_code == 200):
        
        tags = response.json()
        models_present = [model.get('model') for model in tags.get('models', [])]
        if all(required_model in models_present for required_model in MYMODELS):
            print("All required models are present.")
            return True
        else:
            print("Not all required models are present.")
            return False
    else:
        print("Failed to get tags:", response.status_code)
        return False

def get_outline():
    outline_path = os.path.join(os.path.dirname(__file__), 'outline.txt')
    with open(outline_path, 'r') as file:
        lines = file.readlines()
        OUTLINECOUNT = len(lines)  # set outlineCount here, equal to the number of lines
    
    formatted_lines = [f'"{line.strip()}"' for line in lines]
    if len(formatted_lines) > 1:
        outline = ', '.join(formatted_lines[:-1]) + ' and ' + formatted_lines[-1]
    else:
        outline = formatted_lines[0] if formatted_lines else ''
    return outline

def ollamaChatCall(model, prompt): 
    #TODO...might be an up efficiency by doing this as a "chat completion" instead of this "completion". 
    # context window/chat history size mighth come up. 
    # Can swap in models but this rigidity is valuable/don't want to jam up flow. 
    print (f"model: {model}, prompt:{prompt}")
    # Flow jammed up anyways
    
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    if (response.status_code == 200):
   
        return response.json()
    else:
        print(f"Failed to generate response from model {model}: {response.status_code}")
        return None

def main():
    ollamaCallCount = 0
    
    outline = get_outline()
    
    print("Formatted outline:", outline)

    if not check_ollama_container():
        print("Exiting program as the Ollama container is not running or not found.")
        exit(1)

    if not check_models():
        print("Exiting program as the required models are not found.") #TODO add a dl model if not there.
        exit(1)
    
    ollamaCallCount += 1
    
    print("Starting the process with all required models.")
    # foreach model,
    for model in MYMODELS:
        print(f"Processing writing with model: {model}")
        
        writingPrompt = f"You are a writer. Given the following list of bullet points in outline form:{outline} ; expand them into a blog."
        # make Ollama chat API request with writing prompt, model, and outline
        response = ollamaChatCall(model, writingPrompt) # contains inline string literals BULLET2SENTENCE and outline
        
        # if there is a key "response" inside response, print it and save it as initialBlog; else exit.
        if response and 'response' in response:
            ollamaCallCount += 1
            initialBlog = response['response']
        else:
            print(f"Failed to get a valid response from the model{model}.")
            exit(1)
        
        # copy myModels to copyMyModel
        copyMyModel = MYMODELS.copy()
        
        # remove model from copyMyModel
        copyMyModel.remove(model)
        
        # for each m in copyMyModel
        critiques = []
        for m in copyMyModel:
            print(f"Processing critique with model: {m}, on blog written by {model}")
            # create critiquePrompt with initialBlog 
            critiquePrompt = f"You are an online blog editor. Please critique the following blog: {initialBlog}."
            # ollamaChatCall(CritiqueModel-0,1,2, critiquePrompt)
            critiqueResponse = ollamaChatCall(m, critiquePrompt)
            # if there is a response.response, save it in a list called critiques.
            if critiqueResponse and 'response' in critiqueResponse:
                critiques.append(critiqueResponse['response'])
            else:
                print(f"Failed to get a valid response from the model crit model {m}.")
                exit(1)
        
        # TODO analyze crits, if less than 
        # create rewritePrompt using initialBlog, and critiques
        
        print(f"Rewrite on blog written by {model}")
        rewritePrompt = f"You are a writer. Rewrite the following blog considering these critiques: {critiques}. Blog: {initialBlog}."
        finalBlogResponse = ollamaChatCall(model, rewritePrompt)
        if finalBlogResponse and 'response' in finalBlogResponse:
            ollamaCallCount += 1            
            # save or append to ./blog.txt
            with open('blog.', 'a', encoding='utf-8') as blog_file:
                blog_file.write(finalBlogResponse['response'] + "\n\n\n\n\n*****\n\n\n\n\n")
        # no else here...wait this long, take whatever...

    print("Ollama Call Count"+ollamaCallCount)

if __name__ == "__main__":
    main()