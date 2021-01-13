help:
	@echo 'Welcome to my Makefile'

model.pkl: 
	python train.py

train: model.pkl

build: model.pkl Dockerfile.celery Dockerfile.app predict.py
	docker-compose build 

run: model.pkl build
	docker-compose up -d

clean:
	[ -d __pycache__ ] && rm -r __pycache__
	[ -f model.pkl ] && rm model.pkl
	docker-compose down	


