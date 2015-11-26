__author__ = 'urban'

import sys
import os
import threading
from binascii import hexlify

run = 1
datao = 0
num = [0,0,0,0]
class ps3_thread(threading.Thread):
    def run(self):
        global pipe
        global sdata
        global run
        global datao
        
        while 1:
            if(run == 0):
                exit()

            for character in pipe.read(1):
                sdata += [hexlify(character)]

                if len(sdata) == 8:
                    ''' Add other data from PS3 controller if you need.
                        See README file for details
                    '''
                    if sdata[7] == '00':
                        num[0] = hex(int(sdata[5],16))
                    if sdata[7] == '01':
                        num[1] = hex(int(sdata[5],16))
                    if sdata[7] == '02':
                        num[2] = hex(int(sdata[5],16))
                    if sdata[7] == '03':
                        num[3] = hex(int(sdata[5],16))
                        
                    datao = num                            
                    sdata = []

thread = ps3_thread()

def init(path):
    global pipe
    global sdata
    run = 1
    sdata = []
    try:
        pipe = open(path, 'r')
    except:
        return False
    thread.start()
    return True

def get_state():
    global datao
    return datao

def shutdown():
    global run
    run = 0
    thread.join()
