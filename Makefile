help:
	@echo 'Demo Flask App w/ Celery Backend for ML Predictions'
	@echo '==================================================='
	@echo 'Options:'
	@echo '----------------------------------------------------'
	@echo 'help   ->  Print this help message (default)'
	@echo 'train  ->  Train a new model and save it as model.pkl'
	@echo 'build  ->  Build docker images for celery & flask'
	@echo 'run    ->  Run docker compose: redis, celery & flask'
	@echo 'rund   ->  Run docker compose: redis, celery & flask (detached)'
	@echo 'clean  ->  Tear down docker containers, remove images'
	@echo 'all    ->  Runs: train, build, run & clean'
	@echo '----------------------------------------------------'
	@echo ''

model.pkl: 
	python train.py

train: model.pkl

build: model.pkl Dockerfile.celery Dockerfile.app predict.py
	docker-compose build 

rund: model.pkl build
	docker-compose up -d

run: model.pkl build
	docker-compose up

clean:
	docker-compose down	--rmi all --remove-orphans
	[ -d __pycache__ ] && rm -r __pycache__
	[ -f model.pkl ] && rm model.pkl

all: train build run clean
	

