import argparse
import json
import os
import docker
import requests
import ollama

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = json.load(file)
    return config

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
        for model in tags.get('models', []):
            print(model.get('model'))     
       

def main():
    
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    config = load_config(config_path)
    print("Loaded config:", config)

    check_ollama_container()
    begin = check_models()
    if begin:
        print("Starting to name pictures in", args.folder)
        for filename in os.listdir(args.folder):
            if filename.lower().endswith(( '.png', '.jpg' )):
                print(filename)
                image_path = os.path.join(args.folder, filename)
                
                res = ollama.chat(
                    model="llama3.2-vision:latest",
                    messages=[
                        {
                            'role': 'user',
                            'content': "Describe this image in 5 words. Exclude prepositions and articles and any special characters or concern for grammar.",
                            'images': [image_path]
                        }
                    ]
                )
                print(res['message']['content'])
    else:
        print("Exiting program as the required model is not found.")
        exit(1)

if __name__ == "__main__":
    main()