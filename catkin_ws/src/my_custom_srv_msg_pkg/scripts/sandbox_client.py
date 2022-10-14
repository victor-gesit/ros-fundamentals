#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

rospy.init_node("sandbox_service_client_node")

service_client = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage)

service_client_req = MyCustomServiceMessageRequest()
service_client_req.duration = 10

result = service_client(service_client_req)

print("Result: ", result)
