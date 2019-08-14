class Solution: 
  def getRange(self, arr, target):
    if target not in arr:
      return [-1,-1]
    result = []
    result.append(arr.index(target))
    arr.reverse()
    result.append(len(arr) - 1 - arr.index(target))
    return result
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

