# Setup

There are many online courses explaining different pieces of ML. Very few of them answer how to really apply ML in production problems. We share some best practices on how to build ML systems. All built with simple examples in Python but general enough for non-pythonists too.

## Prepare Working Environment

1. Run `make install` - sets up virtual environment in `venv` directory and installs dependencies from `requirements.txt`
2. Run `jupyter lab`
3. Open default [lab url](http://localhost:8888/lab)
4. Open notebook

## Editing Jupyter Book Export

```bash
jupyter-book clean book/
jupyter-book build book/
```