build:
	docker-compose -f local.yml up --build
up:
	docker-compose -f local.yml up
 debug:
	docker-compose -f local.yml run --service-ports -e DEBUGGER=True web /start-reload.sh