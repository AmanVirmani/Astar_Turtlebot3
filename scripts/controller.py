#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from AStar import PathPlanning
from time import sleep
import sys
from math import degrees


def main():
    rospy.init_node('AstarPlanner')
    vel_publish = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1) # 1hz
    # to induce the wandering behaviour
    rpm = [int(sys.argv[7]), int(sys.argv[8])]
    planner = PathPlanning([int((float(sys.argv[1])+5)*10), int((float(sys.argv[2])+5)*10), int(degrees(float(sys.argv[3])))],
                  [int((float(sys.argv[4])+5)*10), int((float(sys.argv[5])+5)*10)], int(sys.argv[6]), rpm)
    path,_ = planner.Astar()
    action_set = [[0, rpm[1]],[rpm[0], rpm[1]],[rpm[1], rpm[1]],[rpm[1], rpm[0]],[rpm[1], 0],[0, rpm[0]],[rpm[0], rpm[0]],[rpm[0], 0]]
    for i in range(1, len(path)):
        velocity = Twist()
        r = 0.0033
        l = 0.9

        action = path[i].action
        rpm1, rpm2 = action_set[int(action)-1]

        velocity.linear.x = r/2*(rpm1+rpm2)
        velocity.angular.z = r/l*(rpm1-rpm2)
        print(velocity.linear.x, velocity.angular.z)
        vel_publish.publish(velocity)
        sleep(10)
    velocity = Twist()
    velocity.linear.x = 0
    velocity.angular.z = 0
    vel_publish.publish(velocity)


if __name__ == '__main__':
    main()
