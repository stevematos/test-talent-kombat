# Test Talent Kombat

## Description
---
API Rest written with Python using Fastapi.

### Construction π οΈ
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
β   .gitignore
β   README.md
β   docker-compose.yml
β   .pre-commit-config.yaml
β
ββββapp
β   β   .env.docker
β   β   .env.test
β   β   Dockerfile
β   β   .dockerignore
β   β   requirements.txt
β   β   requirements-docker.txt
β   β
β   β   main.py
β   β
β   ββββconfig                  Contains system settings
β   β   β
β   β   ββββconstants.py        Constants used in the project
β   β
β   β   ββββexceptions.py       Contains the custom exceptions for project
β   β
β   β   ββββenvironment.py      Environment variables
β   β
β   ββββclasses                 Contains the classes used in the application.
β   β
β   β   ...
β   β
β   ββββrouters                 Contains application routers
β   β
β   β   ...
β   β
β   ββββservices                The application service layer
β   β
β   β   ...
β   β
β   ββββutils                   Functions utils
β   β
β   β   ...
β   β
β   ββββtests
β
βββββββββββββ
...

```

## Documentation π
---

The documentation is in postman.

postman : [documentation on Postman](documentation/talent-kombat.postman_collection.json). Remember to add the environment variables in postman ( {{base_url}} )


## Development π»

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

## Testing βοΈ

Requirements: Follow the instructions it says in Development

To run the tests:

```shell
   cd app

   source env/bin/activate

   python -m pytest
```

### Authors βοΈ

* **Author:** Steve Matos, <steve.matos.1998@gmail.com>
