class Solution:
  def rev(self, b):
    if b == ")":
      return "("
    elif b == "}":
      return "{"
    elif b == "]":
      return "["
      
  def isValid(self, s):
    seq = []
    openings = ["(","{","["]
    closings = [")","}","]"]
    
    for i in s:
      if i in openings :
        seq.append(i)
      elif i in closings:
        if seq.pop() != self.rev(i):
          return False
    
    if len(seq) == 0:
      return True
    else:
      return False

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = "({})[]"

# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))