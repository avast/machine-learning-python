install:
	python -m pip install virtualenv
	python -m virtualenv venv
	source venv/bin/activate && python -m pip install poetry
	source venv/bin/activate && poetry install -E book -E dev -E test
	source venv/bin/activate && ipython kernel install --user --name=machine-learning-python

clean:
	rm -rf build .eggs book/_build dist .tox machine_learning_python/__pycache__
	rm -rf machine_learning_python/plotly_theme/__pycache__ tests/__pycache__
