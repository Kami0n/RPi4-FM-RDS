# RPi4-FM-RDS

GnuRadio 3.7 FM receiver with RDS for Raspberry Pi.

## Installation of all dependencies:
sudo apt install gnuradio gr-osmosdr gr-rds

## How to run:
grcc RPi4_FM_RDS.grc -e -d /home/pi

Tested and working with Raspberry Pi 4, should be working also on Raspberry Pi 3.
