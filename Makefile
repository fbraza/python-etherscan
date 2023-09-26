.PHONY : install
install:
	pre-commit install
	pip install pip-tools
	pip-compile requirements-dev.in
	pip install -r requirements-dev.txt

.PHONY : upgrade
upgrade:
	pip-compile requirements-dev.in --upgrade
	pip install -r requirements-dev.txt
	pre-commit autoupdate

# --- CI instructions

.PHONY : lint
lint:
	pre-commit run --all-files

.PHONY : test
test:
	coverage erase; coverage run --source . -m pytest tests/ -v --durations=5; coverage report --skip-empty --omit "tests/*" -m
