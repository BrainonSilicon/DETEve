
import time
from adafruit_crickit import crickit
import pygame

RATE = 44100
CHUNK = int(RATE / 10)  # 100ms

#initialize pygame so that we can run audio 
pygame.init()
pygame.mixer.init()

def Eve_open_hatch(): #someone has opened Eve's hatch
    pygame.mixer.init()
    pygame.mixer.music.load('Eve_up_beep.wav') #TODO add audio file #welcomeing sound
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(1)

def Eve_closed_hatch(): #someone has closed Eve's hatch - warning sound that eve is active/has blades running
    pygame.mixer.init()
    pygame.mixer.music.load('Eve_soft_low_dodo.wav') #TODO add audio file #confirmation low pitch sound
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(1)
        
def Eve_sings(): #someone has closed Eve's hatch - warning sound that eve is active/has blades running
    pygame.mixer.init()
    pygame.mixer.music.load('Eve_singing.wav') #TODO add audio file #angry warning sound to scare humans away 
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(1)        

        
####if we use a "guard" mode for Eve
#def Eve_guarding(): #someone has closed Eve's hatch - warning sound that eve is active/has blades running
    #pygame.mixer.init()
    #pygame.mixer.music.load('') #TODO add audio file #angry warning sound to scare humans away 
    #pygame.mixer.music.play()
    #while pygame.mixer.music.get_busy(): 
        #pygame.time.Clock().tick(1)