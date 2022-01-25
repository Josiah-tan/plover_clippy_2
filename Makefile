.PHONY: docs

docs: README.org
	pandoc -s README.org -o README.md
