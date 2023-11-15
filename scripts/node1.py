#!/usr/bin/env python3

import numpy as np
import rospy
from geometry_msgs.msg import Pose


class NODE_1:
    def __init__(self, start: tuple, goal: tuple) -> None:
        self.start = start
        self.goal = goal
        self.robot = Pose()

        self.pub_robot = rospy.Publisher('/robotpose', Pose, queue_size=10)
        self.rate = rospy.Rate(1)

    def generate_trajectory(self, start: tuple, goal: tuple, num: int = 5):
        assert type(start) == tuple, 'Start position should be a tuple'
        assert type(goal) == tuple, 'Goal position should be a tuple'
        assert type(num) == int, 'Num should be an integer'

        trajectory = np.empty((0, 2))
        x = np.linspace(start[0], goal[0], num)
        y = np.linspace(start[1], goal[1], num)
        for (xi, yi) in zip(x, y):
            trajectory = np.vstack((trajectory, (xi, yi)))
        return trajectory

    def execuse(self):
        # generate trajectory
        self.trajectory = self.generate_trajectory(self.start, self.goal)

        # start execute
        idx = 0
        while not rospy.is_shutdown():
            # extract a new pose
            new_pose = self.trajectory[idx]
            self.robot.position.x = new_pose[0]
            self.robot.position.y = new_pose[1]

            # publish the pose
            self.pub_robot.publish(self.robot)
            rospy.loginfo("Published pose {}: {}".format(idx, new_pose))

            # sleep
            self.rate.sleep()

            # update index
            idx += 1
            if idx >= len(self.trajectory):
                rospy.loginfo("Robot is at goal: {}".format(new_pose))
                break

        while rospy.is_shutdown():
            rospy.loginfo("Hard shutdown")
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


