class Solution:
  def celebrity(self, mat):
    N=len(mat)
    if N==1:
      return 0
    stack=[]
    for i in range(N):
      stack.append(i)
    while len(stack)!=1:
      a=stack.pop()
      b=stack.pop()
      if mat[a][b]==1:
        stack.append(b)
      else:
        stack.append(a)
    potential_candidate=stack.pop()
    for i in range(N):
      if mat[i][potential_candidate]==0:
        return -1
    for i in range(N):
      if mat[potential_candidate][i]==1 and i!=potential_candidate:
          return -1
    return potential_candidate