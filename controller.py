import time

from pyfirmata import Arduino, SERVO

PORT = "COM3"

pin = 10

board = Arduino(PORT)

board.digital[pin].mode=SERVO

def rotateServo(pin, angle):
    board.digital[pin].write(angle)


def doorAutomate():
    rotateServo(pin,220)
    time.sleep(5)
    rotateServo(pin,40)