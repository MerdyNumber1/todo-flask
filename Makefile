dev-build:
	docker-compose --file docker-compose.dev.yml build

dev:
	docker-compose --file docker-compose.dev.yml up

dev-down:
	docker-compose --file docker-compose.dev.yml down

prod-build:
	docker-compose --file docker-compose.prod.yml build

prod:
	docker-compose --file docker-compose.prod.yml up

prod-down:
	docker-compose --file docker-compose.prod.yml down

migration:
	docker-compose -f docker-compose.dev.yml -f docker-compose.prod.yml exec web pipenv run flask db upgrade
