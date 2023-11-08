#!/usr/bin/env python3

import rospy

class TEST:
    def __init__(self):
        print("Let's test")
        print("First: Test Python3 working in ROS")


def main():
    rospy.init_node("test_cicd")
    test = TEST()

if __name__=="__main__":
    main()

