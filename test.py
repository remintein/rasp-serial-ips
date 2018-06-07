#!/usr/bin/python
import urllib
import urllib2
import time
import serial

ser = serial.Serial(
    port = '/dev/ttyAMA0',
    baudrate = 115200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
    )
count = 0
#print("Coordinate: ")

try:
    #ser.write(b'\r\n\r\n')
    #time.sleep(3)
    #print('testing')
    #ser.write(b'lec')
    
    
    while True:
        s = ser.readline()
        data = s.decode('utf-8')
        data = data.rstrip()
        dataArray = data.split(b',')
        if dataArray[0] != b'':
            print('****************')
            print('ID: ' + str(dataArray[1]) + ' , Lat: ' + str(dataArray[3]) + ' , Long: ' + str(dataArray[4]) + ' , Alt: ' + str(dataArray[5]))
            count += 1
            print count
            if count == 25:
                #if dataArray[1] == 0:
                url = 'http://www.110b3.com/ips/php-config/collect-1.php'
                values = {'latitude': str(dataArray[3]),
                          'longitude': str(dataArray[4])}
                print values
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Encoding': 'gzip,deflate'}
                dataSend = urllib.urlencode(values)
                req = url + '?' + dataSend
                response = urllib2.urlopen(req)
                count = 0
                print('*** Sent ***')
        else:
            print('No new pos')
except KeyboardInterrupt:
    ser.close()
