class urlify_str:

 #uses new datastructure list: as the string is immutable so uses list
 #time complexity: O(n)
 #space complexity O(n)

 def urlify_with_list(self, str):
    list1=[]
    str_wo_space= str.strip()
    for i in str_wo_space:
         if i==' ':
             list1.append('%')
             list1.append('2')
             list1.append('0')
         else:
             list1.append(i)
    return ''.join(list1)

#In place string urlify: using string as a list, as string is immutable. we need to convert string to list when we are changing string
 def urlify_inplace(self, str, origstrlen):
     newindex=len(str)
     for i in reversed(range(origstrlen)):
         if str[i] == ' ':
             str[newindex-1] = '0'
             str[newindex - 2] = '2'
             str[newindex - 3] = '%'
             newindex -= 3

         else:
             str[newindex-1]= str[i]
             newindex -=1

     return str



obj= urlify_str()

res=obj.urlify_with_list('Mr John Smith    ')
print("res1", res)

res=obj.urlify_inplace(list('Mr John Smith    '), 13)

print("res2", res)
