# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/2/20 21:05
# @Author   : juhao666
# bfs       :广度优先搜索算法
# page 85

from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    graph = {"you": {"Bob", "Alice", "Claire"}, "Bob": {"Anuj", "Peggy"}, "Alice": {"Peggy"},
             "Claire": {"Thom", "Jonny"}, "Anuj": [], "Peggy": [], "Thom": [], "Jonny": []}
    print(graph)

    search("you")
