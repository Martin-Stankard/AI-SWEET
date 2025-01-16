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

def main():
    parser = argparse.ArgumentParser(description='Picture Namer utility agent')
    parser.add_argument('-f', '--folder', required=True, help='Path to the directory full of poorly named images')
    args = parser.parse_args()

    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    config = load_config(config_path)
    print("Loaded config:", config)

    check_ollama_container()
    
    response = requests.get('http://localhost:11434/api/tags')
    if response.status_code == 200:
        print("Tags:", json.dumps(response.json(), indent=4))
    else:
        print("Failed to get tags:", response.status_code)

if __name__ == "__main__":
    main()