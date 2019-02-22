class checkedit:
    def oneaway(self, string1, string2):
        count=0
        m=len(string1)
        n=len(string2)
        i=0
        j=0
        if abs(m-n)>1:
            return False
        while i<m and j<n:
          if string1[i]!=string2[j]:
             if count==1 :
                 return False
             count +=1
          else:
              i += 1
              j += 1

        if i<m or j<n:
            count += 1
        return count == 1


obj=checkedit()
res=obj.oneaway('gfg','gf')
print("result1 is : ", res)
res=obj.oneaway('geeks','geek')
print("result2 is : ", res)
res=obj.oneaway('geeks','geeks')
print("result3 is : ", res)
res=obj.oneaway('peaks','geeks')
print("result4 is : ", res)