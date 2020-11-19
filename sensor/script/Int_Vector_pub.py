#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3
from common_msgs.msg import Int_Vector

rospy.init_node('Int_Vector_pub')
pub = rospy.Publisher('hw3_topic_msg', Int_Vector, queue_size=1)
msg = Int_Vector()
msg.num = 1
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    basis = msg.num
    msg.vec = Vector3(x=basis, y=basis*2, z=basis**2)
    pub.publish(msg)
    print "publish: ", msg.vec.x, msg.vec.y, msg.vec.z
    msg.num += 1
    rate.sleep()
