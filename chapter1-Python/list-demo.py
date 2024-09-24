# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/9/23 20:51
# @Author   : juhao666
# demo how to use list
if __name__ == "__main__":
    colors = ["red", "black", "yeloow"]
    print(colors)

    # add a new color
    colors.append("purple")
    print("added new color purple:", colors)

    # read item in list one by one
    for c in colors:
        print(c)

