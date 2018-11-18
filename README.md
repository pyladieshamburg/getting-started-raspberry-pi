# getting-started-raspberry-pi

This tutorial will have several parts. As and end result we want to have a web site which show different information from inside our flats: temperature, humidity, dust, light... and which also predict the values.

There are several things that are involved in this project: setting up a raspberry pi, setting up sensors and collecting sensor readings, storing the readings. 
On the consumer side we will have to read the data, analyse it, display it, train some models, write a website and deploy it.

This will all be done with Python.

## Things you will need:

* Raspberry PI 3 or higher
* Charger: mini-usb phone charger should work
* Micro SD card: at least 8G
* Bread board
* Sensors, can be the DHT11, or equivalent
* One LED... just for fun
* Connecting cables


## Part 1 - Setting up your brand new Raspberry Pi

In this part we will just set things up. Follow the instructions in [raspberry-pi-setup](pisetup/raspberry-pi-setup.md).

## Part 2 - Connecting a sensor to your Raspberry Pi

Using a breadboard and three cables, we'll connect the Raspberry Pi to a DHT11 temperature and humidity sensor.
See [reading-sensor-data-from-pi](sensorsetup/reading-sensor-data-from-pi.md) for instructions on how to do the wiring. 
You'll also find a Python script that shows an example of how to get readings from the sensor using the *Adafruit_DHT* library.

## (Optional) Part 3 - Plotting your sensor readings with *matplotlib*

Head over to [plotting-readings-from-pi](fun/matplotlib/plotting-readings-from-pi.md) if you want to plot the sensor data you collect as a time series graph with *matplotlib*. 

## (Optional) Part 4 - Serving readings from your Pi with *flask*

In [serving-readings-from-pi](fun/flask/serving-readings-from-pi.md) you find inspiration about how to use Python's web framework *flask* to deploy a super simple web app that runs locally on your Raspberry Pi and serves the current temperature and humidity.
  