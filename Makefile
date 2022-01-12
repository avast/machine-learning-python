install:
	poetry update
	poetry install

install-dev: install
	poetry install -E development
	poetry run ipython kernel install --user --name=machine-learning-python
	poetry run pre-commit install

clean:
	rm -rf build .eggs book/_build dist .tox machine_learning_python/__pycache__
	rm -rf machine_learning_python/plotly_theme/__pycache__ tests/__pycache__

# regenerate the book every time there is a change in source files
develop-book:
	source .venv/bin/activate \
	&& find book -path book/_build -prune -false -o \( -name '*.ipynb' -o -name '*.md' -o -name '*.yml' \) \
	| entr jupyter-book build book

# regenerate the book every time there is a change in source files
develop-presentation:
	source .venv/bin/activate \
	&& find book -path book/_build -prune -false -o \( -name '*.ipynb' -o -name '*.md' -o -name '*.yml' \) \
	| entr jupyter nbconvert \
		book/imlp/imlp_1_data.ipynb \
		book/imlp/imlp_2_modeling.ipynb \
		book/imlp/imlp_3_experiments.ipynb \
		book/imlp/imlp_4_deep_learning.ipynb \
		--to slides \
		--TagRemovePreprocessor.remove_cell_tags remove_cell \
		--TagRemovePreprocessor.remove_input_tags hide_input \
		--TagRemovePreprocessor.remove_all_outputs_tags hide_output \
		--no-prompt

presentations:
	source .venv/bin/activate \
	&& jupyter nbconvert \
		book/imlp/imlp_1_data.ipynb \
		book/imlp/imlp_2_modeling.ipynb \
		book/imlp/imlp_3_experiments.ipynb \
		book/imlp/imlp_4_deep_learning.ipynb \
		--to slides \
		--TagRemovePreprocessor.remove_cell_tags remove_cell \
		--TagRemovePreprocessor.remove_input_tags hide_input \
		--TagRemovePreprocessor.remove_all_outputs_tags hide_output \
		--no-prompt
