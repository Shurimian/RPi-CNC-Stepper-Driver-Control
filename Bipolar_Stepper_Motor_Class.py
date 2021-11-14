import RPi.GPIO as GPIO
import time

class Bipolar_Stepper_Motor:
    
    dir = 0
    position = 0
    
    def __init__(self, stepPin, dirPin, M0, M1, M2, sleepPin):
    #initial a Bipolar_Stepper_Moter objects by assigning the pins
    
        GPIO.setmode(GPIO.BOARD)
        
        self.stepPin = stepPin
        self.dirPin = dirPin
        self.M0 = M0
        self.M1 = M1
        self.M2 = M2
        self.sleepPin = sleepPin
        
        GPIO.setup(self.stepPin, GPIO.OUT)
        GPIO.setup(self.dirPin, GPIO.OUT)
        GPIO.setup(self.M0, GPIO.OUT)
        GPIO.setup(self.M1, GPIO.OUT)
        GPIO.setup(self.M2, GPIO.OUT)
        GPIO.setup(self.sleepPin, GPIO.OUT)
        
        self.dir = 0
        self.position = 0
        self.sleepPin = 1 # Sets sleep HIGH by default. Allows for general driver use.
        
    def move(self, dir, steps, delay = 0.2):
        for _ in range(steps):
            next_phase = (self.phase + dir) % num_phase
            
            GPIO.output(self.a1, phase_seq[next_phase][0])
            GPIO.output(self.b2, phase_seq[next_phase][1])
            GPIO.output(self.a2, phase_seq[next_phase][2])
            GPIO.output(self.b1, phase_seq[next_phase][3])
            
            self.phase = next_phase
            self.dir = dir
            self.position += dir
            
            time.sleep(delay)

    def unhold(self):
        GPIO.output(self.sleepPin, 0)
        
