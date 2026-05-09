from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # map the charcount to their anagrams

        # for word in strs:
        #     sorted_word=''.join(sorted(word))
        #     res[sorted_word].append(word)

        for s in strs:
            count = 26 * [0]
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())
