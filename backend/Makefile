build:
	docker build -t grafos1 .
run:
	docker run -d -p 8080:8080 -e PORT="8080" --name grafos_web grafos1
start:
	docker start grafos_web
logs:
	docker logs -f grafos_web
stop:
	docker stop grafos_web