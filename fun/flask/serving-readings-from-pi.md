# Serve readings with a simple *flask* web application

Wouldn't it be great to be able to get instant readings of your apartment's humidity and temperature in the browser?

One possible first step towards that goal is to run a web application locally on the Raspberry Pi.
*Flask* is an extremely easy-to-use web framework that allows us to build such an app without much code.

Our very rudimentary app could consist of a single python file that makes a reading from our sensor and serves a website that displays that very reading.

```
from flask import Flask
import sys
import Adafruit_DHT

app = Flask(__name__)

@app.route('/')
def index():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    return 'Hello!</br>Temperature here in the apartment is {0:0.1f} C.</br>We have a humidity of {1:0.1f} %.'.format(temperature, humidity)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

The above is of course just a prove of concept, not a serious web application.
Save in `app.py` and start up the server with `python app.py`.

By default, *flask* serves the website on port 5000. 
From a device on the same network (e.g. your laptop or mobile phone) you should be able to connect to the website and get your reading by accessing `192.168.0.10:5000` via your browser (replacing 192.168.0.10 by your Raspberry Pi's IP).
