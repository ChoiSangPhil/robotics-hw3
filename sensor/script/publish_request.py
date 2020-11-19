#!/usr/bin/env python
import rospy
import random
import math
from geometry_msgs.msg import Vector3
from common_msgs.msg import Coordinate
from common_msgs.srv import XORGate, XORGateRequest

rospy.init_node('HW3_pub')
pub = rospy.Publisher('hw3_topic_msg', Coordinate, queue_size=1)
requester = rospy.ServiceProxy('hw3_service', XORGate)
msg = Coordinate()
rate = rospy.Rate(2)
count = 1

while not rospy.is_shutdown():
    msg.radius = random.randint(1,10)
    theta = math.radians(random.randint(1,89))
    r_cos = round(msg.radius*math.cos(theta),2)
    r_sin = round(msg.radius*math.sin(theta),2)
    height = round(random.randint(1,9),1)
    msg.vec = Vector3(x=r_cos, y=r_sin, z=height)
    print "publish: ", msg.radius, msg.vec.x, msg.vec.y, msg.vec.z
    if count % 10 == 0:
        req = XORGateRequest(A=random.randint(0,1), B=random.randint(0,1))
        res = requester(req)
        print count, "request:", req.A, req.B, "response:", res.F
    pub.publish(msg)
    rate.sleep()
    count += 1

