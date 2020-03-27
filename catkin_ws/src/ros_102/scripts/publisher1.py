#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def simplePublisher():
    counter=0
    pub = rospy.Publisher('/test_topic_1', String, queue_size=5)
    
    rospy.init_node('pub_task1', anonymous=False)
    rate = rospy.Rate(2) # 2Hz >> 0.5 sec
    while not rospy.is_shutdown():
	counter+=1
	if counter > 10:
            counter=0
        pub.publish(str(counter))
        rate.sleep()    # 500msec

if __name__== '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass
