#! /usr/bin/env python

import rospy
from my_subscriber_example_pkg.msg import Age

pub = rospy.Publisher("/robot_age", Age, queue_size=1)

age = Age()
age.years = 30
age.months = 5
age.days = 20

while not rospy.is_shutdown():
    pub.publish(age)