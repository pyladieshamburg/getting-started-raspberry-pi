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
