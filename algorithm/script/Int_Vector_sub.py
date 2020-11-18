#!/usr/bin/env python

import rospy
from common_msgs.msg import Int_Vecter

def callback(msg):
    print "subscribe: ", msg.vec.x, msg.vec.y, msg.vec.z

rospy.init_node('Int_Vecter_sub')
sub = rospy.Subscriber('hw3_topic_msg', Int_Vecter, callback)
rospy.spin()

