__author__ = 'urban'
import psutil
import serial
import string
import time
import sixaxis
import bluetooth
sixaxis.init("/dev/input/js0")

def parseSensorsOutputLinux(output):
    return int(round(float(output) / 1000))

def connect():
    while(True):
        try:
            gaugeSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            #Write your MAC address
            gaugeSocket.connect(('XX:XX:XX:XX:XX:XX', 1))
            break;
        except bluetooth.btcommon.BluetoothError as error:
            gaugeSocket.close()
            print "Connection failed ", error, "; Retry in 5s..."
            time.sleep(5)
    return gaugeSocket;

gaugeSocket = connect()
while(True):

    time.sleep(0.05)
    data = sixaxis.get_state()
    print data
    try:
        gaugeSocket.send(str(int(data[0], 16)))
        gaugeSocket.send(str(int(data[1], 16)))
        gaugeSocket.send(str(int(data[2], 16)))
        gaugeSocket.send(str(int(data[3], 16)))
        #print gaugeSocket.recv(1)
    except bluetooth.btcommon.BluetoothError as error:
        print "Caught Bluetooth Error: ", error
        time.sleep(5)
        gaugeSocket = connect()
        pass

gaugeSocket.close()
