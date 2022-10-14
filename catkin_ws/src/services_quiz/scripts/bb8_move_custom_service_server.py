#! /usr/bin/env python
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist

def callback(req):
    side = req.side
    repetitions = req.repetitions
    print("Req: ", side, repetitions)
    make_square_movements(side, repetitions)
    res = BB8CustomServiceMessageResponse()
    res.success = True
    print("Done processing request")
    return res

def go_straight(side):
    print("Going Straing: ", side)
    data.linear.x = linear_speed
    data.angular.z = 0
    publisher.publish(data)

    init_count = 0
    while init_count < side:
        init_count += 1
        rate.sleep()
    print("Done going straight")

def stop():
    print("Stopping")
    data.linear.x = 0
    data.angular.z = 0
    publisher.publish(data)
    print("Done stopping")

def turn():
    print("Turning...")
    data.linear.x = 0
    data.angular.z = turn_speed
    publisher.publish(data)

    init_count = 0

    while init_count < 5:
        init_count += 1
        rate.sleep()
    
    stop()
    print("Done turning")

def make_square_movements(side, repetitions):
    init_count = 0
    while init_count < repetitions:
        make_square_movement(side)
        init_count += 1

def make_square_movement(side):
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

rospy.init_node("services_quiz_server_node")

linear_speed = 0.6
turn_speed = 0.3
rate = rospy.Rate(1)

data = Twist()
publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
service = rospy.Service("/move_bb8_in_square_custom", BB8CustomServiceMessage, callback)

rospy.spin()