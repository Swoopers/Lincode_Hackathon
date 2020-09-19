'''
Greetings to all

These are the instructions on how to use the mobot function to perform the simulation

import mobot module

moveForward() function will move the robot 1 unit in forward direction
moveBackward() function will move the robot 1 unit in backward direction
rotateRight() function will rotate the robot 1 degree in clockwise direction
rotateLeft() function will rotate the robot 1 degree in counter clockwise direction

Few places have specific names
All other places are named as 'Road'
Use fetchLocation() to get the current location of the robot

To perform the mapping operation you need to gather lidar data
Use getLidar() function to get the lidar data from robot of its current location
Note: The direction, the robot is facing is taken as 0 degree and the value increases in clockwise direction

Once you have completed the mapping execute updateEndMapping() 

Once you move back to "Start" location after mapping for path planning Phase 1 execute updateStartPlanningP1()

Once you have completed the path planning for Phase 1 and travel to "End" execute updateEndPlanningP1()

Once you move back to "Start" location after mapping for path planning Phase 2 execute updateStartPlanningP2()

Once you have completed the path planning for Phase 2 and travel to "End" execute updateEndPlanningP2()
'''

from mobot import *

moveForward()
moveBackward()
rotateRight()
rotateLeft()

fetchLocation()
getLidar()

updateEndMapping()
updateStartPlanningP1()
updateEndPlanningP1()
updateStartPlanningP2()
updateEndPlanningP2()
