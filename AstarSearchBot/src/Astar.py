#!/usr/bin/env python
# license removed for brevity
import os
import numpy as np
import rospy, rospkg
from geometry_msgs.msg import Twist
import time

def talker():
    rospy.sleep(5)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('brain', anonymous=True)
    rate = rospy.Rate(2) # 10hz
    rospack = rospkg.RosPack()
    msg = Twist()
    msg.linear.x = 0.0
    msg.angular.z = 0.5
    lines = []
    with open(os.path.join(rospack.get_path("AstarSearchBot"),"test.txt")) as f:
        while True:
            a = f.readline()
            if not a:
                break
            lines.append(a.strip())

    #while not rospy.is_shutdown()
    scale = 1.2
    print(len(lines))
    for line in lines:
        ul, ur = line.split(' ')
        msg.linear.x = np.float64(ul)*scale
        msg.angular.z = np.float64(ur)*scale
        #start = rospy.get_time()
        #while rospy.get_time() - start < 5:
        #    pub.publish(msg)
        #    rate.sleep()
        #msg.linear.x = 0
        #msg.angular.z = 0
        print(msg)
        pub.publish(msg)
        #break
        #pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
