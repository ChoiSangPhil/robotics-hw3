#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3
from common_msgs.msg import Int_Vector

rospy.init_node('Int_Vector_pub')
pub = rospy.Publisher('hw3_topic_msg', Int_Vector, queue_size=1)
msg = Int_Vector()
rate = rospy.Rate(2)

while not rospy.is_shutdown():
    msg.num = rospy.get_rostime() % 9 + 1
    msg.vec = Vector3(x=num, y=num*2, z=num**2)
    pub.publish(msg)
    print "publish: ", msg.vec.x, msg.vec.y, msg.vec.z
    rate.sleep()
