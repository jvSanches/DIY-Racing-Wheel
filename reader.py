# -*- coding: utf-8 -*-
"""
Created on Sat May 20 17:09:18 2017

@author: Sanches
"""
import sender
import pygame

pygame.init()
done = False

clock = pygame.time.Clock()

pygame.joystick.init()
a =0
active =0
# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            pass
            
            #print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            pass
            #print("Joystick button released.")
            
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    x = int( 100* joystick.get_axis(2)) 
    y = int( -100* joystick.get_axis(3)) 
    
    if y > 80 and x < -30 and active!= 1:
        sender.press(1)
        #print('1')
        active=1
    elif y > 80 and -10< x < 10 and active!= 3:
        #print("3")
        sender.press(3)
        active=3
    elif y > 80 and x > 30  and active!= 5:
        sender.press(5)
        #print('5')
        active=5
        
    elif y <  -80 and x < -30 and active!= 2:
        #print("2")
        sender.press(2)
        active=2
    elif y <  -80 and -10< x < 10 and active!= 4:
        #print('4')
        sender.press(4)
        active=4
    elif y <  -50 and x > 30 and active!= 6:
        sender.press(6)
        active=6
        #print('6')
    if joystick.get_button(9) and joystick.get_button(8):
        done = True
    if joystick.get_button(11) and x < -90 and active!=8:
        sender.press(7)
        active=8
        
        #print('r')
        
        
