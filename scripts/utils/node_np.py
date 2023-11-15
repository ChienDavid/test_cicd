import numpy as np

def average(p1, p2):
    p = np.empty((0, 2))
    p = np.vstack((p, p1))
    p = np.vstack((p, p2))
    return p.mean(axis=0)

