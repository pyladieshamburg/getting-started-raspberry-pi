# Making Predictions with Temperature Data
- [Setting up Python](#setting-up-python)
- [Exploring Time Series Data](#exploring-time-series-data)
- [Making Univariate Predictions with Temperature Data](#making-univariate-predictions-with-temperature-data)
  + Predictions with SARIMA
  + Predictions with Basic Neural Network
  + Predictions with LSTM
- [Making Multivariate Predictions](#making-multivariate-predictions])


## Setting up Python

To get started you will need  git installed on your computer. 

https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Change to your local user directory.

Let's put our code in a local user directory named 'repo' (You don't have to use the name repo, or any name you like) . Create the directory by using the following commands:

```console
$ cd
mkdir repo
```

Change to the 'repo' directory that you just created. This is where you will place your code. 

```console
cd repo
```

Inside the code directory, clone the repository for this workshop:

```console
repo$ git clone https://github.com/pyladieshamburg/getting-started-raspberry-pi.git
```

Change directory, so that you are inside the cloned repository:

```console
repo$ cd getting-started-raspberry-pi 
```

Create a python virtual environment. The name of the virtual environment is 'env'. You may name the environment whatever you like.

```console
getting-started-raspberry-pi$ python3 -m venv env
```

Activate the newly created virtual environment

```console
getting-started-raspberry-pi$ source env/bin/activate
```

You have successfully activated your environment when the name of your environment is prefixed at the command line:

(env) getting-started-raspberry-pi$ 

Now we need to install the required packages to use the code.


```console
(env) getting-started-raspberry-pi$  pip install -r requirements.txt
```

We must tell Jupyter notebook how to find your python kernel:


```console
(env) getting-started-raspberry-pi$  pip install tornado
(env) getting-started-raspberry-pi$  pip install ipykernel
# Create the kernel (from within the virtual environment that we created above)
(env)$ python -m ipykernel install --user --name env --display-name "PyLadies-Time-Series"
```


Let's look at some code. Start your Jupyter notebook:

```console
(env) getting-started-raspberry-pi$  jupyter-lab
```

## Exploring Temperature and Humidity Data

In the [data-exploration](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/analysis/data-exploration.ipynb) exercise, you create and visualize time series data.
 
You also examine some important characteristics of time series such as seasonality and trend  ad conclude by about learning commons tools for time series analysis.
 
## Making Univariate Predictions with Temperature Data

In these exercises you will experiment with different approaches to making univariate time series with predictions. It is good practice to begin by building simple models as a starting point, before advancing to more complex techniques. 

Based on the findings in a recent study of univariate predictions (https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0194889&type=printable), let's start with a very traditional approach from statistics. 

The [predictions-with-sarima](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/analysis/prediction-with-sarima.ipynb) you  focus on building a SARIMA Model and different ways to select SARIMA hyperparameters.

In the [predictions-with-neural-network](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/analysis/predict-with-nn.ipynb) exercise, you will set up a basic LSTM and experiment with options for training the best model.

In the [predictions-with-lstm](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/analysis/predict-with-lstm.ipynb) exercise, you will set up a basic neural network and experiment with options for training the best model.

## Making Multivariate Predictions

The [prediction-season](https://github.com/pyladieshamburg/getting-started-raspberry-pi/blob/master/analysis/predict-season.ipynb) exercise - for fun - you use both temperature and humidy to predict the season of the year.
