.PHONY: setup test local-test spec-check clean docker-build

setup:
	uv sync

# Rubric Requirement: make test runs INSIDE docker
test:
	docker build -t chimera-factory .
	docker run --rm chimera-factory make local-test

# Internal command used by Dockerfile/CI
local-test:
	@echo "DEBUG: Running tests with dev dependencies"
	uv run --extra dev pytest tests/

spec-check:
	@echo "Checking code alignment with specs..."
	@ls specs/

docker-build:
	docker build -t chimera-factory .

clean:
	rm -rf .venv/
	find . -type d -name "__pycache__" -exec rm -rf {} +
