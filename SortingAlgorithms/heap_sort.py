class Heap:
    def __init__(self, right, numbers):
        self.right = right
        self.numbers = numbers
        self.build_heap()

    def build_heap(self):
        for i in range(self.right // 2 - 1, -1, -1):
            self.heapify(i, self.right)

    def heapify(self, start, heap_size):
        while True:
            left = 2 * start + 1
            right = 2 * start + 2
            max = start
            if left < heap_size and self.numbers[left] > self.numbers[max]:
                max = left
            if right < heap_size and self.numbers[right] > self.numbers[max]:
                max = right
            if max == start:
                return
            self._swap(max, start)
            start = max

    def remove_max(self):
        self.right -= 1
        self._swap(0, self.right)
        self.heapify(0, self.right)

    def _swap(self, i, j):
        self.numbers[i], self.numbers[j] = self.numbers[j], self.numbers[i]


def heap_sort(values):
    heap = Heap(len(values), values)
    for i in range(len(values) - 1, 0, -1):
        heap.remove_max()
