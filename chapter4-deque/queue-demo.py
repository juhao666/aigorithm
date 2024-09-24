# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/9/23 21:09
# @Author   : juhao666

import queue

if __name__=="__main__":
    q = queue.Queue()

    q.put(1)
    q.put(2)

    while q.not_empty:
        print(q.get())

