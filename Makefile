run:
	uvicorn app:app --host 0.0.0.0 --port 8000 --reload

compile:
	uv pip compile requirements.in > requirements.txt
	uv pip compile requirements-dev.in > requirements-dev.txt

install:
	uv pip install -r requirements.txt -r requirements-dev.txt

db:
	docker compose up -d

db-stop:
	docker compose down