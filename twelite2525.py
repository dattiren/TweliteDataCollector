from __future__ import print_function
import csv
import pprint

import serial
from time import sleep
import time
from datetime import datetime

from pymongo import MongoClient

devices = '/dev/ttyUSB0'
ser = serial.Serial(devices, 115200)
num=0
start = time.time()
while True:
    now = datetime.now()
    with open('/home/pi/Desktop/sleep_test.csv' ,'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        value = ser.readline().rstrip().decode('utf-8')
        arr = value.split(":")

        if(len(arr) == 13):
            
            list = ['ed=', 'lq=', 'x=', 'y=', 'z=']
            for i in range(len(list)):
                value = value.replace(list[i], '')
            (nil, nil2,  rc, lq, ct, ed, num, ba, a1, a2, x, y, z) = value.split(":")
            ts = round(time.time() - start, 2)

            #connect mongoDB
            client = MongoClient('192.168.1.252', 27017)
            db = client['twelite2525']
            collection = db['twelite2525_data']
            mongoData = {'ts': ts, 'lqi': lq, 'battery': ba, 'accelerator': {'x': x, 'y': y, 'z': z}}
            collection.insert_one(mongoData)

            a = [ts, lq, ba, x, y, z]
            writer.writerow(a)
           # (nil, ts, nil2, lq, ct, ed, ba, mn, nil3, a1, a2i, p, x, y, z, nil4) = value.split(";")
           #810F1C1C,810F19CF ,810F1D12 
            #a = [now., ct, lq, ed, ba, x, y, z]
            #a = [lq]
            print(a)
