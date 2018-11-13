""" Amazon Interview question. Given several 2-tuple (points) away from the origin.
Find the k-points closest to the origin in ascending order. Python 3. Also runs python 2.
"""
import math
import heapq

the_origin = (0,0)
all_tuples = [ (30,2), (1,1), (3.3,40), (.3,10), (0,9), (3,3), (2,2) ,(1,0), (55,22)] # sample points

def pyt_distance(origin,point): # distance between 2 points.
  return math.sqrt( (point[0] - origin[0])**2 + (point[1] - origin[1])**2 )


# Solution 1.bubble sorting complexity O(n^2) distances alongside corresponding tuples. Return the k points with the shortest distances to the origin.
def entangled_sort(k, origin, tuples):
  distances = []
  for i in range(0, len(tuples)):
    distances.append(pyt_distance(origin,tuples[i]))

  for i in range(0,len(distances)):
    for j in range(i,len(distances)):
      if distances[j] < distances[i]:
        #swap both distances and tuples accordingly.
        temp_dist = distances[j]; temp_tuple = tuples[j];
        distances[j] = distances[i]; tuples[j] = tuples[i];
        distances[i] = temp_dist; tuples[i] = temp_tuple;
  return tuples[0:len(tuples)]



"""
Solution 2: Improved method. Heaps are designed to solve a very specific problem,
they allow removal of the largest (or smallest in min_heap) item from a collection.
Build a max heap with k-points. Go down the remaining k to n tuples,
then replace max_tuple when next distance is smaller. Re-Heapify after each swap.
Items that don't belong in the bottom k-tuples will be removed. The heapify is outsourced to a python Import heapq.
"""
def max_heap_solution(k, origin, tuples):
  dist_tuples = [] #List of distances with its corresponding points.
  for i in range(0, len(tuples)):
    dist_tuples.append([pyt_distance(origin,tuples[i]), tuples[i] ])

  bottom_k = dist_tuples[0:k] # first k items thrown into an array.
  heapq._heapify_max(bottom_k) # The array is max-heaped. O(k)
  for i in range(k,len(dist_tuples)):
    if ( bottom_k[0][0] > dist_tuples[i][0] ): # next item is smaller than max, swap and Re-Heapify
        bottom_k[0] = dist_tuples[i]
        heapq._heapify_max(bottom_k)

  return bottom_k










#print(entangled_sort(3, the_origin, all_tuples))
print(max_heap_solution(3, the_origin, all_tuples))
