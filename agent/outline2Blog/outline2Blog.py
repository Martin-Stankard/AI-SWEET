import argparse
import json
import os
import docker
import requests
import ollama

#magic number globals
MYMODELS = ["llama3.1:8b", "qwen:7b", "mistral:latest", "llama3.2:latest"]
CRITS = 5
BULLET2SENTENCE = 2.83
writingPrompt = ""
critiquePrompt = ""
rewritePrompt = ""

def check_ollama_container():
    client = docker.from_env()
    try:
        container = client.containers.get('ollama')
        if container.status == 'running':
            print("Ollama container is running.")
        else:
            print("Ollama container is not running.")
    except docker.errors.NotFound:
        print("Ollama container not found.")

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



def main():

    outline_path = os.path.join(os.path.dirname(__file__), 'outline.txt')
    with open(outline_path, 'r') as file:
        lines = file.readlines()
    formatted_lines = [f'"{line.strip()}"' for line in lines]
    if len(formatted_lines) > 1:
        outline = ', '.join(formatted_lines[:-1]) + ' and ' + formatted_lines[-1]
    else:
        outline = formatted_lines[0] if formatted_lines else ''
    print("Formatted outline:", outline)

    check_ollama_container()
    begin = check_models()
    if begin:
        print("Starting the process with all required models.")
        # foreach model,
        for model in MYMODELS:
            print(f"Processing with model: {model}")
            
            # make Ollama chat API request with writing prompt, model, and outline
            
            # copy myModels to copyMyModel
            
            # remove model from copyMyModel
            
            # for each m in copyMyModel
            
    else:
        print("Exiting program as the required models are not found.") #TODO add a dl model if not there.
        exit(1)

if __name__ == "__main__":
    main()