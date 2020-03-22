src=src docker/env_util/*.py

.PHONY: check
check:
	mypy ${src}
	flake8 ${src}
	pylint ${src}
	isort --check --recursive ${src}
	black --check ${src}

.PHONY: format
format:
	isort --recursive ${src}
	black ${src}
