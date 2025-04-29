class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        
        def flip(k):
            arr[:k] = arr[:k][::-1]

        for size in range(n, 1, -1):
            max_index = arr.index(max(arr[:size]))
            
            if max_index == size - 1:
                continue  
            
           
            if max_index != 0:
                result.append(max_index + 1)
                flip(max_index + 1)
            
           
            result.append(size)
            flip(size)
        
        return result
