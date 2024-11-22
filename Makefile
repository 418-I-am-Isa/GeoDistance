run:
	fastapi dev geo_distance/main.py

install:
	poetry install

update:
	poetry update

clear_poetry_cache:
	poetry cache clear . --all

black:
	poetry run black .

isort:
	poetry run isort .

flake8:
	poetry run flake8 .


pylint:
	git ls-files -- '*.py' | \
	xargs poetry run pylint --disable=R,C


ruff:
	poetry run ruff check . --preview --fix

format_code: black isort ruff flake8 pylint