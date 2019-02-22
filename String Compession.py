class compression:

  def str_compression(self, string):
      compressed=[]
      counter=0
      for i in range(len(string)):
           if i!=0 and string[i]!=string[i-1]:
               compressed.append(string[i-1]+str(counter))
               counter=0
           counter += 1
      compressed.append(string[-1]+str(counter))
      print (compressed)
      return compressed if len(compressed)<len(string) else string


obj= compression()


res=obj.str_compression('aabcccccaaa')
print("res1", res)

res=obj.str_compression('abcdef')

print("res2", res)
