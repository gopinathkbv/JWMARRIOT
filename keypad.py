import RPi.GPIO as GPIO
import time
L1 = 5
L2 = 6
C1 = 12
C2 = 16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        print(characters[0])
    if(GPIO.input(C2) == 1):
        print(characters[1])
    
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        readLine(L1, ["S1","S2"])
        readLine(L2, ["S3","S4"])
        time.sleep(.8)

except KeyboardInterrupt:
    print("\2x2 MATRIX KEYPAD IS IN IDLE STATE!")
    
       
