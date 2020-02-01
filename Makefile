check:
	poetry run pylint pylint_single_element_destructuring
	poetry run black --check .
	poetry run pytest --cov-report html:cov_html --cov=pylint_single_element_destructuring

format:
	poetry run black .