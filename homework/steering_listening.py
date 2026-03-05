#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def callback(msg):
    rospy.loginfo("Received cmd_vel:")
    rospy.loginfo("Linear x: %.2f", msg.linear.x)
    rospy.loginfo("Angular z: %.2f", msg.angular.z)
    rospy.loginfo("-------------------------")

def listener():
    rospy.init_node('steering_listener', anonymous=True)
    rospy.Subscriber('/turtle1/cmd_vel', Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
