



.PHONY: all unittest e2e tests build

all: tests build

unittest:
	@echo "Running unit tests"
	@python3 -m unittest discover -s tests

e2e:
	@echo "Running end-to-end tests"
	./tests/e2e/runner.sh 

tests: unittest e2e

build:
	@echo "Building the project"
	@docker build -t solution .


