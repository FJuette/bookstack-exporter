CURRENT_DIR := $(shell pwd)

run:
	pip freeze > requirements.txt
	cd app && python main.py -f html

docker:
	pip freeze > requirements.txt
	docker build -t bookstack-exporter .
	# docker run --name bookstack-exporter --rm -v "/$(CURRENT_DIR)/export":/export bookstack-exporter

lint:
	python -m flake8 ./app
	python -m pylint ./app
	python -m mypy ./app
