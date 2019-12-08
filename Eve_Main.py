############# MAIN PROGRAM GAME PLAN ###############

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

########## OUR WORKING CODE #############

#import Pi stuff 
import time 
from adafruit_crickit import crikit 
import pygame #for playing audio
from adafruit_seesaw.neopixel import NeoPixel

import picamera     #camera library
import pygame as pg #audio library
import os           #communicate with os/command line

# from google.cloud import vision  #gcp vision library
# import signal
# import sys
# import re    

#import Eve files
import Eve_Moves
import Eve_audio
import Eve_Lights

###GOOGLE IMAGE CODE FOR IMAGE/HUMAN RECOGNITION
# credential_path = "/home/pi/DET190-JSON/DETcredential.json" #credential file path
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=credential_path

# client = vision.ImageAnnotatorClient()

# image = 'image.jpg'

# def takephoto(camera):
#     # this triggers an on-screen preview, so you know what you're photographing!
#     camera.start_preview() 
#     sleep(0.5)                   #give it a pause so you can adjust if needed
#     camera.capture('image.jpg') #save the image
#     camera.stop_preview() 

# def image_labeling(image):
    
#     string1 = "dog"
#     string2 = "cat"
    
#     sound1 = "/home/pi/DET2019_Class5/dog2.wav"
#     sound2 = "/home/pi/DET2019_Class5/cat.wav"
    
#     response = client.label_detection(image=image)
#     labels = response.label_annotations
       
#     label_text = ""
    
#     #this next block of code parses the various labels returned by google,
#     #extracts the text descriptions, and combines them into a single string. 
#     for label in labels:
#         label_text += ''.join([label.description, " "])
    
#     #if labels are identified, send the sound files, search strings, and label
#     #text to speaker_out()
#     if label_text:
#         print('image_labeling(): {}'.format(label_text))
#         speaker_out(sound1, sound2, label_text, string1, string2)
#     else:
#         print('image_labeling(): No Label Descriptions')   
       
# def web_search(image):
#     #this function sends your image to google cloud using the
#     #web_detection method, collects a response, and parses that
#     #response for the 'best web association' found for the image.
#     #there's no actuation here - just printing - but you can easily
#     #engage with speaker_out() or motor_turn() if you like!
    
#     response = client.web_detection(image=image)
#     web_guess = response.web_detection
    
#     for label in web_guess.best_guess_labels:
#         print('Best Web Guess Label: {}'.format(label.label))


  

#not sure if this needs to be both here and in the audio file 
RATE = 44100
CHUNK = int(RATE / 10)  # 100ms

num_pixels = 8 #TODO change this  
pixels = NeoPixel(crickit.seesaw, 20, num_pixels) 

pygame.init()
pygame.mixer.init()

def main():
    print ("running main")
    #eve recieves compost from people 
    time.sleep(8)
    Eve_audio.Eve_open_hatch()
    time.sleep(2)
    Eve_audio.Eve_closed_hatch()
    Eve_Lights.Eve_recieved()
    time.sleep(8)
    Eve_Moves.Eve_blade_on()
    Eve_Lights.Eve_planting()
    time.sleep(0.2)
    Eve_Moves.Seed_dispersed()
    Eve_Moves.Eve_blade_off()
    Eve_audio.Eve_sings()
    time.sleep(3)
    Eve_Moves.Water_on()
    Eve_Moves.Water_off()
    time.sleep(4)
    #camera = picamera.PiCamera()
    Eve_Lights.Eve_stealth()
    # takephoto(camera) # First take a picture
    # """Run a label request on a single image"""

    # with open('image.jpg', 'rb') as image_file:
    #     #read the image file
    #     content = image_file.read()
    #     #convert the image file to a GCP Vision-friendly type
    #     image = vision.types.Image(content=content)
    #     ocr_handwriting(image)
    #     image_labeling(image)
    #     face_distinction(image)
    #     web_search(image)
    #     time.sleep(0.1)        
        

if __name__ == '__main__':
    main()
