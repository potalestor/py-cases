from typing import List


class MinHeap:
    def __init__(self, list: List[int]):
        self.__heap = list
        self.__size = len(list)
        for i in range(self.__size >> 1, -1, -1):
            self.__minHeapify(i)

    def __minHeapify(self, i):
        li = 2*i + 1
        ri = 2*i + 2
        si = i
        if li < self.__size and self.__heap[i] > self.__heap[li]:
            si = li
        if ri < self.__size and self.__heap[si] > self.__heap[ri]:
            si = ri
        if si != i:
            self.__heap[i], self.__heap[si] = self.__heap[si], self.__heap[i]
            self.__minHeapify(si)

    def min(self):
        if self.__size > 0:
            return self.__heap[0]
        return None

    def replaceMin(self, item):
        self.__heap[0] = item
        self.__minHeapify(0)

    def pop(self):
        min = self.min()
        if min == None:
            return
        self.__heap[0] = self.__heap[-1]
        del self.__heap[-1]
        self.__size -= 1
        self.__minHeapify(0)
        return min

