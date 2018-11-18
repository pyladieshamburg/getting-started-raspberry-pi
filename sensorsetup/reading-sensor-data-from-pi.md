Now that we've set up our Raspberry Pi, it should have a Linux operating system on it and nothing more.

For collecting the data from DHT11 sensor we will follow the [Circuitbasics DHT11 tutorial](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi) and focus on the python part.

## The Software side

But first for some necessary setup on the software side.

### Installing python and other libraries

Python 3 and pip
```bash
sudo apt-get install python3-dev python3-setuptools build-essential
sudo apt-get install python3-pip
```

Git: we will need this for sure for when we get lots of code
```bash
sudo apt-get install git-core
```

Vim: unless you want to explore the ssh connection capabilities of your favored code editor.
```bash
sudo apt-get vim
```
A recommended minimal configuration would be:
```
# change tabstop and shiftwidth to taste (e.g. you might prefer two instead of the given four spaces) 
set nocompatible
set tabstop=4
set shiftwidth=4
set expandtab
set number
syntax on
```
Put this in a file named .vimrc in your Raspberry Pi's home directory.

AdaFruit: Python library to read the DHT series of humidity and temperature sensors
```bash
sudo pip3 install Adafruit_DHT
```


## The Hardware part

What are all those pins

![Raspberry Pins](https://www.rs-online.com/designspark/rel-assets/dsauto/temp/uploaded/githubpin.JPG)
