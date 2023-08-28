#!/usr/bin/env pybricks-micropython
from _subfolder.initializer import *

########################PROGRAMS HERE LOL :)##################
#SECTION 1
while True:
    if (Button.CENTER in ev3.buttons.pressed()):
        
        #Start the robot
        wait(300)
        ev3.speaker.beep()
        
        #Make sure all is in other
        robot.reset()
        #Main program here!
        break