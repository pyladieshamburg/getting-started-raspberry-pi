# -*- coding: utf-8 -*-

import time
import datetime as dt
import matplotlib.pyplot as plt
import Adafruit_DHT

# Create figure for plotting
fig, ax = plt.subplots()

xs = []
y1s = []
y2s = []

# Sample temperature 10 times every 2 seconds
for t in range(0, 10):

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    
    # Add x and y to lists
    timestamp = dt.datetime.now().strftime('%H:%M:%S')
    xs.append(timestamp)
    y1s.append(humidity)
    y2s.append(temperature)
    print('Time: {0} Temp: {1:0.1f} C  Humidity: {2:0.1f} %'.format(timestamp, temperature, humidity))

    # Wait 2 seconds before sampling temperature again
    time.sleep(2)

# Draw plot
ax.plot(xs, y1s, 'b:', label='Humidity (%)')
ax.plot(xs, y2s, 'r-', label='Temperature (C)')
ax.tick_params(axis='x', rotation=45)
ax.legend()

# Draw the graph
plt.title('DHT11 Humidity and Temperature over Time')
plt.show()

