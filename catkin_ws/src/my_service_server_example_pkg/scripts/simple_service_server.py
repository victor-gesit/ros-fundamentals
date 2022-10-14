#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse

def my_callback(request):
    print("My callback has been called", request)
    return EmptyResponse()
    # return MyServiceResponse(len(request.words.split()))


rospy.init_node('service_server')
my_service = rospy.Service('/my_service', Empty, my_callback)

rospy.spin()
