#!/usr/bin/env python
import rospy
from common_msgs.msg import Coordinate

def callback(msg):
    print "subscribe: ", msg.radius, msg.vec.x, msg.vec.y, msg.vec.z

rospy.init_node('Coordinate_sub')
sub = rospy.Subscriber('hw3_topic_msg', Coordinate, callback)
rospy.spin()

