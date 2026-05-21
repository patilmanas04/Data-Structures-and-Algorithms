class Solution:
  def celebrity(self, mat):
    N=len(mat)
    for i in range(N):
      isCelebrity=True
      for j in range(N):
        if mat[j][i]==0:
          isCelebrity=False
        if i==j:
          continue
        if mat[i][j]==1:
          isCelebrity=False
      if isCelebrity:
        return i
    return -1