#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "publisher1");
    ros::NodeHandle n;
    ros::Publisher pub = n.advertise<std_msgs::String>("/topic_3", 10);
    ros::Rate rate(1);

    while (ros::ok()) {
        std_msgs::String msg;
        msg.data = "hello from cpp";
        pub.publish(msg);
        rate.sleep();
    }
}
