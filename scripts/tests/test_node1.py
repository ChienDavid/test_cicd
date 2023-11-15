
import sys
sys.path.append('../scripts')

import rospy
from node1 import NODE_1

class TestNode1:
    def test_trajectory(self):
        rospy.init_node("node1")
        start = (0., 0.)
        goal = (10., 15.)
        node1 = NODE_1(start, goal)

        trajectory = node1.generate_trajectory(start, goal, num=100)
        assert len(trajectory) == 100, "Trajectory should have 100 waypoints"

    
