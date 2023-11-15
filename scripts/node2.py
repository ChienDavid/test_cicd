#!/usr/bin/env python3

from utils import node_math, node_np



def main():
    p1 = [0., 0.]
    p2 = [3., 4.]
    dist = node_math.distance(p1, p2)
    print(dist)

    avg = node_np.average(p1, p2)
    print(avg)


if __name__ == '__main__':
    main()
