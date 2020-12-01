# TODO App on Flask

## Installation:
```sh
$ cp .env.example .env  # set services env vars here
$ cd app 
$ cp .env.example .env  # set app env vars here
$ cd src/static && yarn install && cd ../../..
```
#### For development:
```sh
$ docker-compose --file docker-compose.dev.yml up --build
```
#### For production:
```sh
$ docker-compose --file docker-compose.prod.yml up --build
```
### Then make migrations
```sh
$ docker-compose exec web pipenv run flask db upgrade
```