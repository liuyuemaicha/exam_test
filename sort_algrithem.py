# -*- coding: utf-8 -*-

# reference :https://www.cnblogs.com/skywang12345/p/3597597.html
# http://blog.csdn.net/morewindows/article/details/6678165
# http://python.jobbole.com/82270/
import copy
test_list = [10,23,1,53,654,54,16,646,65,3155,546,31]

def bubble_sort(array_list):
    length = len(array_list)
    for i in xrange(length):
        for j in xrange(1, length - i):
            if array_list[j] < array_list[j-1]:
                array_list[j-1], array_list[j] = array_list[j], array_list[j-1]

    return array_list
print bubble_sort(copy.deepcopy(test_list))


def select_sort(array_list):
    length = len(array_list)
    for i in xrange(length):
        for j in xrange(i+1, length):
            if array_list[i] > array_list[j]:
                array_list[i], array_list[j] = array_list[j], array_list[i]

    return array_list
print select_sort(copy.deepcopy(test_list))


def insert_sort(array_list):
    length = len(array_list)
    for i in xrange(1, length):
        j = i
        while j > 0:
            if array_list[j] < array_list[j-1]:
                array_list[j-1], array_list[j] = array_list[j], array_list[j-1]
            j -= 1
    return array_list
print insert_sort(copy.deepcopy(test_list))


def shell_sort(array_list):
    length = len(array_list)
    gap = length / 2
    while gap > 0:
        for i in xrange(gap):
            for j in xrange(i + gap, length, gap):
                if array_list[j] < array_list[j - gap]:
                    tmp = array_list[j]
                    k = j - gap
                    while k >= 0 and array_list[k] > tmp:
                        array_list[k + gap] = array_list[k]
                        k -= gap
                    array_list[k + gap] = tmp
        gap /= 2
    return array_list
print shell_sort(copy.deepcopy(test_list))


def quick_sort(array_list, l=None, r=None):
    if l == None or r == None:
        l, r = 0, len(array_list)-1
    left, right = l, r
    if l < r:
        k = array_list[left]
        while l < r:
            # print r
            while r > l and array_list[r] > k:
                r -= 1
            if r > l:
                array_list[l] = array_list[r]
                l += 1

            while l < r and array_list[l] < k:
                l += 1
            if r > l:
                array_list[r] = array_list[l]
                r -= 1
        array_list[l] = k
        quick_sort(array_list, left, l -1)
        quick_sort(array_list, l + 1, right)
    return array_list
print quick_sort(copy.deepcopy(test_list))

