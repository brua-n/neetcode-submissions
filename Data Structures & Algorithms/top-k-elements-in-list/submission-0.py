import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)          # {value: frequency}
        heap = []                      # min-heap of (frequency, value)

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)    # drop the least frequent

        return [num for freq, num in heap]