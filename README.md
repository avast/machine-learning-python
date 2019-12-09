# Machine Learning in Python

There are many online courses explaining different pieces of ML. Very few of them answer how to really apply ML in production problems. We share some best practices on how to build ML system. All built with simple examples in Python but general enough for non-pythonists too.

This course [Introduction to Machine Learning with Python](https://www.cerge-ei.cz/economics-discovery-hub/2019-11-13/introduction-to-machine-learning-with-python) was lectured by [Avast](http://www.avast.com) as part of [Economics Discovery Hub](https://www.cerge-ei.cz/discovery/) at [CERGE-EI](https://www.cerge-ei.cz/).

This course covers:

1. [Data](./imlp_1_data.ipynb)
Given data it is quite simple to build some models. We go through typical modeling workflow from data exploration, feature engineering, to modeling on a complete worked-out example, discuss options and tradeoffs.

2. [ML in Production](./imlp_2_modeling.ipynb)
We test several models in laboratory conditions. We try to extract some knowledge from the model to help us with stakeholders’ buy-in. We move the best model from messy notebooks into production. We give an overview of techniques used to ease transition from development to production and how to keep the model running well.

3. [Experimentation](./imlp_3_experiments.ipynb)
There is no improvement without failures, we have to know what works and what does not. We give examples of basic techniques to run controlled experiments and learn from them. We help to communicate results in natural language and how to get most of the value from the experiment using Bayesian approach.

4. [Deep Learning](./imlp_4_deep_learning.ipynb)
Deep learning helps where traditional techniques stop. It does not need to be too difficult and technical to implement. We give an example of a problem solved using deep net, what are common pitfalls and how to evade them.

## Course Materials

You can browse notebooks in git see [Lesson 1 Notebook](./imlp_1_data.ipynb). If you want to follow the course in code and play with notebooks, you need to setup your own python and Jupyter notebook environment.

## Prepare Working Environment

1. Install Python 3.7 Miniconda - [here](https://docs.conda.io/en/latest/miniconda.html)
2. Using Miniconda default python environment install following packages `conda install scikit-learn seaborn pandas numpy graphviz scipy`
3. Install additional packages `conda install -c conda-forge pydotplus xgboost lime shap jupyterlab`
4. Install [TensorFlow](https://www.tensorflow.org/install) `pip install tensorflow`

## Viewing and Editing Notebooks

1. Clone this repository
1. Navigate to the local repository files
1. Run `jupyter lab`
1. Open default [lab url](http://localhost:8888/lab)
1. Open notebook
