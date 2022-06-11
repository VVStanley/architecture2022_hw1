test:
	pytest tests/test_quadratic_equation.py

linter:
	flake8 .

mypy:
	mypy .
