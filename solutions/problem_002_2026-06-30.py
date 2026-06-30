"""
Problem #2
Date: 2026-06-30
Task: Write a Python implementation of K-Means clustering from scratch with a simple example.


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define a function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    # Calculate the difference in x and y coordinates
    x_diff = point1[0] - point2[0]
    y_diff = point1[1] - point2[1]
    
    # Calculate the Euclidean distance using the Pythagorean theorem
    distance = np.sqrt(x_diff ** 2 + y_diff ** 2)
    
    return distance

# Define a function to initialize centroids randomly
def initialize_centroids(data, k):
    # Choose k random points from the data as centroids
    indices = np.random.choice(len(data), k, replace=False)
    centroids = data[indices]
    
    return centroids

# Define a function to assign each data point to the closest centroid
def assign_clusters(data, centroids):
    # Initialize an array to store the cluster assignments
    clusters = np.zeros(len(data))
    
    # Iterate over each data point
    for i, point in enumerate(data):
        # Initialize the minimum distance and the closest centroid
        min_distance = float('inf')
        closest_centroid = -1
        
        # Iterate over each centroid
        for j, centroid in enumerate(centroids):
            # Calculate the distance between the point and the centroid
            distance = euclidean_distance(point, centroid)
            
            # Update the minimum distance and the closest centroid if necessary
            if distance < min_distance:
                min_distance = distance
                closest_centroid = j
        
        # Assign the point to the closest centroid
        clusters[i] = closest_centroid
    
    return clusters

# Define a function to update the centroids based on the cluster assignments
def update_centroids(data, clusters, k):
    # Initialize new centroids as the mean of each cluster
    new_centroids = np.zeros((k, 2))
    
    # Iterate over each cluster
    for i in range(k):
        # Get the points in the current cluster
        cluster_points = data[clusters == i]
        
        # Calculate the mean of the cluster points
        if len(cluster_points) > 0:
            new_centroids[i] = np.mean(cluster_points, axis=0)
    
    return new_centroids

# Define the K-Means clustering algorithm
def kmeans_clustering(data, k, max_iterations=100):
    # Initialize centroids randomly
    centroids = initialize_centroids(data, k)
    
    # Iterate until convergence or the maximum number of iterations
    for _ in range(max_iterations):
        # Assign each data point to the closest centroid
        clusters = assign_clusters(data, centroids)
        
        # Update the centroids based on the cluster assignments
        new_centroids = update_centroids(data, clusters, k)
        
        # Check for convergence
        if np.all(centroids == new_centroids):
            break
        
        # Update the centroids
        centroids = new_centroids
    
    return clusters, centroids

# Example usage
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
