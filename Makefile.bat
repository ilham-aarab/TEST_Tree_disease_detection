.PHONY: build start stop

build:
    @echo "Building Docker images..."
    docker-compose -f docker-compose.yml -f docker-compose.prod.yml build

start:
    @echo "Starting the application..."
    docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

stop:
    @echo "Stopping the application..."
    docker-compose -f docker-compose.yml -f docker-compose.prod.yml down
