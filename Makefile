# created with `cookiecutter https://github.com/zillionare/cookiecutter-pypackage`

install:
	poetry update
	poetry install

dev-install: install
	poetry install -E development
	poetry run ipython kernel install --user --name=machine-learning-python
	poetry run pre-commit install

clean:
	rm -rf build .eggs book/_build dist .tox machine_learning_python/__pycache__
	rm -rf machine_learning_python/plotly_theme/__pycache__ tests/__pycache__

# regenerate the book every time there is a change in source files
develop:
	source .venv/bin/activate && find book -path book/_build -prune -false -o \( -name '*.ipynb' -o -name '*.md' -o -name '*.yml' \) | entr jupyter-book build book
