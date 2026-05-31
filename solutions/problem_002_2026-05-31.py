"""
Problem #2
Date: 2026-05-31
Task: Write a Python implementation of K-Means clustering from scratch with a simple example.


import numpy as np

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    # Calculate the difference in each dimension and square it
    squared_diffs = (point1 - point2) ** 2
    # Calculate the sum of the squared differences
    sum_squared_diffs = np.sum(squared_diffs)
    # Calculate the square root of the sum of the squared differences
    distance = np.sqrt(sum_squared_diffs)
    return distance

# Define a function to initialize the centroids randomly
def initialize_centroids(data, k):
    # Randomly select k data points as the initial centroids
    indices = np.random.choice(data.shape[0], k, replace=False)
    centroids = data[indices, :]
    return centroids

# Define a function to assign each data point to the closest centroid
def assign_clusters(data, centroids):
    # Initialize an array to store the cluster assignments
    cluster_assignments = np.zeros(data.shape[0], dtype=int)
    # Iterate over each data point
    for i, point in enumerate(data):
        # Initialize the minimum distance and the index of the closest centroid
        min_distance = float('inf')
        closest_centroid_index = -1
        # Iterate over each centroid
        for j, centroid in enumerate(centroids):
            # Calculate the distance between the point and the centroid
            distance = euclidean_distance(point, centroid)
            # If the distance is less than the minimum distance, update the minimum distance and the index of the closest centroid
            if distance < min_distance:
                min_distance = distance
                closest_centroid_index = j
        # Assign the point to the closest centroid
        cluster_assignments[i] = closest_centroid_index
    return cluster_assignments

# Define a function to update the centroids
def update_centroids(data, cluster_assignments, k):
    # Initialize an array to store the updated centroids
    updated_centroids = np.zeros((k, data.shape[1]))
    # Iterate over each cluster
    for i in range(k):
        # Get the data points assigned to the current cluster
        cluster_points = data[cluster_assignments == i]
        # If there are data points assigned to the current cluster, calculate the new centroid
        if cluster_points.shape[0] > 0:
            updated_centroids[i] = np.mean(cluster_points, axis=0)
    return updated_centroids

# Define a function to perform K-Means clustering
def kmeans_clustering(data, k, max_iterations=100):
    # Initialize the centroids randomly
    centroids = initialize_centroids(data, k)
    # Iterate over each iteration
    for _ in range(max_iterations):
        # Assign each data point to the closest centroid
        cluster_assignments = assign_clusters(data, centroids)
        # Update the centroids
        updated_centroids = update_centroids(data, cluster_assignments, k)
        # If the centroids have not changed, stop iterating
        if np.all(centroids == updated_centroids):
            break
        # Update the centroids
        centroids = updated_centroids
    return cluster_assignments, centroids

# Example usage
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    data = np.random.rand(100, 2)
    
    # Perform K-Means clustering
    k = 3
    cluster_assignments, centroids = kmeans_clustering(data, k)
    
    # Print the cluster assignments and centroids
    print("Cluster Assignments:")
    print(cluster_assignments)
    print("Centroids:")
    print(centroids)
