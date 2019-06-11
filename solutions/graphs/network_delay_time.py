#! /usr/bin/env python
"""
Problem

    There are 'N' network nodes, labelled '1' to 'N'.

    Given 'times', a list of travel times as directed edges 'times[i] = (u, v,
    w)', where 'u' is the source node, 'v' is the target node, and 'w' is the
    time it takes for a single to travel from source to target.

    Now, as send a signal from a certain node 'K'. How long will it take for
    all nodes to receive the signal? If it is impossible, return -1.

Example 1

         2
        / |
       /  v
    1<    3
         /
        /
       /
    4 <

    Input

        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        N = 4
        K = 2

    Output

        2

Note

    * N will be in the range [1, 100].
    * K will be in the range [1, N].
    * The length of 'times' will be in the range [1, 6000]
    * All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100
"""
from functools import total_ordering
import heapq
import math
from typing import List, Tuple, Union


@total_ordering
class Vertex:
    def __init__(self):
        self.distance = math.inf
        self.parent = None
        self.edges = []

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self.distance == self.distance


class Edge:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight


SourceVertexIndex = int
DestinationVertexIndex = int
TravelTime = int
TravelTimeEntry = Tuple[SourceVertexIndex, DestinationVertexIndex, TravelTime]
Metric = List[TravelTimeEntry]
Graph = List[Vertex]


def _relaxation(source: Vertex, destination: Vertex, weight: int) -> None:
    total_distance = source.distance + weight
    if destination.distance > total_distance:
        destination.distance = total_distance
        destination.parent = source


def _find_maxium_distance(
    graph: Graph, source_index: SourceVertexIndex
) -> Union[TravelTime, None]:
    maximum_distance = None
    min_heap: List = []
    graph[source_index].distance = 0

    for vertex in graph[1:]:
        heapq.heappush(min_heap, vertex)

    while len(min_heap) != 0:
        vertex = heapq.heappop(min_heap)
        for edge in vertex.edges:
            _relaxation(vertex, edge.destination, edge.weight)
        if vertex.distance == math.inf:
            return None
        elif (not maximum_distance) or (vertex.distance > maximum_distance):
            maximum_distance = vertex.distance
        heapq.heapify(min_heap)
    return maximum_distance


def find_network_delay_time(
    travel_metric: Metric, number_of_nodes: int, source: SourceVertexIndex
) -> Union[TravelTime, None]:
    """Finds a time to deliver a packet to each node of the vertex

    This method first calculates shortest path to reach each vertexes from a
    source vertex using Dijkstra's shortest path finding algorithm. Once
    shortest path to reach each vertex is calculated, this method will find
    maximum distance amongst all other vertexes and returns founded maximum
    distance.

    If there are any vertexes which are unreachable by a source vertex then
    this method returns 'None' to indicate that some nodes will always miss
    packets if it is routed from given source node.
    """
    graph = [Vertex() for _ in range(number_of_nodes + 1)]
    for source_node, destination_node, time in travel_metric:
        destination_vertex = graph[destination_node]
        edge = Edge(destination_vertex, time)
        graph[source_node].edges.append(edge)

    maximum_distance = _find_maxium_distance(graph, source)
    return maximum_distance if maximum_distance != 0 else None
