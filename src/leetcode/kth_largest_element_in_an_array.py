class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        occurences = dict()
        
        for num in nums:
            if not occurences.get(num):
                occurences[num] = 0
            occurences[num] += 1
            
        elOccurences = []

        for key, value in occurences.items():
            elOccurences.append([value, key])
            
        self.__nth_element(elOccurences, k)
        
    def __nth_element(self, elOccurences: List[List[int]], k: int):
        print(elOccurences)
        for elOccurence in elOccurences:
            pass