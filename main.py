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

    # Change this while loop to stop when sensor is triggered
    servo.ChangeDutyCycle(5)
    time.sleep(0.5)
    servo.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    servo.ChangeDutyCycle(10)
    time.sleep(0.5)
    servo.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    servo.ChangeDutyCycle(10)
    time.sleep(0.5)
    servo.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    servo.ChangeDutyCycle(5)
    time.sleep(0.5)
    servo.ChangeDutyCycle(2.5)
    time.sleep(0.5)

# def look_left():
    # stub

# def look_right():
    # stub


    

try:
    while True:
        mAll.forward(100)
        sensor.trigger()
        while sensor.Triggered == False:
            servo_scan()

        mAll.stop()
        time.sleep(5)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()

