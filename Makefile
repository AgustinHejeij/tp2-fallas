run:
	docker build  -f Dockerfile . --rm  -t tu_destino
	docker run --publish 8000:8000 -e PORT=8000 --rm -it tu_destino
