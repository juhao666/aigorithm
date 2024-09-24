# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/9/23 21:14
# @Author   : juhao666
# KMP to find the longest string

# build next list
# 给一个子串ABABC，生成next数组，数组中的值表示这个字母在子串中的公共最大长度
def build_next(patt):
    next = [0] # next 数字的第一位永远是0
    i = 1 # 让循环从1开始， 即patt的第二位开始
    preffix_len = 0 # 初始的最大匹配长度为0
    while i < len(patt): # 循环到patt的最后一位结束
        if patt[preffix_len] == patt[i]: # 如果当前第i个字符和最大匹配的那个相等
            preffix_len += 1 # 最大匹配长度 增加1
            next.append(preffix_len) # 当前i位置的最大匹配数就是preffix_len
            i += 1 # 往前进一步
        else: # 如果不相等，表示前后两个字符不相等，没有匹配上, 这是后分两种情况
            # 1 最大匹配长度为0， 就是之前一直没有匹配上的
            if preffix_len == 0:
                next.append(0) # 当前位置还是没匹配到，值为0
                i += 1 # 并且，往前进一步
            # 2  最大匹配长度>0， 表示之前已经有若干个匹配到了，只是加上现在i位置的字符后不匹配了。
            # 那就需要在之前匹配到的字符串中找一个子串，再加上当前i位置的字符，看是不是有前后匹配的情况
            else:
                # 这里是重点。 最大匹配长度减去1，这样就是在之前最长匹配的字符串中缩减一位，看看它能匹配的最大长度（这个长度值x 也是第x个字符）
                # 相当于拿到了最左侧的可匹配字符，在下一个循环中和i位置的进行匹配。注意，这里i没有再往前走
                preffix_len = next[preffix_len - 1]
    print("next list is ", next)
    return next


# find the position where the patt in string
# e.g.
#    string = ABAABABC
#    patt = ABABC
# the matched position should be 3
def find_longest_str(string, patt):
    # 首先要得到一个next数组，这是KMP算法的基础。
    next = build_next(patt)
    # i是string数组的下标
    i = 0
    # j是patt的下标
    j = 0
    # 循环直到遍历完string数组，而且i只能向前，不能后退
    while i < len(string):
        # 如果string里面第i个字符和patt里面第j个字符一样，两个数组个往前一步
        if string[i] == patt[j]:
            i += 1
            j += 1
        # 如果不匹配的话，这里就是KMP的精髓，我们本来是要从patt的第1个字符重新开始
        # 但是KMP的思路是，我们可以跳过前面已知的n个字符，因为patt中前面n个刚才是匹配的
        # 那这个n是多少呢，其实就是next数组中左边那位置对应的那个值
        # 所以 除了patt的第一位，因为第一位没有前一个
        elif j > 0:
            j = next[j-1]
        # 那如果j已经回到第1位了 还没找到连续匹配的，那string数组的i就往前一步
        else:
            i += 1
        # 如果j已经到patt的最后位置了，说明最长匹配的字符串已经找到了
        if j == len(patt) - 1:
            return i - j
    # 没找到的话返回-1
    return -1


if __name__=="__main__":
    string = "ABAABABC"
    print("the string is ", string)
    patt = "ABABC"
    print("the sub-string is ", patt)
    start = find_longest_str(string, patt)
    print("the longest sub-string start at ",start)
    print("find the longest sub-string in string is ", string[start:])