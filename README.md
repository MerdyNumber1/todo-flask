# TODO App on Flask

## Installation:
```sh
$ cp .env.example .env  # set services env vars here
$ cd app 
$ cp .env.example .env  # set app env vars here
```
#### For development:
```sh
$ make dev-build
$ make dev
```
#### For production:
```sh
$ make prod-build
$ make prod
```
#### Then make migrations:
```sh
$ make migration
```