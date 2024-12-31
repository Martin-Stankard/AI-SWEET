## AI-SWEET: A Docker Compose Setup for Local Development
===============

### Overview

AI-SWEET is a custom Docker Compose setup designed for local development and testing. It provides a convenient way to run multiple services simultaneously, leveraging the power of Docker containers.

### Prerequisites

To use AI-SWEET, you'll need to create three adjacent folders: `../ollamaLocalVolume`, `../openWebUILocalVolume`, (TODO and `../text`).

### Running AI-SWEET

To start the services, run the following command:
```bash
git clone https://github.com/Martin-Stankard/AI-SWEET.git
cd ./AI-SWEET
docker-compose up --build
```

### TODOs

* Guarantee data integrity by preventing data from being moved from private directories to the container volumes.
* Enable GPU acceleration for the `GPU feelz.` service.
* Implement pipeline-based development and testing for the `Pipeline rag ability, local ../` service.
* Investigate and document the purpose of the `Rag server?` service.