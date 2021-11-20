import pigpio as pig
import time

class Bipolar_Stepper_Motor:

    # IMPORTANT: PIGPIO ONLY USES BCM NUMBERING. NOT BOARD
    # pi = pig.pi() Grants access to RPI's GPIO. Insert into primary code

    dir = 0
    position = 0 # Current "step position" of motor. A single revolution has 200 positions (steps)
    
    # Initialize an object to control a single stepper driver
    def __init__(self, stepPin, dirPin, M0, M1, M2, sleepPin):

        self.stepPin = stepPin
        self.dirPin = dirPin
        self.M0 = M0
        self.M1 = M1
        self.M2 = M2
        self.sleepPin = sleepPin
        
        pi.set_mode(self.stepPin, pig.OUTPUT)
        pi.set_mode(self.dirPin, pig.OUTPUT)
        pi.set_mode(self.M0, pig.OUTPUT)
        pi.set_mode(self.M1, pig.OUTPUT)
        pi.set_mode(self.M2, pig.OUTPUT)
        pi.set_mode(self.sleepPin, pig.OUTPUT)
        
        self.dir = 0
        self.position = 0
        pi.write(self.sleepPin, True) # Sets sleep HIGH by default. Allows for general driver use.
        
    def move(self, dir, steps, delay = 0.2):
        for _ in range(steps):
            
            # MODIFY BELOW SECTION TO USE PIGPIO WAVEFORMS FOR TIMING
            self.dir = dir
            self.position += dir
            
            time.sleep(delay)

    def unhold(self):
        pi.write(self.sleepPin, False)
        
