class matrix:
    def zero_matrix(self, list1):
      rows=len(list1)
      cols=len(list1[0])
      rows_list=[]
      cols_list=[]
      for i in range(rows):
          for j in range(cols):
              if list1[i][j]==0:
                  if i not in rows_list:
                    rows_list.append(i)
                  if j not in cols_list:
                    cols_list.append(j)

      for i in rows_list:
          for j in  range(cols):
              list1[i][j]=0

      for i in cols_list:
          for j in range(rows):
              list1[j][i]=0

      print (list1)




obj= matrix()
res = obj.zero_matrix([[3, 0, 1], [2, 1, 5], [0, 1, 3], [7, 2, 4]])
print("res1", res)