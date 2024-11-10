import os
import sys
import subprocess
import time
import os.path
import serial



from os.path import *
from subprocess import Popen, PIPE, STDOUT
from time import sleep
from serial import *




def detect():
    print("Console > Detecing Serial-Connection!")
    os.system("ls -l /dev/ttyS*")
    
    print("Choose smth. like: '/dev/ttyS1' !!!")
    uart_dev = input("UART-Device > ")
    return uart_dev

def advanced_console(uart_dev):
    detect()
    ser = serial.Serial(
        port=uart_dev, 
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    
    ser.write(b'Hello, Banana Pi!\n')

    while True:
        if ser.in_waiting > 0:
            data = ser.readline()
            print(data.decode('utf-8'))

    ser.close()






def default_console():


    ser = serial.Serial('/dev/ttyS1', 115200, timeout=1)

    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(f"Received from ESP8266: {data}")


def all_in_one():
    print("Console > Detecing Serial-Connection!")
    os.system("ls -l /dev/ttyS*")
    
    print("Choose smth. like: '/dev/ttyS1' !!!")
    uart_dev = input("UART-Device > ")
    ser = serial.Serial(
        port=uart_dev, 
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    
    ser.write(b'Hello, Banana Pi!\n')

    while True:
        if ser.in_waiting > 0:
            data = ser.readline()
            print(data.decode('utf-8'))

    ser.close()

    

def main():
    all_in_one()
    
    
if __name__ == '__main__':
    main()
    