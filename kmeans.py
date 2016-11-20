import sys
import numpy as np
import random
import csv


def assign_clusters(data, centroids):
    clusters = {}
    for point in data:
        min_distance = sys.float_info.max
        length = len(centroids)
        new_point = point
        new_point.pop()
        for i in range(0, length):
            center = centroids[i]
            center.pop()
            dist = np.dot(new_point, center)  # np.sqrt(sum((np.asarray(point) - np.asarray(centroids[i])) ** 2))
            if dist < min_distance:
                cluster_key = i
                min_distance = dist
        # noinspection PyBroadException
        try:
            curr_cluster = clusters[cluster_key]
            curr_cluster.append(point)
        except:
            clusters[cluster_key] = [point]
    return clusters


def generate_new_centroids(clusters):
    centroids = []
    keys = sorted(clusters.keys())
    for key in keys:
        centroids.append(np.mean(clusters[key], axis=0))
    return centroids


def compute_objective_function(centroids, clusters):
    keys = sorted(clusters.keys())
    objective_sum = 0
    for key in keys:
        for point in clusters[key]:
            new_point = point
            new_point.pop()
            center = centroids[key]
            center.pop()
            objective_sum += np.dot(new_point, center)
    return objective_sum


def centroids_converged(centroids, old_centroids, iterations):
    max_iterations = 100
    if iterations > max_iterations:
        return True
    return set([tuple(val) for val in centroids]) == set([tuple(val) for val in old_centroids])


def kmeans(data, k):
    old_centroids = random.sample(data, k)
    centroids = random.sample(data, k)
    iterations = 0
    clusters = {}

    while not centroids_converged(centroids, old_centroids, iterations):
        iterations += 1
        old_centroids = centroids
        clusters = assign_clusters(data, centroids)
        centroids = generate_new_centroids(clusters)
    return compute_objective_function(centroids, clusters)


def store_clusters(centroids, clusters):
    for cluster_id in clusters:
        cluster_file = open("Clusters/Cluster_" + cluster_id + ".csv", "wb")
        csv_file = csv.writer(cluster_file)
        for vector in clusters[cluster_id]:
            csv_file.writerow(vector)

    centers_file = open("Clusters/Centers.csv", "wb")
    new_file = csv.writer(centers_file)
    for cluster_id in clusters:
        new_file.writerow(centroids[cluster_id])


if __name__ == "__main__":
    # Reading and storing input
    inp_file = raw_input("Enter the input file path: ")
    kmeans(data=inp_file, k=50)
