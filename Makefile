FOLDERS=pylint_single_element_destructuring tests examples

check:
	poetry run pylint pylint_single_element_destructuring
	poetry run black --check ${FOLDERS}
	poetry run pytest --cov-report html:cov_html --cov=pylint_single_element_destructuring

format:
	poetry run black ${FOLDERS}
