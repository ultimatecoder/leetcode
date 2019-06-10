init:
	pip install pipenv
	pipenv install --dev
unit-test:
	pipenv run pytest
end-to-end-test:
	cucumber
lint:
	@echo "Running Static Type Checker"
	@echo "#################################"
	pipenv run mypy solutions
