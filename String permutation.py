class palindrome_check:

#using hashmap; set , requires memory but
 def palindrome(self, str1, str2):
    hash1 = set()
    hash2= set()
    for ch in str1:
        if ch not in hash1:
           hash1.add(ch)
    for ch in str2:
        if ch not in hash2:
           hash2.add(ch)
    if hash1!=hash2:
        return False
    else:
        return True

# using sorting and then comparing: O(nlogn)
 def palindrome_sort(self, str1, str2):
     if len(str1)!=len(str2):
         return False
     s1 = sorted(str1)
     s2 = sorted(str2)

     if s1!=s2:
         return False
     else:
         return True

obj = palindrome_check()

res1 = obj.palindrome('sfttrrm', 'mrrttfs')
print("res1", res1)

res2 = obj.palindrome_sort('sfttrrm', 'mrrttfs')
print("res2", res2)


