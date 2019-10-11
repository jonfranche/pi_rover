import PiMotor
import time
import RPi.GPIO as GPIO

servoPIN = 38

GPIO.setup(servoPIN, GPIO.OUT)
servo = GPIO.PWM(servoPIN, 50)
servo.start(7.5)

m1 = PiMotor.Motor("MOTOR1", 1)
m2 = PiMotor.Motor("MOTOR2", 1)
m3 = PiMotor.Motor("MOTOR3", 1)
m4 = PiMotor.Motor("MOTOR4", 1)

mLeft = PiMotor.Motor(m1, m2)
mRight = PiMotor.Motor(m3, m4)

mAll = PiMotor.LinkedMotors(m1, m2, m3, m4)

ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3)
ar = PiMotor.Arrow(4)

sensor =  PiMotor.Sensor("ULTRASONIC", 40)

def servo_scan():
    look_left()
    sensor.trigger()
    if sensor.Triggered == False:
        mAll.reverse(100)
        time.sleep(1)
        mAll.stop()
        mLeft.forward(100)
        time.sleep(2)
        mLeft.stop()
    else:
        look_right()
        sensor.trigger()
        if sensor.Triggered == False:
            mAll.reverse(100)
            time.sleep(1)
            mAll.stop()
            mRight.forward(100)
            time.sleep(2)
            mRight.stop()
        else:
            mLeft.forward(100)
            time.sleep(3)
            mLeft.stop()

def look_left():
    servo.ChangeDutyCycle(12.5)

def look_right():
    servo.ChangeDutyCycle(2.5)

try:
    while True:
        servo.ChangeDutyCycle(7.5)
        mAll.forward(100)
        sensor.trigger()
        if sensor.Triggered:
            mAll.stop()
            servo_scan()

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()

