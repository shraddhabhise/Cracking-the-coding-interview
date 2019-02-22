class rotate:

   def rotateString(self, A, B):
        if len(A) != len(B):
            return False
        else:
            return B in A+A


rot= rotate()
res= rot.rotateString('abcde','cdeab')
print("rotated string", res)

