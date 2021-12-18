import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
plt.style.use('seaborn-whitegrid')
def difference(coordinates1, coordinates2):
    return round(math.sqrt((coordinates1[0] - coordinates2[0])**2 + (coordinates1[1] - coordinates2[1])**2), 1)

points = [(2, 10), (2, 5), (8, 4), (5, 8), (7, 5), (6, 4), (1, 2), (4, 9)]
initial_clusters = [(2, 10), (5, 8), (1, 2)]
means = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
clusters_average = []
colors = ['r', 'g', 'b', "darkred", "lime", "aqua"]
iteration = 0
while clusters_average != initial_clusters:
    if clusters_average != []:
        initial_clusters = clusters_average
    clusters_average = []
    counter = 1
    for i in points:
        mean = [difference(i, j) for j in initial_clusters]
        mean.append(mean.index(min(mean)))
        means[counter] = mean
        counter += 1
    for i in range(3):
        x, y = 0, 0
        points_in_cluster = [point for point in points if means[points.index(point)+1][3] == i]
        for point in points_in_cluster:
            x, y = x + point[0], y + point[1]
        clusters_average.append((round(x/len(points_in_cluster), 1), round(y/len(points_in_cluster), 1)))
    col = []
    points_x, points_y = [], []
    for point in points:
        points_x.append(float(point[0]))
        points_y.append(float(point[1]))
        if means[points.index(point)+1][3] == 0:
            col.append('r')
        elif means[points.index(point)+1][3] == 1:
            col.append('g')
        elif means[points.index(point)+1][3] == 2:
            col.append('b')
    counter = 0
    for cluster_point in clusters_average:
        points_x.append(float(cluster_point[0]))
        points_y.append(float(cluster_point[1]))
        points_x.append(initial_clusters[counter][0])
        points_y.append(initial_clusters[counter][1])
        col.append(colors[counter+3])
        if initial_clusters[counter] in points:
            col.append(colors[counter])
        else:
            col.append(colors[counter+3])
        counter += 1
    figure, ax = plt.subplots()
    for counter in range(3):
        min_x, min_y = 100, 100
        max_x, max_y = 0, 0
        for i in range(len(points_x)):
            if col[i] in (colors[counter], colors[counter+3]):
                if points_x[i] <= min_x:
                    min_x = points_x[i]
                if points_y[i] <= min_y:
                    min_y = points_y[i]
                if points_x[i] >= max_x:
                    max_x = points_x[i]
                if points_y[i] >= max_y:
                    max_y = points_y[i]
        if len([color for color in col if color in (colors[counter], colors[counter+3])]) > 3:
            ax.add_patch(patches.Rectangle((min_x-0.3, min_y-0.3),max_x-min_x+0.6, max_y-min_y+0.6, color=colors[counter], fill=False))
        else:
            ax.add_patch(patches.Rectangle((min_x-0.3, min_y-0.3),0.6, 0.6, color=colors[counter], fill=False))
    plt.xlim([0, 10])
    plt.ylim([0, 12])
    plt.scatter(points_x, points_y, c=col)
    counter = 0
    for cluster_point in clusters_average:
        plt.annotate("C%i = %s" % (counter+1, str(initial_clusters[counter])), (initial_clusters[counter][0], initial_clusters[counter][1]), c=colors[counter+3])
        if (cluster_point[0], cluster_point[1]) != (initial_clusters[counter][0], initial_clusters[counter][1]):
            plt.annotate("M%i = %s" %(counter+1,str(cluster_point)), (cluster_point[0], cluster_point[1]), c= colors[counter+3])
        counter += 1
    plt.savefig("/Users/bre.xit/Desktop/Uni Documents/Second Year/CS 2021/2022/DATA2/Practicals/Images/kmean" + str(iteration) + ".png")
    plt.clf()
    iteration += 1
    print(means, initial_clusters)
