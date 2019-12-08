import time
from adafruit_crickit import crickit
from adafruit_seesaw.neopixel import NeoPixel
 
num_pixels = 8  #TODO changed based on our pixels 
 
# The following line sets up a NeoPixel strip on Seesaw pin 20 for Feather
pixels = NeoPixel(crickit.seesaw, 20, num_pixels) #TODO check which pin 

ss = crickit.seesaw

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0,0,0)

def Eve_waiting():
    pixels.fill(WHITE)
    
def Eve_recieved(): 
    pixels.fill(GREEN) #maybe some green some white
    
def Eve_guarding(): 
    pixels.fill(RED)
    
def Eve_planting():
    pixels.fill(BLUE)
    
def Eve_stealth():
    pixels.fill(OFF)
    
