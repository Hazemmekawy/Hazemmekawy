#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def simplePublisher():
    pub = rospy.Publisher('/sensor/ultrasonic', String, queue_size=5)
    
    rospy.init_node('node_1', anonymous=False)
    rate = rospy.Rate(0.5) # 0.5Hz >> 2 sec
    counter=100
    while not rospy.is_shutdown():
	counter-=5
	if counter < 0:
            counter=100
        pub.publish(str(counter))
        rate.sleep()    

if __name__== '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass
