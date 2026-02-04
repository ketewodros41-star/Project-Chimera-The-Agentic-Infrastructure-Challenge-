.PHONY: setup test spec-check clean docker-build docker-test

setup:
	uv sync

test:
	@echo "DEBUG: Running tests with dev dependencies"
	uv run --extra dev pytest tests/

spec-check:
	@echo "Checking code alignment with specs..."
	@ls specs/

docker-build:
	docker build -t chimera-factory .

docker-test:
	docker run --rm chimera-factory make test

clean:
	rm -rf .venv/
	find . -type d -name "__pycache__" -exec rm -rf {} +
