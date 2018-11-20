# Reading sensor data

Now that we've set up our Raspberry Pi, it should have a Linux operating system on it and nothing more.

For collecting the data from DHT11 sensor we will follow the [Circuitbasics DHT11 tutorial](http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi) and focus on the python part.

## The Software side

But first for some necessary setup on the software side.

### Installing python and other libraries

Python 3 and pip
```bash
sudo apt-get update
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
A recommended minimal configuration to be put in a file named .vimrc in your Raspberry Pi's home directory would be:
```
# change tabstop and shiftwidth to taste (e.g. you might prefer two instead of the given four spaces) 
set nocompatible
set tabstop=4
set shiftwidth=4
set expandtab
set number
syntax on
```

AdaFruit: Python library to read the DHT series of humidity and temperature sensors
```bash
sudo pip3 install Adafruit_DHT
```

## The Hardware part

The 40 GPIO pins above the Raspberry Pi logo an important connection point of our Raspberry Pi to the outside world.
The GPIO pins allow us to control electric circuits from the Raspberry Pi. 
We thereby can control all kinds of devices and, in particular, receive data from sensors.

![Raspberry Pins](https://www.rs-online.com/designspark/rel-assets/dsauto/temp/uploaded/githubpin.JPG)

What are all those pins?

There are two 3.3V pins in **yellow** and two 5V pins in **red**.
**Black** are the eight ground pins. 
The other pins in blue, green, pink and orange are all general purpose pins that can be used for both input or output.
The non-orange ones of the pins can also communicate with special interfaces using the appropriate protocols, on top of their general purpose.
The two grey ones are reserved for other special use cases that aren't of our concern here.

For the sensor setup, we'll be using pins number 2 (5V), 4 (GND) and 7 (GPIO4).
We'll connect pin 2 (5V) to the sensor's positive pole and pin 4 (GND) to its negative pole, thus forming the basis for an electric circuit.
Pin 7 (GPIO4) will connect to the sensor's signal pin so that we can get readings.
![DHT11 pins](https://mounishkokkula.files.wordpress.com/2017/02/dht11-pinout-for-three-pin-and-four-pin-types-21.jpg)

The resulting circuit should look similar to this:

![Circuit diagram](https://mounishkokkula.files.wordpress.com/2017/02/raspberry-pi-dht11-ssh-terminal-output1.png?w=1338&h=582) 

Note that we could have chosen any other 3.3/5V pin instead of pin 2, any other ground pin instead of pin 4, and any other general purpose pin instead of pin 7.

And in case you wondered how the cables make a connection to the right sensor pins just by us plugging them in the same vertical row on the bread board:
all 5 hole vertical rows that we see on the bread board are connected with metal stripes.
This is how a board looks like from the bottom with the cover removed:

![Breadboard under the hood](https://cdn.sparkfun.com/r/600-600/assets/e/7/7/e/c/5175c500ce395f5a49000004.jpg)

For more details, see [https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all).

The *Adafruit_DHT* library provides us with a high level interface to get readings from the sensor.
We will adapt their sample code to test if our circuit setup works alright.
If you want, you can save the following code in a file `read_temperature_and_humidity.py` and run it with `python read_temperature_and_humidity.py`.

```
#!/usr/bin/python
import sys
import Adafruit_DHT

sensor = 11
pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
```