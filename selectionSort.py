class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            imin = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[imin]:
                    imin = j
            arr[i], arr[imin] = arr[imin], arr[i]
       return arr
