#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Twist

def simplePublisher():
    
    pub = rospy.Publisher('/vel_msg_1', Twist, queue_size=5)
    rospy.init_node('pub_task2', anonymous=False)
    rate = rospy.Rate(1) # 1Hz >> 1sec

    vel = Twist()
    while not rospy.is_shutdown():
	vel.linear.x = 1
        pub.publish(vel)
        rate.sleep()    # 500msec

if __name__== '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass


