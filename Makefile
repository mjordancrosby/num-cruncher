tests: unittest e2e
unittest:
	@echo "Running unit tests"
	@python3 -m unittest discover -s tests

e2e:
	@echo "Running end-to-end tests"
	./tests/e2e/runner.sh 