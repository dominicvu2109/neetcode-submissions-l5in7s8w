class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_tracker = defaultdict(list)
        most_common = []
        for number in nums:
            frequency_tracker[number].append(number)
        
        val_list = sorted(frequency_tracker.values(), key = len, reverse= True)

        for group in val_list[:k]:
            most_common.append(group[0])
        
        return most_common