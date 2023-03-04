# Test Kuantaz

## Description
---
API Rest written with Python using Fastapi.

### Construction 🛠️
* **Language:** Python 3.10
* **Technologies:** Fastapi

## Requirements
---
- Docker installed

- Remember to copy the env.test to .env ( in folder app ) to add environment variables to the application. ( for development )

## Installation and execution
---
Clone or Fork the project.

Run ```docker-compose``` command inside **docker-python** folder.

* Building the containers: ```docker-compose build```

* Starting the services: ```docker-compose up -d```

* Stoping the services: ```docker-compose stop```

By default the service will run under the following port:
- test-talent-kombat: 8000

## Project Structure
---
The following diagram describe the project structure used for this API
```
test_kuantaz
│   .gitignore
│   README.md
│   docker-compose.yml
│   .pre-commit-config.yaml
│
└───app
│   │   .env.docker
│   │   .env.test
│   │   Dockerfile
│   │   requirements.txt
│   │   requirements-docker.txt
│   │   .dockerignore
│   │
│   │   main.py
│   │
│   └───config                  Contains system settings
│   │   │
│   │   └───constants.py        Constants used in the project
│   │
│   │   └───exceptions.py       Contains the custom exceptions for project
│   │
│   │   └───environment.py      Environment variables
│   │
│   └───classes                 Contains the classes used in the application.
│   │
│   │   ...
│   │
│   └───routers                 Contains application routers
│   │
│   │   ...
│   │
│   └───services                The application service layer
│   │
│   │   ...
│   │
│   └───utils                   Functions utils
│   │
│   │   ...
│   │
│   └───tests
│
└────────────
...

```

## Documentation 📕
---

The documentation is in postman.

postman : [documentation on Postman](documentation/talent-kombat.postman_collection.json). Remember to add the environment variables in postman ( {{base_url}} )


## Development 💻

Requirements:
- virtualenv
- python3.10

If you want to run the project to develop , you can run the following commands:
```shell
   cd app

   virtualenv -p python3.10 env

   source env/bin/activate # in linux or macos

   pip install -r requirements
```

Run with env activated:

```shell
   uvicorn main:app --reload
```

If you want to contribute to the project, Remember that pre-commit is used for uniform code styling, so you'll need to **install the pre-commit**.

## Testing ⚙️

Requirements: Follow the instructions it says in Development

To run the tests:

```shell
   cd app

   source env/bin/activate

   python -m pytest
```

### Authors ✒️

* **Author:** Steve Matos, <steve.matos.1998@gmail.com>
