from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap=defaultdict(list)
        for n in strs:
            srtd=tuple(sorted(n))
            hmap[srtd].append(n)
        return list(hmap.values())