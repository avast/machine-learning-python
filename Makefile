install:
	python -m pip install virtualenv
	python -m virtualenv venv
	source venv/bin/activate && python -m pip install -r requirements.txt
	source venv/bin/activate && ipython kernel install --user --name=machine-learning-python

clean:
	rm -rf build
