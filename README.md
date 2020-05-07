# RPi4-FM-RDS

FM receiver with RDS for Raspberry Pi, made with GnuRadio 3.7.

## Installation of all dependencies:
``` sudo apt install gnuradio gr-osmosdr gr-rds ```

## How to run:
``` grcc RPi4_FM_RDS.grc -e -d /home/pi ```

Tested and working with Raspberry Pi 4 and generic DVB-T USB receiver with Realtek RTL2838UHIDIR chip (with Rafael Micro R820T tuner), should be working also on Raspberry Pi 3.
