
# refer https://www.geeksforgeeks.org/rotate-matrix-90-degree-without-using-extra-space-set-2/

from copy import deepcopy
# extra space solution
class matrix:
    #  clockwise : bottom to left or left to top
    def rotate_matrix(self, list1):
        n=len(list1)
        res= deepcopy(list1)
        for i in range(0,n):
          # till -1 and dec by -1
          for j in range(n-1, -1, -1):
              res[i][n-j-1] =list1[j][i]
        return res

#without extra space solution


obj= matrix()
res = obj.rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("res1", res)