#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile


# Creating objects here.
ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

gyro = GyroSensor(Port.S1)
left_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S3)
color_sensor = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=150)

robot_speed = 100

#Station Color Codes
possible_color = [['Color', 'GREEN'], ['Color', 'BLUE']]
possible_color_1 = [Color.BLUE, Color.GREEN, 'Color.GREEN', 'Color.BLUE']
station_color = []
station_blue_green = [Color.BLUE, Color.GREEN, 'Color.GREEN', 'Color.BLUE']

#Container Color Codes
container_color = [] #List of lists to store the color codes for each container


                        #PROGRAMS STAY HERE LOL:)


# DEFINE ACTIONS HERE :)

# PID Until Both See Black
def pid_line(proportional_gain=1.05, drive_speed=200):
    while left_sensor.reflection() + right_sensor.reflection() > 50:
        # Calculate the deviation from the threshold.
        deviation = left_sensor.reflection() - right_sensor.reflection()
        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation
        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)
    robot.stop()
    
#PID For Right Sensor
#---

# PID For Distance
def pid_distance(proportional_gain=1.4, drive_speed=robot_speed, distance=10):
    robot.reset()
    while robot.distance() <= distance:
        # Calculate the deviation from the threshold.
        deviation = left_sensor.reflection() - right_sensor.reflection()
        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation
        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)
    robot.stop()

# Move robot straight with gyro sensor!
def accurate_straight(distance=200, drive_speed=150):
    gyro.reset_angle(0)
    while robot.distance() <= 100:
        correction = (0 - gyro.angle())*1
        robot.drive(drive_speed, correction)
    robot.stop() #corrected
ev3.speaker.beep()

# Turn 90 Degrees
def turn_90_left(speed=200):
    gyro.reset_angle(0)
    while gyro.angle() < 90:
        left_motor.run(200)
    robot.stop()
    ev3.speaker.beep()
    
def turn_90_right(speed=200):
    gyro.reset_angle(0)
    while gyro.angle() < 90:
        right_motor.run(200)
    robot.stop()
    ev3.speaker.beep()
    
def turn_90_right_rev(speed=-200):
    gyro.reset_angle(0)
    while gyro.angle() < 90:
        right_motor.run(-200)
    robot.stop()
    ev3.speaker.beep()
    
def turn_90_left_rev(speed=-200):
    gyro.reset_angle(0)
    while gyro.angle() < 90:
        left_motor.run(-200)
    robot.stop()
    ev3.speaker.beep()

# Turn 180 Degrees
def turn_180(speed=200):
    gyro.reset_angle(0)
    while gyro.angle() < 180:
        left_motor.run(robot_speed)
    robot.stop()
    ev3.speaker.beep()

    # DEFINE MISSIONS HERE :(

# Say color that has been sensed
def say_color():
    output_color = str(color_sensor.color()).split(".")
    ev3.speaker.set_speech_options('en', 'f3', 150, 75)
    ev3.speaker.set_volume(100, which='PCM')
    ev3.speaker.say(str(output_color[1]))
    print(output_color)