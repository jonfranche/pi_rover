import PiMotor
import time
import RPi.GPIO as GPIO

servoPIN = 38

GPIO.setup(servoPIN, GPIO.OUT)
servo = GPIO.PWM(servoPIN, 50)
servo.start(2.5)

m1 = PiMotor.Motor("MOTOR1", 1)
m2 = PiMotor.Motor("MOTOR2", 1)
m3 = PiMotor.Motor("MOTOR3", 1)
m4 = PiMotor.Motor("MOTOR4", 1)

mAll = PiMotor.LinkedMotors(m1, m2, m3, m4)

ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3)
ar = PiMotor.Arrow(4)

sensor =  PiMotor.Sensor("ULTRASONIC", 10)
    
def servo_scan():
    for x in range (2, 6, 1):
        servo.ChangeDutyCycle(x * 2.5)
        time.sleep(0.5)
        sensor.trigger()
    for x in range (5, 0, -1):
        servo.ChangeDutyCycle(x * 2.5)
        time.sleep(0.5)
        sensor.trigger()

try:
    while True:
        mAll.forward(100)
        while sensor.Triggered == False:
            servo_scan()

        mAll.stop()
        time.sleep(5)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()

