#!/usr/bin/env python

import rospy
# from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from my_custom_srv_msg_pkg.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist

rospy.init_node('bb8_square_service')

speed_of_travel = 0.6
speed_of_turn = 0.3

def callback(request):
    print("Req: ", request)
    side = request.side
    repetitions = request.repetitions
    make_square_movements(side, repetitions)
    res = BB8CustomServiceMessageResponse()
    res.success = True
    return res


def make_square_movements(side, repetitions):
    square_movement(side)
    # init_count = 0
    # while init_count < repetitions:
    #     square_movement(side)
    #     init_count += 1


def turn_around(duration):
    data.linear.x = 0.2
    data.angular.z = 0.2
    publisher.publish(data)
    init_time = 0

    while not rospy.is_shutdown() and init_time < duration:
        init_time += 1
        rate.sleep()
        print("Init ", init_time)
    stop()


def square_movement(side):
    print("Starting Square Movement: ", side)
    go_straight(side)
    stop()
    turn()
    go_straight(side)
    stop()
    turn()
    go_straight(side)
    stop()
    turn()
    go_straight(side)
    stop()
    turn()


def turn():
    print("Turning")
    data.linear.x = 0
    data.angular.z = speed_of_turn
    publisher.publish(data)
    init_t = 0
    while init_t < 5:
        init_t += 1
        rate.sleep()
    stop()
    print("Done turning")


def go_straight(side):
    print("Going Straight", side)
    data.linear.x = speed_of_turn
    data.angular.z = 0
    publisher.publish(data)

    init_t = 0
    while init_t < side:
        init_t += 1
        rate.sleep()
    print("Done going straight")


def stop():
    print("Stopping")
    data.linear.x = 0
    data.angular.z = 0
    publisher.publish(data)
    print("Done Stopping")


rate = rospy.Rate(1)

data = Twist()
my_service = rospy.Service(
    '/move_bb8_in_square_custom', BB8CustomServiceMessage, callback)
publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rospy.spin()
