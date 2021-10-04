# created with `cookiecutter https://github.com/zillionare/cookiecutter-pypackage`

install:
	poetry install
	source .venv/bin/activate && pip install kaleido
	source .venv/bin/activate && ipython kernel install --user --name=machine-learning-python

clean:
	rm -rf build .eggs book/_build dist .tox machine_learning_python/__pycache__
	rm -rf machine_learning_python/plotly_theme/__pycache__ tests/__pycache__

# regenerate the book every time there is a change in source files
develop:
	source .venv/bin/activate && find book -path book/_build -prune -false -o \( -name '*.ipynb' -o -name '*.md' -o -name '*.yml' \) | entr jupyter-book build book
