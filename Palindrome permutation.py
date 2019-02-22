
class palindrome_check:

#using hashmap; set , requires memory but.
# explanation: no of counts of all letters should be same except one

 def palindrome(self, str1):

    hash1 = set()
    for ch in str1.replace(" ", "").lower():
        if ch not in hash1:
           hash1.add(ch)
        else:
           hash1.remove(ch)

    return len(hash1) <= 1


obj = palindrome_check()

res1 = obj.palindrome('tactcoa')
print("res1", res1)
res1 = obj.palindrome('tact coa')
print("res1", res1)
res1 = obj.palindrome('Tact Coa')
print("res1", res1)