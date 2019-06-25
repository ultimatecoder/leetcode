#! /usr/bin/env python
"""
Problem

    Design a class to find the Kth largest element in a stream. Note that it is
    the kth largest element in the sorted order, not the kth distinct element.

    Your 'KthLargest' class will have a constructor which accepts an integer
    'k' and an integer array 'nums', which contains initial elements from the
    stream. For each call to the method 'KthLargest.add', return the element
    representing the kth largest element in the stream.

Example

    int k = 3;
    int[] arr = [4, 5, 8, 2];
    KthLargest kthLargest = new KthLargest(3, arr);
    kthLargest.add(3); // return 4
    kthLargest.add(5); // return 5
    kthLargest.add(10); // return 5
    kthLargest.add(9); // return 8
    kthLargest.add(4); // return 8


Note

    You may assume that 'nums' length >= k - 1 and k >= 1
"""
from typing import List


class MinHeap:

    def __init__(self, numbers: List[int]) -> None:
        # First element is a gap filler
        self._numbers: List[int] = [-1]
        self._numbers.extend(numbers)
        self._build_heap()

    def _build_heap(self):
        for index in range(self.size // 2, 0, -1):
            self._heapify(index)

    def parent(self, index: int) -> int:
        return index // 2

    def left(self, index: int) -> int:
        return 2 * index

    def right(self, index: int) -> int:
        return (2 * index) + 1

    @property
    def size(self) -> int:
        return len(self._numbers) - 1

    def exchange(self, first_index: int, second_index: int) -> None:
        self._numbers[first_index], self._numbers[second_index] = (
            self._numbers[second_index], self._numbers[first_index]
        )

    def insert(self, number: int) -> None:
        self._numbers.append(number)
        self._decrease_key(self.size)

    def _decrease_key(self, index: int) -> None:
        while (
            (index > 1) and
            (self._numbers[self.parent(index)] > self._numbers[index])
        ):
            self.exchange(self.parent(index), index)
            index = self.parent(index)

    def insert_with_consistant_size(self, number: int) -> None:
        self._numbers[1] = number
        self._heapify(1)

    def get_minimum(self) -> int:
        return self._numbers[1]

    def extract_min(self) -> int:
        minimum = self._numbers[1]
        self._numbers[1] = self._numbers.pop()
        self._heapify(1)
        return minimum

    def _heapify(self, index: int) -> None:
        left = self.left(index)
        right = self.right(index)
        if (
            (left <= self.size) and
            (self._numbers[left] < self._numbers[index])
        ):
            small = left
        else:
            small = index

        if (
            (right <= self.size) and
            (self._numbers[right] < self._numbers[small])
        ):
            small = right

        if small != index:
            self.exchange(index, small)
            self._heapify(small)


class KthLargest:

    def __init__(self, k: int, numbers: List[int]) -> None:
        self.k = k
        self.min_heap = MinHeap(numbers)
        while self.min_heap.size > self.k:
            self.min_heap.extract_min()

    def add(self, value: int) -> int:
        if (
            (self.min_heap.size == self.k) and
            (value <= self.min_heap.get_minimum())
        ):
            return self.min_heap.get_minimum()
        elif self.min_heap.size < self.k:
            self.min_heap.insert(value)
            return self.min_heap.get_minimum()
        else:
            self.min_heap.insert_with_consistant_size(value)
            return self.min_heap.get_minimum()
