#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node("bb8_square_service")

service_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)

service_client_req = BB8CustomServiceMessageRequest()
service_client_req.side = 5
service_client_req.repetitions = 2

result = service_client(service_client_req)

print("Result: ", result)
