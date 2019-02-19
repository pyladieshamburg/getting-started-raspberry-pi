# Making Predictions with Temperature Data
- [Setting up Python](#setting-up-python)
- [Exploring Time Series Data](#exploring-time-series-data)
- [Making Univariate Predictions with Temperature Data](#making-univariate-predictions-with-temperature-data)
  + Predictions with SARIMA
  + Predictions with Basic Neural Network
  + Predictions with LSTM
- [Making Multivariate Predictions](#making-multivariate-predictions])


## Setting up Python

To get started, you will need to have Python, pip and  Jupyter Notebook installed.

To set up your Python environment, follow the instructions in repository: [getting-started-with-python](https://github.com/pyladieshamburg/getting-started-with-python/blob/master/README.md)

Change directory to a location where you want to place your code. We will use the  name this  'repo' as an example.

```console
~$ cd repo
```

Inside the code directory, clone the repository for this workshop

```console
repo $ git clone https://github.com/pyladieshamburg/getting-started-raspberry-pi.git
```

Change directory to the cloned repository:

```console
repo $ cd getting-started-raspberry-pi 
```

Create a python virtual environment:

```console
getting-started-raspberry-pi  $ python3 -m venv env
```

Activate the newly created virtual environment

```console
getting-started-raspberry-pi  $ source env/bin/activate
```

You have succussfully activated your enviroment when the name of your environment is prefixed at the command line:

```console
(env) getting-started-raspberry-pi  $ source env/bin/activate
```


## Exploring Temperature and Humidity Data

In the [data-exploration](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/analysis/data-exploration.ipynb) exercise, you create and visualize time series data.
 
You also examine some important characteristics of time series such as seasonality and trend  ad conclude by about learning commons tools for time series analysis.
 
## Making Univariate Predictions with Temperature Data

In these exercises you will experiment with different approaches to making univariate time series with predictions.

Before you build use complex techniques for univariate time series prediction, traditional approaches should also be implemented as a baseline. The [predictions-with-sarima](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/analysis/prediction-with-sarima.ipynb) you  focus on building a SARIMA Model and different ways to select SARIMA hyperparameters.

In the [predictions-with-neural-network](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/analysis/predict-with-nn.ipynb) exercise, you will set up a basic LSTM and experiment with options for training the best model.

In the [predictions-with-lstm](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/analysis/predict-with-lstm.ipynb) exercise, you will set up a basic neural network and experiment with options for training the best model.

## Making Multivariate Predictions

The [prediction-season](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/analysis/predict-season.ipynb) exercise - for fun - you use both temperature and humidy to predict the season of the year.
