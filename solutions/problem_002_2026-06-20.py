"""
Problem #2
Date: 2026-06-20
Task: Write a Python implementation of K-Means clustering from scratch with a simple example.


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    # Calculate the difference in x and y coordinates
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    # Return the Euclidean distance
    return np.sqrt(dx**2 + dy**2)

# Define a function to initialize centroids randomly
def initialize_centroids(data, k):
    # Initialize an empty list to store the centroids
    centroids = []
    # Randomly select k points from the data as centroids
    for _ in range(k):
        centroid = data[np.random.randint(0, len(data))]
        centroids.append(centroid)
    # Return the list of centroids
    return np.array(centroids)

# Define a function to assign each point to the closest centroid
def assign_clusters(data, centroids):
    # Initialize an empty list to store the cluster assignments
    clusters = []
    # Iterate over each point in the data
    for point in data:
        # Initialize the minimum distance and the closest centroid
        min_distance = float('inf')
        closest_centroid = None
        # Iterate over each centroid
        for i, centroid in enumerate(centroids):
            # Calculate the distance between the point and the centroid
            distance = euclidean_distance(point, centroid)
            # If the distance is less than the minimum distance, update the minimum distance and the closest centroid
            if distance < min_distance:
                min_distance = distance
                closest_centroid = i
        # Append the cluster assignment to the list
        clusters.append(closest_centroid)
    # Return the list of cluster assignments
    return np.array(clusters)

# Define a function to update the centroids
def update_centroids(data, clusters, k):
    # Initialize an empty list to store the new centroids
    new_centroids = []
    # Iterate over each cluster
    for i in range(k):
        # Get the points in the current cluster
        cluster_points = data[clusters == i]
        # If the cluster is not empty, calculate the new centroid as the mean of the points
        if len(cluster_points) > 0:
            new_centroid = np.mean(cluster_points, axis=0)
        # If the cluster is empty, use the previous centroid
        else:
            new_centroid = np.array([0, 0])
        # Append the new centroid to the list
        new_centroids.append(new_centroid)
    # Return the list of new centroids
    return np.array(new_centroids)

# Define a function to perform K-Means clustering
def kmeans_clustering(data, k, max_iterations=100):
    # Initialize the centroids randomly
    centroids = initialize_centroids(data, k)
    # Iterate over the maximum number of iterations
    for _ in range(max_iterations):
        # Assign each point to the closest centroid
        clusters = assign_clusters(data, centroids)
        # Update the centroids
        new_centroids = update_centroids(data, clusters, k)
        # If the centroids have not changed, stop the iteration
        if np.all(centroids == new_centroids):
            break
        # Update the centroids
        centroids = new_centroids
    # Return the final cluster assignments and centroids
    return clusters, centroids

# Define a working example
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    data = np.random.rand(100, 2)
    
    # Perform K-Means clustering
    k = 3
    clusters, centroids = kmeans_clustering(data, k)
    
    # Plot the clusters and centroids
    plt.scatter(data[:, 0], data[:, 1], c=clusters)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200)
    plt.show()
