import time 
from adafruit_crickit import crickit 

servos = (crickit.servo_1, crickit.servo_2, crickit.servo_3, crickit.servo_4)
motor = crickit.dc_motor_1

#BLADE CONTROLS 
def Eve_blade_on():
    print ("blade on")
    #motor turns on for 5 seconds 
    #and then turns off
    servos[1].angle = 200 #we think this is "on" for the continuous motor 
    ###### TODO will need to figure out how to turn the continuous motor off

def Eve_blade_off(): 
    print ("blade turning off")
    servos[1].angle = 90 #TODO whichever angle turns the motor off maybe 180 

#SEED DISPERSION CONTROLS 
def Seed_dispersed():
    print ("Seed dispersion open")
    servos[2].angle = 90 #whichever angle will open the hatch 
    print ("Seed dispersion closing")
    servos[2].angle = 0 #whichever angle will close the hatch 
    
#WATER CONTROLS 
def Water_on(): 
    print ("Water on")
    motor.throttle = 0.5 
      
def Water_off(): 
    print("Water off")
    motor.throttle = 0.0
    
     

