__author__ = 'Kiran'
import random
import numpy as np

if __name__ == "__main__":
    center_data = np.genfromtxt("Clusters/Centers.csv", delimiter=',', dtype=int)
    sample_data = []
    for i in range(len(center_data)):
        cluster_data = np.genfromtxt("Clusters/Cluster" + str(i) + ".csv", delimiter=',', dtype=int)
        sample_data.append(random.sample(cluster_data, cluster_data.shape[0] / 100))

    print len(sample_data)
