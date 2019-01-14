# Storing sensor data in the IOTA tangle

So we've manage to read data from the sensor and we also saw how we can send data to IOTA. What we need to do next is have a script which reads data from the sesor periodically (e.g. 5 mins) and sends it to the IOTA tangle. Also this program should run all the time.. also it should restart in case it dies (if the RaspberryPi gets turned off and on again).

## Sending the data to IOTA

We should select a unique seed/address pair for the collecting the sensor data. The seed/address values are stored in tangle/config. The seed in seed_tan.conf and the address in address_pi.conf. These files have to be copied on the raspberryPi.

The code in [collect_and_send.py](collect_and_send.py) combines the sensor reading from [read_temperature_and_humidity.py](../sensorsetup/read_temperature_and_humidity.py) and [send_data.py](../tangle/send_data.py)

## Supervisord

We want our script to start when the pi boots up and restart when it fails. 
An easy way to do this is to use *supervisord*.

Our instructions here closely follow 
[https://serversforhackers.com/c/monitoring-processes-with-supervisord](https://serversforhackers.com/c/monitoring-processes-with-supervisord).

Install *supervisord* with the package manager.

```sudo apt-get install -y supervisor```

And start it up.

```sudo service supervisor start```

Create a directory where the output and error logs from the script can go.

```mkdir /var/log/iotastream```

Create a *supervisord* configuration file `iotastream.conf` for the script and store 
it in *supervisord*'s config folder `/etc/supervisord/conf.d/`. 
You might need `sudo` to save the file in this location.

```
[program:iotastream]
command=/usr/bin/python3 /home/pi/repos/getting-started-raspberry-pi/pitangle/collect_and_send.py
directory=/home/pi/repos/getting-started-raspberry-pi/pitangle
autostart=true
autorestart=true
startretries=3
stderr_logfile=/var/log/iotastream/iotastream.err.log
stdout_logfile=/var/log/iotastream/iotastream.out.log
user=pi
```

Tell supervisord to reload the configuration.

```
sudo supervisorctl reread
sudo supervisorctl update
```

If we did everything right, we should now see the python process running.
You can check with `sudo supervisorctl` (hit control+d to exit).
We should also see the python script in the list of active processes when running
`ps aux | grep python`.

If the output of the above commands indicates that script failed and was terminated, we can check the error log in 
`/var/log/iotastream/iotastream.err.log` to see what went wrong.


## Reading the data from IOTA

You can read data published to the address you sent the data to, once some data gets collected.

Until then we could look at some of the data uploaded already to the address_dump.conf address.. by running [data_reading_to_json.py](data_reading_to_json.py).

Later on update the script to use the address_pi.conf address to read your own data.