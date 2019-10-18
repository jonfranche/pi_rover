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

mLeft = PiMotor.LinkedMotors(m1, m2)
mRight = PiMotor.LinkedMotors(m3, m4)

mAll = PiMotor.LinkedMotors(m1, m2, m3, m4)

ab = PiMotor.Arrow(1)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(3)
ar = PiMotor.Arrow(4)

sensor =  PiMotor.Sensor("ULTRASONIC", 40)

''' def servo_scan():
    look_left()
    sensor.trigger()
    if sensor.Triggered == False:
        mAll.reverse(100)
        time.sleep(1)
        mAll.stop()
        mLeft.forward(50)
        time.sleep(2)
        mLeft.stop()
    else:
        look_right()
        sensor.trigger()
        if sensor.Triggered == False:
            mAll.reverse(100)
            time.sleep(1)
            mAll.stop()
            mRight.forward(50)
            time.sleep(2)
            mRight.stop()
        else:
            mLeft.forward(100)
            mRight.reverse(100)
            time.sleep(2)
            mLeft.stop() '''
            
def servo_scan2():
    left = scan_left()
    time.sleep(0.5)
    right = scan_right()
    time.sleep(0.5)
    if sensor.Triggered == False and left > right:
        servo.ChangeDutyCycle(7.5)
        move_reverse()
        time.sleep(1)
        reverse_stop()
        mLeft.forward(100)
        al.on()
        time.sleep(2)
        mLeft.stop()
        al.off()
    elif sensor.Triggered == False and right > left:
        servo.ChangeDutyCycle(7.5)
        move_reverse()
        time.sleep(1)
        reverse_stop()
        mRight.forward(100)
        ar.on()
        time.sleep(2)
        mRight.stop()
        ar.off()
    else:
        servo.ChangeDutyCycle(7.5)
        mLeft.forward(100)
        al.on()
        mRight.reverse(100)
        ar.on()
        time.sleep(3)
        mLeft.stop()
        al.off()
        mRight.stop()
        ar.off()
    
def scan_left():
    servo.ChangeDutyCycle(12.5)
    sensor.trigger()
    print('scanning left')
    return sensor.lastRead
    
def scan_right():
    servo.ChangeDutyCycle(2.5)
    sensor.trigger()
    print('scanning right')
    return sensor.lastRead

def move_forward():
    mAll.forward(100)
    af.on()

def forward_stop():
    mAll.stop()
    af.off()

def move_reverse():
    mAll.reverse(100)
    ab.on()

def reverse_stop():
    mAll.stop()
    ab.off()

try:
    while True:
        move_forward()
        sensor.trigger()
        if sensor.Triggered:
            forward_stop()
            servo_scan2()

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()

