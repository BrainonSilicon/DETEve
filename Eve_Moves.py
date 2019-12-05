import time 
from adafruit_crickit import crickit 

servos = (crickit.servo_1, crickit.servo_2, crickit.servo_3, crickit.servo_4)

####THIS SHOULD BE CHANGED BASED ON DEC 4TH SYNC 
#compost hatch is on pin1 
#seed out is pin 2
#grinder is pin 3
#squirter is pin 4

######THIS SHOULD BE CHANGED BASED ON DEV 4TH SYNC #########

#COMPOST HATCH CONTROLS 
def hatch_open():
    print ("Hatch opening")
    servos[1].angle = 120
    time.sleep(2)
    
def hatch_close():
    print ("Hatch closing")
    servos[1].angle = 0 
    time.sleep(1)
    
#SEE DISPERSION CONTROLS 
def seeds_open():
    print ("Seed dispersion open")
    servos[2].angle = 90

def seeds_closed():
    print ("Seed dispersion closed")
    servos[2].angle = 0 

