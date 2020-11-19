#!/usr/bin/env python
import rospy
from common_msgs.msg import Coordinate
from common_msgs.srv import XORGate, XORGateRequest

def callback(msg):
    print "subscribe: ", msg.radius, msg.vec.x, msg.vec.y, msg.vec.z

def service_callback(request):
    response = XORGateResponse(F=(request.A != request.B))
    print "request data:", request.A, request.B, ", response:", response.F
    return response

rospy.init_node('HW3')
sub = rospy.Subscriber('hw3_topic_msg', Coordinate, callback)
service = rospy.Service('xor_gate', XORGate, service_callback)
rospy.spin()
