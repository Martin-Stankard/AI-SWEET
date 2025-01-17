import argparse
import json
import os
import docker
import requests

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
        
def check_vision_model():
    response = requests.get('http://localhost:11434/api/tags')
    if response.status_code == 200:
        tags = response.json()
        for model in tags.get('models', []):
            if model.get('model') == 'llama3.2-vision:latest':
                print("Model 'llama3.2-vision:latest' is there.")
                return True
        print("Model 'llama3.2-vision:latest' isn't there.")
        return False
    else:
        print("Failed to get tags:", response.status_code)
        return False

def main():
    parser = argparse.ArgumentParser(description='Picture Namer utility agent')
    parser.add_argument('-f', '--folder', required=True, help='Path to the directory full of poorly named images')
    args = parser.parse_args()

    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    config = load_config(config_path)
    print("Loaded config:", config)

    check_ollama_container()
    begin = check_vision_model()
    if begin:
        print("Starting to name pictures in", args.folder)
        for filename in os.listdir(args.folder):
            if filename.lower().endswith(('.png', '.jpeg', '.gif')):
                image_path = os.path.join(args.folder, filename)
                with open(image_path, 'rb') as image_file:
                    image_data = image_file.read()
                response = requests.post(
                    'http://localhost:11434/api/chat',
                    json={
                        'model': 'llama3.2-vision:latest',
                        'messages': [
                            {
                                'role': 'user',
                                'content': 'Describe this image:',
                                'images': [image_data]
                            }
                        ]
                    }
                )
                
                if response.status_code == 200:
                    description = response.json().get('message', {}).get('content', 'No description available')
                    print(f"Description for {filename}: {description}")
                else:
                    print(f"Failed to describe {filename}: {response.status_code}")
    else:
        print("Exiting program as the required model is not found.")
        exit(1)
    
if __name__ == "__main__":
    main()