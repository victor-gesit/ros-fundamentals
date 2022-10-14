#! /usr/bin/env python

import rospy
import actionlib
from std_msgs.msg import Empty
from actions_quiz.msg import CustomActionMsgAction, CustomActionMsgFeedback, CustomActionMsgResult


class TakeOffLand(object):
    def __init__(self):
        rospy.init_node("custom_action_node")
        self._as = afctionlib.SimpleActionServer(
            "action_custom_msg_as", CustomActionMsgAction, self.callback, False)
        
        self.travel_time = 2
        self.rate = rospy.Rate(1)
        self._as.start()
        self.start_time = 0
        self.current_state = "DEFAULT"
        self.cancelled = False 
        self.lift()

    def callback(self, goal):
        g = goal.goal
        
        if g == "TAKEOFF" and self.current_state != "TAKEOFF":
            self.current_state = "TAKEOFF"
            self.lift()
            while not self.cancelled:
                print("!! @@ ##")
                if self._as.is_preempt_requested():
                    rospy.loginfo("The goal has been cancelled/preempted")
                    self._as.set_preempted()
                    break
                self.one_sec_pause()
                fb = CustomActionMsgFeedback()
                fb.feedback = self.current_state
                self._as.publish_feedback(fb)

        elif g == "LAND":
            self.land()
            self.cancelled = True
            self.land()
            res = CustomActionMsgResult()
            self._as.set_succeeded(res)

    def one_sec_pause(self):
        rate = rospy.Rate(1)
        init_time = 0
        while init_time <= 4:
            print("pausing ", init_time)
            init_time += 1
            rate.sleep()

    def lift(self):
        print("Lifting")
        pub = rospy.Publisher("/drone/takeoff", Empty, queue_size=4)
        cmd = Empty()
        pub.publish(cmd)

        init_time = 0
        rate = rospy.Rate(1)
        while init_time <= 4:
            print("HAHAH ", init_time)
            init_time += 1
            rate.sleep()
        print("Done Lifting")

    def land(self):
        print("Start Landing")
        pub = rospy.Publisher("/drone/land", Empty, queue_size=1)
        cmd = Empty()
        pub.publish(cmd)

        init_time = 0
        rate = rospy.Rate(1)
        while init_time <= self.travel_time:
            print("Land... ", init_time)
            init_time += 1
            rate.sleep()
        print("Done Landing")
        

if __name__ == "__main__":
    TakeOffLand()
    rospy.spin()
