import PiMotor
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) 

GPIO.setwarnings(False)

servoPIN1 = 7

GPIO.setup(servoPIN1, GPIO.OUT)
servoX = GPIO.PWM(servoPIN1, 50)
servoX.start(7.3)

servoPIN2 = 12

GPIO.setup(servoPIN2, GPIO.OUT)
servoY = GPIO.PWM(servoPIN2, 50)
servoY.start(7.5)

m1 = PiMotor.Motor("MOTOR1", 1)
m2 = PiMotor.Motor("MOTOR2", 1)
m3 = PiMotor.Motor("MOTOR3", 1)
m4 = PiMotor.Motor("MOTOR4", 1)

mLeft = PiMotor.LinkedMotors(m1, m2)
mRight = PiMotor.LinkedMotors(m3, m4)

mAll = PiMotor.LinkedMotors(m1, m2, m3, m4)

ab = PiMotor.Arrow(3)
al = PiMotor.Arrow(2)
af = PiMotor.Arrow(1)
ar = PiMotor.Arrow(4)

sensor =  PiMotor.Sensor("ULTRASONIC", 30)

def scan_left():
    servoX.ChangeDutyCycle(12.5)
    servoY.ChangeDutyCycle(8.5)
    sensor.trigger()
    print('scanning left')
    return sensor.lastRead
    
def scan_right():
    servoX.ChangeDutyCycle(2.5)
    sensor.trigger()
    print('scanning right')
    return sensor.lastRead

def servo_scan2():
    left = scan_left()
    time.sleep(0.5)
    right = scan_right()
    time.sleep(0.5)
    if sensor.Triggered == False and left > right:
        servoX.ChangeDutyCycle(7.3)
        servoY.ChangeDutyCycle(7.5)
        move_reverse()
        time.sleep(1)
        reverse_stop()
        mLeft.forward(100)
        mRight.reverse(100)
        al.on()
        time.sleep(1)
        mLeft.stop()
        mRight.stop()
        al.off()
    elif sensor.Triggered == False and right > left:
        servoX.ChangeDutyCycle(7.3)
        servoY.ChangeDutyCycle(7.5)
        move_reverse()
        time.sleep(1)
        reverse_stop()
        mRight.forward(100)
        mLeft.reverse(100)
        ar.on()
        time.sleep(1)
        mRight.stop()
        mLeft.stop()
        ar.off()
    else:
        servoX.ChangeDutyCycle(7.3)
        servoY.ChangeDutyCycle(7.5)
        mLeft.forward(100)
        al.on()
        mRight.reverse(100)
        ar.on()
        time.sleep(3)
        mLeft.stop()
        al.off()
        mRight.stop()
        ar.off()

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
    mAll.stop()
    servoY.stop()
    servoX.stop()
    GPIO.cleanup()