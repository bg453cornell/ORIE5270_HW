import sys
import io
import numpy as np
from pyspark import SparkContext


sc = SparkContext('local[2]', 'hw4')

# Load the data
data = sc.textFile(sys.argv[1]).map(
   lambda line: np.array([float(x) for x in line.split(' ')])).cache()

# Load the initial centroids
centroids1 = sc.textFile(sys.argv[2]).map(
   lambda line: np.array([float(x) for x in line.split(' ')])).cache()


def min_distance(line, cur_c):
    min_distance = float("inf")
    min_distance_idx = 0
    for idx, c in cur_c:
        temp = np.linalg.norm(line - c)
        if temp < min_distance:
            min_distance = temp
            min_distance_idx = idx
    return min_distance_idx


try:
    sys.argv[3]
except IndexError:
    MAX_ITER = 100
else:
    MAX_ITER = int(sys.argv[3])


cur_centroids = centroids1.zipWithIndex().map(lambda l: (l[1], l[0])).collect()

for _ in range(MAX_ITER):
    cur_iter = data.map(lambda l: (min_distance(l, cur_centroids), l))
    aTuple = (0, 0)
    cur_iter_aggr = cur_iter.aggregateByKey(aTuple, lambda a, b: (a[0] + b, a[1] + 1),
                                            lambda a, b: (a[0] + b[0], a[1] + b[1]))
    new_c = cur_iter_aggr.mapValues(lambda v: v[0]/v[1]).collect()
    cur_centroids = new_c

final_result = sorted(cur_centroids, key=lambda k: k[0])

open('output_centroids.txt', 'w').close()
with io.open('output_centroids.txt', 'a', encoding='utf-8') as file:
    for _, c in final_result:
        file.write(' '.join([str(v) for v in c]))
        file.write('\n')

print("K-Means iterated", MAX_ITER, "times finished. See 'output_centroids.txt' for results.")