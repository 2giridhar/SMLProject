__author__ = 'Kiran'
import random
import numpy as np
import csv


def save_data(file_name, data):
    cluster_file = open(file_name, "a")
    csv_file = csv.writer(cluster_file)
    for row in data:
        csv_file.writerow(row)


if __name__ == "__main__":
    center_data = np.genfromtxt("Clusters/Centers.csv", delimiter=',', dtype=int)
    sample_data = []
    for i in range(len(center_data)):
        print(i)
        cluster_data = np.genfromtxt("Clusters/Cluster" + str(i) + ".csv", delimiter=',', dtype=int)
        len = cluster_data.shape[0] / 100
        random.shuffle(cluster_data)
        test_data = cluster_data[:len]
        train_data = cluster_data[len:]
        save_data("Train/Cluster" + str(i) + ".csv", train_data)
        save_data("Test/test.csv", test_data)
