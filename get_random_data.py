__author__ = 'Kiran'
from scipy import spatial
import numpy as np
import random
import sys
import operator
from collections import  defaultdict


def calculate_closest_cluster(center_data, sample_data):
    closest_cluster =  defaultdict(list)
    for sdata in sample_data:
        min_dist = sys.float_info.max
        index = 0
        cnt = 0
        sample = sdata[:-1].copy()
        for cdata in center_data:
            center = cdata[:-1].copy()
            dist = np.sqrt(sum((np.asarray(sample) - np.asarray(center)) ** 2))
            if dist < min_dist:
                min_dist = dist
                index = cnt
            cnt += 1

        closest_cluster[index].append(sdata)

    return closest_cluster


def knn(cluster_data, sample_data):
    correct_count = 0
    for sample in sample_data:
        dist_dict = {}
        cnt = 0
        sam = sample[:-1].copy()
        for cluster in cluster_data:
            clu = cluster[:-1].copy()
            dist_dict[cnt] = np.sqrt(sum((np.asarray(sam) - np.asarray(clu)) ** 2))
            cnt += 1

        dist_dict = sorted(dist_dict.items(), key=operator.itemgetter(1))
        k = 0
        hotel_cluster_id = defaultdict(int)
        for key in dist_dict:
            if k == 1:
                break
            hotel_cluster_id[cluster_data[key[0], 22]] += 1
            k += 1

        hotel_cluster_id = sorted(hotel_cluster_id.items(), key=operator.itemgetter(1))
        print "--------------------"
        print sample[22]
        print hotel_cluster_id[0][0]
        if sample[22] == hotel_cluster_id[0][0]:
            correct_count += 1

    return correct_count


if __name__ == "__main__":
    # Reading and storing input
    inp_file = raw_input("Enter the input file path: ")
    sample_data = random.sample(np.genfromtxt(inp_file, delimiter=',', dtype=int), 20000)
    # sample_data = random.sample(in_data, 10)

    center_data = np.genfromtxt("Clusters/Centers.csv", delimiter=',', dtype=int)
    closest_cluster = calculate_closest_cluster(center_data, sample_data)
    overall_correct = 0
    for key in closest_cluster:
        cluster_data = np.genfromtxt("Clusters/Cluster" + str(key) + ".csv", delimiter=',', dtype=int)
        correct_count = knn(cluster_data, closest_cluster[key])
        overall_correct += correct_count
    print ("-------------------")
    print (float(overall_correct) / len(sample_data))  * 100

    # sample_file = open("Sample/sample_data.csv", "wb")
    # new_file = csv.writer(sample_file)
    # for data in sample_data:
    #     new_file.writerow(data)


