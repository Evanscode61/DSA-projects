from collections import Counter
import heapq
from typing import List


class TopKFrequentStream:
    def __init__(self):
        self.freq = Counter()
        self.heap = []
        self.in_heap = set()
        self.lazy_deleted = set()

    def add(self, x: int) -> None:
        self.freq[x] += 1

        if x in self.in_heap:
            self.lazy_deleted.add(x)

        heapq.heappush(self.heap, (self.freq[x], x))
        self.in_heap.add(x)

        while len(self.heap) > 1000:  # adjust limit if needed
            f, num = heapq.heappop(self.heap)
            self.in_heap.remove(num)

    def remove(self, x: int) -> None:
        if x not in self.freq or self.freq[x] == 0:
            return
        self.freq[x] -= 1
        if self.freq[x] == 0:
            del self.freq[x]
        if x in self.in_heap:
            self.lazy_deleted.add(x)

    def get_top_k(self, k: int) -> List[int]:
        if k <= 0:
            return []

        temp = []
        seen = set()

        while self.heap and len(temp) < k:
            freq, num = heapq.heappop(self.heap)
            if num in self.lazy_deleted or num not in self.freq:
                self.in_heap.discard(num)
                continue
            if num in seen:
                continue
            seen.add(num)
            heapq.heappush(temp, (freq, num))

        self.heap = temp
        self.in_heap = seen.copy()
        self.lazy_deleted.clear()

        result = [num for _, num in sorted(temp, reverse=True)]
        return result[:k]


# Example
if __name__ == "__main__":
    s = TopKFrequentStream()

    for x in [5, 7, 5, 3, 5, 7, 3, 5, 2, 7, 7, 7, 3]:
        s.add(x)

    print(s.get_top_k(3))  # [7, 5, 3] or [5, 7, 3]

    s.remove(7)
    s.remove(7)
    s.remove(5)

    print(s.get_top_k(3))