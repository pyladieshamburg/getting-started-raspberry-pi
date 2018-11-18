# -*- coding: utf-8 -*-

import time
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Adafruit_DHT

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xs = []
ys = []

ax.plot(xs, ys, 'r^', label='Humidity')
ax.tick_params(axis='x', rotation=45)
ax.set_ylabel('Humidity (%)')
plt.title('DHT11 Humidity over Time')

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    # Read sensor data
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    
    # Add readings to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(humidity)
    print('Humidity: {0:0.1f} %'.format(humidity))

    # Limit data arrays to 10 most recent readings
    xs = xs[-20:]
    ys = ys[-20:]
    
    # Update plot
    ax.clear()
    ax.plot(xs, ys)

# Draw the graph
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=5000)
plt.show()

