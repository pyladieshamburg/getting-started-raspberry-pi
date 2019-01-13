# Storing sensor data in the IOTA tangle

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