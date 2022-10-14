#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse


def callback(request):
    duration = request.duration
    res = MyCustomServiceMessageResponse()
    if duration == 5:
        res.success = True
    else:
        res.success = False
    return res

rospy.init_node("service_client")
server = rospy.Service("/my_service",
                       MyCustomServiceMessage, callback)

rospy.spin()
