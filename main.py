#!/usr/bin/env pybricks-micropython
from _subfolder.initializer import *



########################PROGRAMS HERE LOL :)##################

#start robot @ center button is pressed
start = Button.CENTER in ev3.buttons.pressed()

#SECTION 1
if (start):
    #sense(store) station colors & fuel big ship --- section 1 
    run_section_1()
    