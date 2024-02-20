# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/2/20 21:44
# @Author   : juhao666
# Dijkstra  : 狄克斯特拉算法
# page 108

from collections import deque


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def output_lowest_cost_path(parent):
    stack = []
    next_node = "fin"
    stack.append(next_node)
    while next_node in parent:
        next_node = parent[next_node]
        stack.append(next_node)
    output = ' -> '.join(stack[::-1])
    print(output)


if __name__ == '__main__':
    # graph
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    graph["fin"] = {}

    # costs
    infinity = float("inf")
    costs = {"a": 6, "b": 2, "fin": infinity}

    # parent
    parent = {}
    parent["a"] = "start"
    parent["b"] = "start"
    parent["fin"] = None

    processed = []
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parent[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    # print(costs)
    # print(processed)
    # print(parent)
    output_lowest_cost_path(parent)
