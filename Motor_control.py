import RPi.GPIO as GPIO
import pigpio as pig
import time
from Bipolar_Stepper_Motor_Class import Bipolar_Stepper_Motor
from numpy import abs, sign, sqrt


def GCD(a, b): # Greatest common diviser
    while b:
       a, b = b, a % b
    return a

def LCM(a, b): # Least common multipler
    return a * b / GCD(a, b)
    
def Motor_Step(stepper1, step1, stepper2, step2, speed):
#   control stepper motor 1 and 2 simultaneously
#   stepper1 and stepper2 are objects of Bipolar_Stepper_Motor class
#   direction is reflected in the polarity of [step1] or [step2]

    dir1 = sign(step1) != -1 # Get dirction from the polarity of argument [step]
    dir2 = sign(step2) != -1

    step1 = abs(step1)
    step2 = abs(step2)

# [total_micro_step] total number of micro steps
# stepper motor 1 will move one step every [micro_step1] steps
# stepper motor 2 will move one step every [micro_step2] steps
# So [total_mirco_step]=[micro_step1]*[step1] if step1<>0;  [total_micro_step]=[micro_step2]*[step2] if step2<>0 

    # IMPORTANT: FIGURE OUT WTH THIS SECTION DOES SO I CAN CODE FOR IT
    if step1 == 0:
        total_micro_step = step2
    	micro_step2 = 1
        micro_step1 = step2 + 100  #set [micro_step1]>[total_micro_step], so stepper motor will not turn
    elif step2 == 0:
        total_micro_step = step1
        micro_step1 = 1
        micro_step2 = step1 + 100
    else:
        total_micro_step = LCM(step1, step2)
        micro_step1 = total_micro_step / step1
        micro_step2 = total_micro_step / step2

    T = sqrt(step1 ** 2 + step2 ** 2) / speed   # Total time
    dt = T / total_micro_step                   # Time delay every micro_step
    
    for i in range(1, total_micro_step + 1):    #i is the iterator for the micro_step. i cannot start from 0
        time_laps = 0

        #FIGURE OUT IF WAVEFORMS WILL RUN IN PARALLEL AFTER THE WAVE IS CREATED
        if ((i % micro_step1) == 0): # Motor 1 need to turn one step
            stepper1.move(dir1, 1, dt / 4.0)
            time_laps += dt / 4.0
            
        if ((i % micro_step2) == 0): # Motor 2 need to turn one step
            stepper2.move(dir2, 1, dt / 4.0)
            time_laps += dt / 4.0
        
        time.sleep(dt - time_laps)

    return 0
