check:
	poetry run pylint pylint_single_element_destructuring
	poetry run black --check .
	poetry run pytest tests/

format:
	poetry run black .