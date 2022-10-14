#! /usr/bin/env python

import rospy
import rospkg
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest

rospack = rospkg.RosPack()
release_traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/release_food.txt"
get_food_traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"
rospy.init_node("traj_service_client")

reproduce_trajectory_service = rospy.ServiceProxy("/execute_trajectory", ExecTraj)

reproduce_trajectory_service_req = ExecTrajRequest()


def perform_service():
    reproduce_trajectory_service_req.file = get_food_traj
    get_food_result = reproduce_trajectory_service(reproduce_trajectory_service_req)
    reproduce_trajectory_service_req.file = release_traj
    release_food_result = reproduce_trajectory_service(reproduce_trajectory_service_req)
    
    print("Get Food Result... ", get_food_result)
    print("Release Food Result... ", release_food_result)

while not rospy.is_shutdown():
    perform_service()