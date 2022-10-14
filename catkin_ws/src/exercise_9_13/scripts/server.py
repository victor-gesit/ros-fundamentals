#! /usr/bin/env python

import rospy
import actionlib

from actionlib.msg import TestAction, TestFeedback, TestResult
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty


class SquareDroneMovement(object):
    def __init__(self):
        rospy.init_node('exercise_9_13_node')

        self._as = actionlib.SimpleActionServer(
            'square_drone', TestAction, self.callback, False)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.cmd = Twist()
        self.rate = rospy.Rate(1)
        self.linear_vel = 0.8

        self.travel_time = 3
        self._as.start()
        self.lift()


    def callback(self, goal):
        self.lift()
        start_time_secs = rospy.get_time()
        size = goal.goal
        current_side = 1

        while current_side <= 4:
            self.move_drone_straight_line(current_side, size)
            self.stop()

            feedback = TestFeedback()
            feedback.feedback = current_side
            self._as.publish_feedback(feedback)
            print("Published Feedback: ", feedback)
            current_side += 1

        stop_time_secs = rospy.get_time()
        time_diff = stop_time_secs - start_time_secs
        result = TestResult()
        print("Done", result, time_diff)
        result.result = int(time_diff)
        self._as.set_succeeded(result)

    def move_drone_straight_line(self, side, size):
        drone_vel = self.linear_vel
        print("SSS AAA ", side, size)
        if side == 1:
            drone_vel = self.linear_vel
            self.cmd.linear.x = drone_vel
            self.cmd.linear.y = 0
        if side == 2:
            drone_vel = self.linear_vel
            self.cmd.linear.x = 0
            self.cmd.linear.y = drone_vel
        if side == 3:
            drone_vel = -self.linear_vel
            self.cmd.linear.x = drone_vel
            self.cmd.linear.y = 0
        if side == 4:
            drone_vel = -self.linear_vel
            self.cmd.linear.x = 0
            self.cmd.linear.y = drone_vel

        self.pub.publish(self.cmd)

        init_time = 0
        while init_time <= size:
            init_time += 1
            self.rate.sleep()
        self.stop()

    def stop(self):
        self.cmd.linear.x = 0
        self.cmd.linear.y = 0
        self.cmd.linear.z = 0
        self.pub.publish(self.cmd)
        init_time = 0
        rate = rospy.Rate(1)
        while init_time <= 1:
            init_time += 1
            rate.sleep()

    def lift(self):
        print("Lifting")
        pub = rospy.Publisher("/drone/takeoff", Empty, queue_size=1)
        cmd = Empty()
        pub.publish(cmd)

        init_time = 0
        while init_time <= self.travel_time:
            init_time += 1
            self.rate.sleep()
        # self.stop()
        print("Done")

    def land(self):
        pub = rospy.Publisher("/drone/land", Empty, queue_size=1)
        cmd = Empty()
        pub.publish(cmd)


if __name__ == "__main__":
    SquareDroneMovement()
    rospy.spin()
