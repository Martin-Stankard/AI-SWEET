import argparse
import json
import os
import docker
import requests
import ollama

#magic number globals
MYMODELS = ["llama3.1:8b", "qwen:7b", "mistral:latest", "llama3.2:latest"]
CRITS = 5
SENTENCEPERBULLET = 2.83
OUTLINECOUNT = 0
critiquePrompt = ""
rewritePrompt = ""

def check_ollama_container():
    client = docker.from_env()
    try:
        container = client.containers.get('ollama')
        if container.status == 'running':
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
    if response.status_code == 200:
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
        #set outlineCount here, equal to the lines of 
    formatted_lines = [f'"{line.strip()}"' for line in lines]
    if len(formatted_lines) > 1:
        outline = ', '.join(formatted_lines[:-1]) + ' and ' + formatted_lines[-1]
    else:
        outline = formatted_lines[0] if formatted_lines else ''
    return outline

def ollamaChatCall(m, outline):
    print(m)
    print(outline)
    
    
def main():
    outline = get_outline()
    
    print("Formatted outline:", outline)

    if not check_ollama_container():
        print("Exiting program as the Ollama container is not running or not found.")
        exit(1)

    if not check_models():
        print("Exiting program as the required models are not found.") #TODO add a dl model if not there.
        exit(1)
    
    print("Starting the process with all required models.")
    # foreach model,
    for model in MYMODELS:
        print(f"Processing with model: {model}")
        
        writingPrompt = f"You are a writer. Given the following list of bullet points in outline form:{outline} ; write a blog. The style should be brief, to the point and humorous. The final blog should be about {SENTENCEPERBULLET*OUTLINECOUNT} sentences long. Return JUST the blog and nothing else, including small talk from you or asking if there is anything else you can help me with."
        # make Ollama chat API request with writing prompt, model, and outline
        ollamaChatCall(model, writingPrompt) # contains inline string literals BULLET2SENTENCE and outline
        
        # copy myModels to copyMyModel
        
        # remove model from copyMyModel
        
        # for each m in copyMyModel
            
        
    

if __name__ == "__main__":
    main()