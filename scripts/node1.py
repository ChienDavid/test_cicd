#!/usr/bin/env python3

import numpy as np
import rospy
from geometry_msgs.msg import Pose


class NODE_1:
    def __init__(self, start, goal) -> None:
        self.start = start
        self.goal = goal
        self.robot = Pose()

        self.pub_robot = rospy.Publisher('/robotpose', Pose, queue_size=10)
        self.rate = rospy.Rate(1)

    def generate_trajectory(self, start, goal):
        trajectory = np.empty((0, 2))
        x = np.linspace(start[0], goal[0], 50)
        y = np.linspace(start[1], goal[1], 50)
        for (xi, yi) in zip(x, y):
            trajectory = np.vstack((trajectory, (xi, yi)))
        return trajectory

    def execuse(self):
        self.trajectory = self.generate_trajectory(self.start, self.goal)
        idx = 0
        while not rospy.is_shutdown():
            new_pose = self.trajectory[idx]
            self.robot.position.x = new_pose[0]
            self.robot.position.y = new_pose[1]
            self.pub_robot.publish(self.robot)
            rospy.loginfo("Published pose {}: {}".format(idx, new_pose))
            self.rate.sleep()
            idx += 1
            if idx >= len(self.trajectory):
                break




def main():
    rospy.init_node("node1")

    start = (0., 0.)
    goal = (10., 15.)
    node1 = NODE_1(start, goal)

    rospy.loginfo('Node 1 started!')
    node1.execuse()
    rospy.loginfo('Node 1 finished!')



if __name__=="__main__":
    main()


