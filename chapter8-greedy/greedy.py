# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/2/21 22:52
# @Author   : juhao666
# chapter 123 Greedy 贪婪算法

# 用最少的电台尽可能覆盖所有州，剩下的电台就可以关闭了
if __name__ == '__main__':
    # 这么多州
    states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

    # stations['k1'] = set(['id', 'av', 'ut'])
    # stations['k2'] = set(['wa', 'id', 'mt'])
    # stations['k3'] = set(['or', 'nv', 'ca'])
    # stations['k4'] = set(['nv', 'ut'])
    # stations['k5'] = set(['ca', 'az'])
    # 每个电台k1,k2...都可以覆盖不同的州
    stations = {'k1': {'id', 'nv', 'ut'},
                'k2': {'wa', 'id', 'mt'},
                'k3': {'or', 'nv', 'ca'},
                'k4': {'nv', 'ut'},
                'k5': {'ca', 'az'}
                }
    final_stations = set()
    # 州没处理完就一直跑
    while states_needed:
        best_station = None  # 用来存放最佳station
        states_covered = []  # 用来保存覆盖了最多的州列表
        # 遍历所欲stations 找到cover最多城市的那个station
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = states
        states_needed -= states_covered
        final_stations.add(best_station)
    print(final_stations)

    print(sorted(final_stations))
