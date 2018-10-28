## Setting up the  your brand new Raspberry Pi

There are two ways to setup a new Raspbery Pi. With connection to periferals (monitor, keyboard, mouse) or headless.

### Headless setup

Following instructions from [setting-up-a-raspberry-pi-without-keyboard-and-mouse-headless](https://medium.com/@maheshsenni/setting-up-a-raspberry-pi-without-keyboard-and-mouse-headless-9359e0926807)

Get image from [Raspberr Pi](https://www.raspberrypi.org/downloads/raspbian/)
(the light version is fine)

Connect SD card to pc, (it should be formatted), and write the downloaded image to it:

(change to the folder you downloaded the img file to)
sudo dd bs=1m if=2018-10-09-raspbian-stretch-lite.img  of=/dev/rdisk2 conv=sync

### Setup wifi and ssh

SD card should now have a boot partition, navigate to id and add an ssh file
```bash
cd /Volumes/boot
touch ssh
```

Creata a new file: *wpa_supplicant.conf* and add the wifi info (change country code if not DE):

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

In order to connect via ssh you will have to find the IP of your Device. For this install *nmap* and run

```bash
nmap -sn 192.168.0.5/24
```

The last IP should be the one you are looking for. 
Connect then via ssh

```bash
ssh pi@192.168.0.10
```

At this moment the password should be still the default one.
