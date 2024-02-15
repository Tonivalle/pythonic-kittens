SRC_DIR		= src
TEST_DIR	= tests
CHECK_DIRS = $(SRC_DIR) $(TEST_DIR) $(SCRIPTS_DIR)
PYTEST_FLAGS = -vv

.PHONY: check
check: format-check lint type-check test ## Launch all the checks

.PHONY: format
format: ## Format repository code
	poetry run black $(CHECK_DIRS)
	poetry run isort $(CHECK_DIRS)

.PHONY: format-check
format-check: ## Check the code format with no actual side effects
	poetry run black --check $(CHECK_DIRS)
	poetry run isort --check $(CHECK_DIRS)

.PHONY: install
install: ## Install dependencies
	poetry run pip install --upgrade pip
	poetry install -v

.PHONY: lint
lint: ## Launch the linting tool
	poetry run pylint -j 0 $(SRC_DIR).pythonic_kittens
	poetry run pylint -j 0 -d missing-function-docstring -d missing-class-docstring -d redefined-outer-name $(TEST_DIR)

.PHONY: lock
lock: ## Update the poetry.lock file
	poetry lock

.PHONY: test
test: ## Launch the tests
	poetry run pytest $(PYTEST_FLAGS) $(TEST_DIR)

.PHONY: type-check
type-check: ## Launch the type checking tool
	poetry run mypy $(CHECK_DIRS)

.PHONY: update
update: ## Update python dependencies
	poetry update

.PHONY: help
help: ## Show the available commands
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
