# Setup

There are many online courses explaining different pieces of ML. Very few of them answer how to really apply ML in production problems. We share some best practices on how to build ML systems. All built with simple examples in Python but general enough for non-pythonists too.

## Prepare Working Environment

1. Run `make install` - sets up virtual environment in `.venv` directory and setups dependencies using [Poetry]() config file [pyproject.toml](./pyproject.toml).
2. Run `jupyter lab`
3. Open default [lab url](http://localhost:8888/lab)
4. Open notebook

### Additional Dependencies

1. Install [Graphviz](https://graphviz.org/) to be able to create images of decision trees.

## Editing Jupyter Book Export

```bash
jupyter-book clean book/
jupyter-book build book/
```

It is possible to setup [entr](http://eradman.com/entrproject/) to get the book rebuild with every new .md or .ipynb file saved with

```bash
poetry shell
find book -path book/_build -prune -false -o \( -name '*.ipynb' -o -name '*.md' \) | entr jupyter-book build book
```

Or as simply as `make develop`.

## Editing Slides Export

We use [nbconvert] to prepare reveal.js slides.

```bash
poetry shell
jupyter nbconvert \
    book/imlp/imlp_1_data.ipynb \
    book/imlp/imlp_2_modeling.ipynb \
    book/imlp/imlp_3_experiments.ipynb \
    book/imlp/imlp_4_deep_learning.ipynb \
    --to slides \
    --TagRemovePreprocessor.remove_cell_tags remove_cell \
    --TagRemovePreprocessor.remove_input_tags hide_input \
    --TagRemovePreprocessor.remove_all_outputs_tags hide_output
```

Use following cell tags

* `remove_cell` to completely remove the cell (input and output) from the presentation.
* `hide_input` to hide code cells but to show output.
* `hide_output` to hide output of the cell.

It is possible to setup [entr](http://eradman.com/entrproject/) to get presentations rebuild with every new .md or .ipynb file saved with

```bash
poetry shell
find book -path book/_build -prune -false -o \( -name '*.ipynb' -o -name '*.md' \)
    | entr jupyter nbconvert \
        book/imlp/imlp_1_data.ipynb \
        book/imlp/imlp_2_modeling.ipynb \
        book/imlp/imlp_3_experiments.ipynb \
        book/imlp/imlp_4_deep_learning.ipynb \
        --to slides \
        --TagRemovePreprocessor.remove_cell_tags remove_cell \
        --TagRemovePreprocessor.remove_input_tags hide_input \
        --TagRemovePreprocessor.remove_all_outputs_tags hide_output
        --no-prompt
```
