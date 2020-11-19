#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3
from common_msgs.msg import Coordinate

rospy.init_node('Coordinate_pub')
pub = rospy.Publisher('hw3_topic_msg', Coordinate, queue_size=1)
msg = Coordinate()
msg.radius = 1
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    r = msg.radius
    msg.vec = Vector3(x=r, y=r*2, z=r**2)
    pub.publish(msg)
    print "publish: ", msg.vec.x, msg.vec.y, msg.vec.z
    msg.radius += 1
    rate.sleep()
