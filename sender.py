import pyvjoy
import time
import serial

j=pyvjoy.VJoyDevice(1)
j.startFfb()

class CallBack:
    def callback(self,data):
        print(data)
j.RegFfbCB()


def press(but):
    global j
    j.set_button(but,1)
    time.sleep(0.1)
    j.set_button(but,0)

def config():
    arduino=serial.Serial('COM3',9600)
    time.sleep(2)
    while arduino.in_waiting > 0:
        arduino.read()
    print('pronto')
    for i in range(1,8):
        while arduino.in_waiting==0:
            pass
        press(i)
        print(i)
        arduino.read()
    arduino.close()

