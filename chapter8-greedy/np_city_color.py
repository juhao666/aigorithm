# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/2/25 13:46
# @Author   : juhao666

# (Nondeterministic Polynomially，非确定性多项式
#  NP类问题数量很大，如完全子图问题、图着色问题、旅行商(TSP)问题等。

# 相邻城市颜色不同问题

def find_max_neighbours(cb):
    neighbour_count = 0
    city_max_nb = None
    for city, neighbours in cb.items():
        if len(neighbours) > neighbour_count:
            neighbour_count = len(neighbours)
            city_max_nb = city
    return city_max_nb


if __name__ == '__main__':
    cities = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    # city_neighbours['a'] = ['b', 'c', 'd']
    # city_neighbours['b'] = ['a', 'c']
    # city_neighbours['c'] = ['a', 'b', 'd', 'e']
    # city_neighbours['d'] = ['a', 'c', 'e', 'g']
    # city_neighbours['e'] = ['c', 'd', 'f']
    # city_neighbours['f'] = ['e', 'g']
    # city_neighbours['g'] = ['d', 'f']

    city_neighbours = {'a': ['b', 'c', 'd'],
                       'b': ['a', 'c'],
                       'c': ['a', 'b', 'd', 'e'],
                       'd': ['a', 'c', 'e', 'g'],
                       'e': ['c', 'd', 'f'],
                       'f': ['e', 'g'],
                       'g': ['d', 'f']
                       }
    city_colors = {'a': None,
                   'b': None,
                   'c': None,
                   'd': None,
                   'e': None,
                   'f': None,
                   'g': None}

    colors = {'red', 'yellow', 'white', 'green', 'pink', 'orange', 'brown'}
    used_colors = set()
    while city_neighbours:
        # 找出邻居最多的那个city
        city = find_max_neighbours(city_neighbours)
        # 把这些邻居的Color放到一个set中
        neighbours_colors = set([city_colors[key] for key in city_colors if key in city_neighbours[city]])
        # 当前city的color不能是这些邻居的color
        allowed_colors = colors - neighbours_colors
        # 这块处理一个case:
        # 如果某个颜色已经使用过，且当前邻居没有用，那就可以复用了
        if len(used_colors - neighbours_colors) > 0:
            # 拿到可以服用的color
            allowed_colors = allowed_colors & used_colors
        # 随便拿一个
        # color = allowed_colors.pop()
        # 每次都去第一个
        color = sorted(allowed_colors)[0]
        # 把这个color给当前city
        city_colors[city] = color
        # 新增一个使用的颜色到set
        used_colors.add(color)
        # 当前city已经有color了 可以从dict删除
        del city_neighbours[city]
    print(city_colors)
    print(used_colors)
    print(sorted(used_colors))