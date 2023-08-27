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
        task_1() #Defined task ends @ the line from the station
        pid_line(0.3, 100)
        robot.straight(-80)
        turn_90_right()
        robot.straight(100)
        turn_90_right_rev()
        
        containers_store_colors()
        robot.straight(80)
        left_motor.run_target(100, 90)
        robot.straight(80)
        
        break