unit-test:
	pytest
end-to-end-test:
	cucumber
lint:
	@echo "Running Static Type Checker"
	@echo "#################################"
	mypy solutions
