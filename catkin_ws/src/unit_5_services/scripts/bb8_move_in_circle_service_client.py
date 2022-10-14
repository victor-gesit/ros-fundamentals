#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node("call_bb8_in_circle_node")

move_circle_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)

move_in_circle_req = EmptyRequest()

result = move_circle_service(move_in_circle_req)

print("Res... ", result)
