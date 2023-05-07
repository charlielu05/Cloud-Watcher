SHELL := /bin/bash

start-api:
	. .cw/bin/activate
	cd ./src
	uvicorn w2:app --reload
	
python-env:
	python -m venv .cw 
	. .cw/bin/activate 
	pip-compile ./requirements.in
	pip install --upgrade pip 
	pip install -r ./requirements.txt

pytest:
	. .cw/bin/activate
	python -m pytest

start-local-dynamodb:
	docker-compose up -d

stop-local-dynamodb:
	docker-compose down

cw-dev: 
	source env.sh
	. .cw/bin/activate
	python -i ./src/cw.py

.PHONY: *
.ONESHELL:
.SILENT: