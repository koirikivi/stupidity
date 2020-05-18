usage:
	@echo Usage: make [$$(cat Makefile | grep -vPe '^\t|^\.|^$$' | sed 's/:$$//g' | paste -sd "|" -)]

test:
	pytest

watch:
	pytest-watch

publish: dist | test
	twine upload dist/*

dist: README.md *.py stupidity
	rm -rf dist
	python setup.py sdist

.PHONY: usage test watch publish
