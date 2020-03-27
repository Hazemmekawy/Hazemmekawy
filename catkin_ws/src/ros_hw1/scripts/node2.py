#!/usr/bin/env python
import rospy

from std_msgs.msg import String
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/motor/vel_msg', Twist, queue_size=5)
vel = Twist()
speed = 0.0

def subfunctionCb(msg):
    global speed

    rospy.loginfo("Received msg from /sensor/ultrasonic is: %s", msg.data)

    distance = int(msg.data)
    if(distance <= 30):
        speed = 0.0
    elif distance >= 70:
        speed = 1.0
    else:
	speed = float(distance)/100

    vel.linear.x = speed
    pub.publish(vel)

def subscriberRole():
    global vel

    rospy.init_node('node_2', anonymous=False)
    rospy.Subscriber('/sensor/ultrasonic', String, subfunctionCb)
    rospy.spin()   

if __name__== '__main__':
    try:
        subscriberRole()
    except rospy.ROSInterruptException:
        pass
