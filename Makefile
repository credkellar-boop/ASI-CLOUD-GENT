.PHONY: setup run test docker-build docker-up clean

setup:
	chmod +x setup.sh && ./setup.sh

run:
	.venv/bin/python main.py

test:
	.venv/bin/pytest tests/ --verbose

docker-build:
	docker compose build

docker-up:
	docker compose up -to

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf .venv
