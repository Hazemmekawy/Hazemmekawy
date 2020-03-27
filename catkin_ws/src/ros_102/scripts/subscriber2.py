#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Twist

def callbackfn(msg):
    rospy.loginfo("Received a /vel_msg_1 message!")
    rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))

def subscriber():
    rospy.init_node('subscriber2', anonymous=False)
    rospy.Subscriber('/vel_msg_1', Twist, callbackfn)
    rospy.spin()

if __name__== '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
