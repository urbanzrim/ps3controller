# PS3 controller data bridge

This script gets data from PS3 controller via USB (on linux), extracts it and sends it to specified MAC address via PC's bluetooth. This was made as part of a quadcopter project (it's a STM32f3 based quadcopter - I will commit code here in the future).

## Usage
 - Write MAC address of the device
 - run the script ($ python main.py)

In this project I only needed data for both analog sticks. For other keys, you have to check if flag is set on 6th element of "datas" array and when it is, you can get data on 7th element.


The script was tested on/with:
- Ubuntu 14.04 (Linux this is mandatory)
- PS3 controller (it doesn't matter if it's original or fake)
- HC-06 bluetooth module
- Python 2.7 (for newer version, just replace what's necesarry)
