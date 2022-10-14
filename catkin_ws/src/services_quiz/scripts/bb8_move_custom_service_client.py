#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node("services_quiz_client_node")

service = rospy.ServiceProxy("/move_bb8_in_square_custom", BB8CustomServiceMessage)

service_req = BB8CustomServiceMessageRequest()
service_req.repetitions = 2
service_req.side = 2

result = service(service_req)


service_req.repetitions = 1
service_req.side = 5

result = service(service_req)

print("Result: ", result)

