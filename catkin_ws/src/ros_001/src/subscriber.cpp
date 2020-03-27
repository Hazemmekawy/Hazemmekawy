#include <ros/ros.h>
#include "std_msgs/String.h"
#include <geometry_msgs/Twist.h>
#include <stdlib.h>

// Topic messages callback
/*
void velCallback(const geometry_msgs::Twist msg)
{

	ROS_INFO("[Subscriber] received:\n[x=%f]\n[y=%f]\n[z=%f]\n-------\n", msg.linear.x, msg.linear.y, msg.linear.z);

}
*/

void velCallback(const std_msgs::String::ConstPtr& msg)
{
	ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
	// Initiate new ROS node named "subscriber1"
	ros::init(argc, argv, "subscriber1");
	// Create a node handle: it is reference assigned to a new node
	ros::NodeHandle n;
	
	// Subscribe to a given topic, in thise case "/topic_3"
	// velCallback: is the name of the callback function that will be executed each time a message is received
	ros::Subscriber sub = n.subscribe("/topic_3", 1000, velCallback);
	
	// Enter a loop, pumping callbacks
	ros::spin();

	return 0;
}
