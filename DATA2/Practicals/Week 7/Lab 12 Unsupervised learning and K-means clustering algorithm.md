# Lab Sheet

![[Lab 12 Usupervised Learning And K-Means Clustering Algorithm.pdf]]

# Answers
1) </br>
	1) <span></span>

	|            | (2,10) | (5, 8) | (1, 2) | Cluster |
	|------------|--------|--------|--------|---------|
	| P1 (2, 10) |    0   |   3.6  |   8.1  |    C1   |
	| P2 (2, 5)  |    5   |   4.2  |   3.2  |    C3   |
	| P3 (8, 4)  |   8.5  |    5   |   7.3  |    C2   |
	| P4 (5, 8)  |   3.6  |    0   |   7.2  |    C2   |
	| P5 (7, 5)  |   7.1  |   3.6  |   6.7  |    C2   |
	| P6 (6, 4)  |   7.2  |   4.1  |   5.4  |    C2   |
	| P7 (1, 2)  |   8.1  |   7.2  |    0   |    C3   |
	| P8 (4, 9)  |   2.2  |   1.4  |   7.6  |    C2   |

	</br>

	![[kmean0.png]]

	</br>

	2) </br>

	|            | (2,10) | (6, 6) | (1.5, 3.5) | Cluster |
	| ---------- | ------ | ------ | ---------- | ------- |
	| P1 (2, 10) | 0      | 5.7    | 6.5        | C1      |
	| P2 (2, 5)  | 5      | 4.1    | 1.6        | C3      |
	| P3 (8, 4)  | 8.5    | 2.8    | 6.5        | C2      |
	| P4 (5, 8)  | 3.6    | 2.2    | 5.7        | C2      |
	| P5 (7, 5)  | 7.1    | 1.4    | 5.7        | C2      |
	| P6 (6, 4)  | 7.2    | 2.0    | 4.5        | C2      |
	| P7 (1, 2)  | 8.1    | 6.4    | 1.6        | C3      |
	| P8 (4, 9)  | 2.2    | 3.6    | 6        | C1      |

	</br>

	![[kmean1.png]]

	</br>

	3) </br>

	|            | (3, 9.5) | (6.5, 5.2) | (1.5, 3.5) | Cluster |
	| ---------- | -------- | ---------- | ---------- | ------- |
	| P1 (2, 10) | 1.1      | 6.6        | 6.5        | C1      |
	| P2 (2, 5)  | 4.6      | 4.5        | 1.6        | C3      |
	| P3 (8, 4)  | 7.4      | 1.9        | 6.5        | C2      |
	| P4 (5, 8)  | 2.5      | 3.2        | 5.7        | C1      |
	| P5 (7, 5)  | 6        | 0.5        | 5.7        | C2      |
	| P6 (6, 4)  | 6.3      | 1.3        | 4.5        | C2      |
	| P7 (1, 2)  | 7.8      | 6.4        | 1.6        | C3      |
	| P8 (4, 9)  | 1.1      | 4.5        | 6          | C1      |

	</br>

	![[kmean2.png]]

	4) </br>

	|            | (3.7, 9) | (7, 4.3) | (1.5, 3.5) | Cluster |
	| ---------- | -------- | -------- | ---------- | ------- |
	| P1 (2, 10) | 2        | 7.6      | 6.5        | C1      |
	| P2 (2, 5)  | 4.3      | 5        | 1.6        | C3      |
	| P3 (8, 4)  | 6.6      | 1.0      | 6.5        | C2      |
	| P4 (5, 8)  | 1.6      | 4.2      | 5.7        | C1      |
	| P5 (7, 5)  | 5.2      | 0.7      | 5.7        | C2      |
	| P6 (6, 4)  | 5.5      | 1.0      | 4.5        | C2      |
	| P7 (1, 2)  | 7.5      | 6.4      | 1.6        | C3      |
	| P8 (4, 9)  | 0.3      | 5.6      | 6          | C1      |

	</br>

	![[kmean3.png]]

	**Code for the plots:**

	![[kmeans.py]]
	
</br>

2) 
	```jupyter
	import numpy as np
	from sklearn.datasets import make_blobs
	from sklearn.cluster import KMeans
	import matplotlib.pyplot as plt
	num_of_coordinates = 50
	initial_cluster_means = [(10,15),(4,7)]
	number_of_clusters = len(initial_cluster_means)
	dataset=make_blobs(n_samples=num_of_coordinates,centers=initial_cluster_means,n_features=2,cluster_std=2)
	random_data=dataset[0]
	print(random_data)
	print("\n")
	k=KMeans(n_clusters=number_of_clusters) 
	print(k)
	print("\n")
	cluster_data = k.fit_predict(random_data)
	print(cluster_data)
	```
	```jupyter
	%%capture
	x, y = np.split(random_data, 2, axis = 1)
	C1, C2 = random_data[np.where(cluster_data == 0)], random_data[np.where(cluster_data == 1)]
	C1_m, C2_m = C1.mean(axis= 0), C2.mean(axis= 0)
	colors = np.where(cluster_data == 0, "r", "b")
	plt.figure(figsize=(10, 10))
	plt.scatter(x.reshape(-1, 50), y.reshape(-1, 50), c = colors)
	plt.scatter([C1_m[0], C2_m[0]], [C1_m[1], C2_m[1]], marker = "X", c = ["darkred", "aqua"], s = 100)
	```

	![[plot.png|500]]

3)
 	```jupyter
	import math
	import random

	def k_means(initial_points, start_cluster_p):
		if initial_points == []:
			raise Exception("You have to define at least one initial point")
		elif type(start_cluster_p) == int and start_cluster_p > 0:
			start_cluster_p = random.sample(initial_points, start_cluster_p)
		elif (start_cluster_p == []) or (type(start_cluster_p) == int and start_cluster_p < 1):
			raise Exception("You have to define at least one cluster point")
		initial_points = np.array(initial_points)
		start_cluster_p = np.array(start_cluster_p)
		num_clusters = len(start_cluster_p)
		new_cluster_p = np.array([[]])
		colors = plt.cm.rainbow(np.linspace(0, 1, num_clusters))
		test = new_cluster_p == start_cluster_p
		while not(test):
			all_colors, clusters = [] , []
			if new_cluster_p.size != 0:
				start_cluster_p = new_cluster_p
			new_cluster_p = np.array([[]])
			for point in initial_points:
				temp = []
				for cluster_p in start_cluster_p:
					temp.append(euclidian_difference(point, cluster_p))
				clusters.append(temp.index(min(temp)))
				all_colors.append(colors[clusters[-1]])
			for i in range(num_clusters):
				new_cluster_p = np.append(new_cluster_p, [initial_points[np.where(np.array(clusters) == i)].mean(axis = 0)])
			new_cluster_p = new_cluster_p.reshape(num_clusters, 2)
			test = (new_cluster_p == start_cluster_p).all()
			plt.scatter(initial_points[:,0], initial_points[:,1], c = all_colors)
			plt.scatter(new_cluster_p[:,0], new_cluster_p[:,1], c = colors, marker = "X", s= 200)
			plt.show()

	def euclidian_difference(coordinates1, coordinates2):
		return round(math.sqrt((coordinates1[0] - coordinates2[0])**2 + (coordinates1[1] - coordinates2[1])**2), 1)

	k_means([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]], 3)
	```
	
	```jupyter
	k_means(random_data.tolist(), 3)
	```

[[Unsupervised learning and K-means|]]
