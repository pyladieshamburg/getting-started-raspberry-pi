## Setting up the  your brand new Raspberry Pi

There are two ways to setup a new Raspberry Pi. With connection to peripherals (monitor, keyboard, mouse) or headless.
The first step of flashing an image of Raspian OS onto an SD card is the same for both ways.

### Prepare SD card with Raspian image

Raspian is the officially recommended Linux distribution for general use of the Raspberry Pi.
Get an image of Raspian OS from [Raspberry Pi Foundation](https://www.raspberrypi.org/downloads/raspbian/)
(get Raspbian Stretch with desktop).

You can choose between two options for flashing the Raspian image onto SD card.
The safe option is to use Etcher, a graphical SD card writing tool that works on Mac OS, Linux and Windows.
The second option is to flash the image onto the SD card with the help of command line tools that come with your operating system.
This works for Mac OS and Linux and doesn't require you to download an additional tool.

Both options are described in the section on installing OS images in the Raspberry Pi Foundation documentation.
[This page](https://www.raspberrypi.org/documentation/installation/installing-images/) outlines the process using Etcher (including a download link for Etcher). 
On the bottom of the same page, you find links to pages that describe how to flash the image using command lines tools for [Mac OS](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md) and [Linux](https://www.raspberrypi.org/documentation/installation/installing-images/linux.md).

### Graphical setup

If everything went as planned in the previous step, you should now be able to insert your SD card into its slot on the Raspberry Pi and boot the OS from there.
If you have a monitor, HDMI cable, mouse and keyboard available, you can connect them with your Raspberry Pi *before* plugging in the charger.
That way, you can configure wifi graphically after the OS has booted. 
Select the wifi you want to connect to by clicking on the wifi symbol in the upper right corner.

You may still want to configure ssh in order to be able to connect to the pi from your laptop.
Once you're connected to the wifi, you can find out your Raspberry Pi's local IP by opening the terminal and running:
```bash
ifconfig | grep inet
```
Enable ssh in the menu that opens by clicking on the Raspberry Pi Menu Icon in the upper left corner → Preferences → Raspberry Pi Configuration.
Now you're all set to ssh into your pi (see below for more information).

If you don't have a monitor, HDMI cable, mouse and keyboard handy, go with the headless setup described below instead.

### Headless setup

For the headless setup we'll be proceeding according to the steps outlined in [setting-up-a-raspberry-pi-without-keyboard-and-mouse-headless](https://medium.com/@maheshsenni/setting-up-a-raspberry-pi-without-keyboard-and-mouse-headless-9359e0926807).

#### Setup wifi and ssh

Your SD card should now have a boot partition. Navigate to id and add an ssh file.
```bash
cd /Volumes/boot
touch ssh
```

Create a new file: *wpa_supplicant.conf* and add the wifi info (change country code if not DE):

```bash
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev update_config=1 country=DE

network={
    ssid="<SSID>"
    psk="<password>"
    key_mgmt=WPA-PSK
}
```

### Install the OS and connect to your Raspberry

At this point, if all went well, it should be enough to insert the SD card into your Raspberry Pi. Plug in your Raspberry Pi connect via SSH.

In order to connect via ssh you will have to find the IP of your Device. For this install *nmap* (available in your Linux or MacOS package manager or from http://nmap.org/download.html) and run

```bash
nmap -sn 192.168.0.5/24
```

The last IP should be the one you are looking for. 

Alternatively, you can try:
```bash
arp -a | grep "b8:27:eb"
```
This scans the local network and greps for IP addresses that are associated with a Raspberry Pi hardware address.

Connect then via ssh (exchange the IP 192.168.0.10 for the IP of your Raspberry Pi).

```bash
ssh pi@192.168.0.10
```

At this moment the password should be still the default one.

Copying files from and to your Raspberry Pi with scp might also come in handy at some point.
To copy a file named `file-on-my-machine` on your laptop to your Raspberry Pi's home directory, use the following:

```bash
scp file-on-my-machine pi@192.168.0.10:/home/pi
```

Or, the other way round, you can copy a file named `file-on-my-pi` from your Raspberry Pi's home directory to a directory on your laptop.

```bash
scp pi@192.168.0.10:/home/pi/file-on-my-pi dir-on-my-machine
```

### Changing your Pi's hostname

By default your Raspberry Pi's hostname is raspberrypi. 
You can use that hostname and the suffix ".local" instead the Pi's local IP to ssh into it.

Like so:

```ssh pi@raspberrypi.local```

That's handy because you don't have to take the trouble of figuring out your Pi's local IP.
But it only works if your Raspberry Pi is the only one around in your local network. 
As soon as there's more than one Pi with this hostname, you can't be sure which one you're connecting to with the above command.

So, in order to take advantage of this convenient way of connecting to the Pi in a workshop setting, it's a good idea to change your Pi's hostname at home.

Say I like Korean food and I want to change my Pi's hostname to *bibimbap123*. 
One way to do this is to go and modify `/etc/hostname` and `/etc/hosts`, and change `raspberrypi` into `bibimbap123` in both files.
You'll need to `sudo vim /etc/hostname` and `sudo vim /etc/hosts`, make the change and save to achieve this.

Another option is to change the hostname via the Raspbian commandline config tool `raspi-config`. 
It opens when you issue 

```sudo raspi-config```

on the commandline. A dialog box will open. Choose `2 Network Options` with the arrow keys and hit enter.
Choose `N1 Hostname` and follow the instructions.

In both cases, reboot to see the hostname change take effect. No you can use

```ssh pi@bimbimbap123.local```

to ssh into your Raspberry Pi.






