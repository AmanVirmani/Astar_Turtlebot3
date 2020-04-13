## Overview
A* implementation for Rigid Robot

## Dependencies

The following dependencies must be installed.

1. python3.5 or above
2. numpy
3. ROS melodic

Enter the given commands in bash terminal to install the dependencies.
```bash
sudo apt-get install python3
pip3 install numpy
```
To instal ROS melodic, follow instructions on official ROS website.

## Build Instructions

Run the following command to do path planning for a rigid robot using A* algorithm
Clone this repository in src directory of ROS workspace
```bash
catkin_make
source devel/setup.bash
```
For Case 1 output
```bash
roslaunch astar_turtlebot3 demo.launch x_pos:=-4 y_pos:=-3 theta:=0 x_pos_f:=0 y_pos_f:=-3 clearance:=2 rpm1:
```
For Case 2 output
```bash
roslaunch astar_turtlebot3 demo.launch x_pos:=-4 y_pos:=-4 theta:=0 x_pos_f:=4 y_pos_f:=4 clearance:=2 rpm1:=60 rpm2:=
```

## Output

The file  output_1.avi and output_2.avi show the animation for the optimal path after the exploration in res
