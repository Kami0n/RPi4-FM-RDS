# RPi4-FM-RDS

FM (mono) receiver analyzer with RDS optimized for Raspberry Pi 4, made with GnuRadio 3.7.

## Installation of all dependencies:
``` sudo apt install gnuradio gr-osmosdr gr-rds ```

## How to build and run (recomended for first use):
``` grcc RPi4_FM_RDS.grc -e -d /home/pi ```

## How to run (after first use):
``` python ./RPi4_FM_RDS.py ```

Tested and working with Raspberry Pi 4 and generic DVB-T USB receiver with Realtek RTL2838UHIDIR chip (with Rafael Micro R820T tuner), should also be working on Raspberry Pi 3.
