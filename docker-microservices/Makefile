.PHONY: build up down logs shell

build:
	docker compose build --pull

up:
	docker compose up -d --remove-orphans

down:
	docker compose down --volumes --remove-orphans

logs:
	docker compose logs -f

shell:
	docker compose exec api sh
