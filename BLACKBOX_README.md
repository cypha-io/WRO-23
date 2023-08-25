 # LEGO Mindstorms EV3 Python Project 

This project is designed to demonstrate how to use the LEGO Mindstorms EV3 brick to sense colors and navigate through a course. 

## Step-by-Step Explanation

### 1. Importing the Necessary Libraries

The first step is to import the necessary libraries. In this case, we are using the `pybricks-micropython` library. This library provides access to the EV3 brick's sensors and motors.

```python
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile
```

### 2. Creating Objects

Next, we need to create objects for the EV3 brick, motors, sensors, and drive base.

```python
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
```

### 3. Defining Functions

Next, we need to define some functions that will be used to control the robot.

```python
# DEFINE ACTIONS HERE :)

# PID Until Both See Black
def pid_line(proportional_gain=1.05, drive_speed=robot_speed):
    while left_sensor.reflection() + right_sensor.reflection() > 50:
        # Calculate the deviation from the threshold.
        deviation = left_sensor.reflection() - right_sensor.reflection()
        # Calculate the turn rate.
        turn_rate = proportional_gain * deviation
        # Set the drive base speed and turn rate.
        robot.drive(drive_speed, turn_rate)
    robot.stop()

# PID