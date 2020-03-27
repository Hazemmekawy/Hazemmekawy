#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Twist


def callbackfn(msg):
    if msg.linear.x == 0.0:
        rospy.loginfo("Robot stopped")
    else:
        rospy.loginfo("Robot is moving forward with speed = %.2f"%(msg.linear.x))

def subscriber():
    rospy.init_node('node_3', anonymous=False)
    rospy.Subscriber('/motor/vel_msg', Twist, callbackfn)
    rospy.spin()

if __name__== '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
