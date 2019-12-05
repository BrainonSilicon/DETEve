#eve moves up to a user 

#user opens the hatch 
#if hatch open then nothing is on
#user puts compost in 
#hatch closes 
#else the other motors are running 

#eve trundles away 

#eve arrives to protected area 
#eve chops up compost 
#eve compressed the compost
#compost heap comes out 
#eve disperses a seed 
#eve waters the heap 

#eve trundles away

####should eve have a "guard" or "educational" attribute ??

### should it be timing based ?? 

#import Pi stuff 
import time 
from adafruit_crickit import crikit 
import pygame  #for playing audio
from adafruit_seesaw.neopixel import NeoPixel

#import Eve files
import Eve_Moves
import Eve_Audio
import Eve_Lights

#not sure if this needs to be both here and in the audio file 
RATE = 44100
CHUNK = int(RATE / 10)  # 100ms

num_pixels = 8 #TODO change this  
pixels = NeoPixel(crickit.seesaw, 20, num_pixels) #TODO change the number 

pygame.init()
pygame.mixer.init()

def main():
    print ("running main")
    if (# the switch is active):
        print("Eve in active mode!")
        Eve_Audio.Eve_closed_hatch()
        Eve_Lights.Eve_recieved()
        Eve_Moves. () #the compressor compresses TODO
        Eve_Moves. () #the disperser disperses TODO 
        Eve_Moves. () #the waterer waters TODO 
        
        #should eve also have lights that help plants grow? 
        
        #if switch is active and a person is near - activate guard mode ?? 
             
    else:
        print("Eve's hatch is open and Eve is in safe mode!")
        #all motors are off
        Eve_Lights.Eve_waiting()
         

 
if __name__ == '__main__':
    main()
