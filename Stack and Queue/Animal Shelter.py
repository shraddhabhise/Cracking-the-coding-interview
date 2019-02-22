class Animal:
    def __init__(self):
        self.arrival=None
        self.type=None
class queue:
    def __init__(self):
        self.queue_cat=[]
        self.queue_dog = []

    def enque(self, x):
        if x.type == 'dog':
            self.queue_dog.append(x)
        if x.type == 'cat':
            self.queue_cat.append(x)


    def deque(self, type):

        if type == 'dog':
            if self.queue_dog:
                self.queue_dog=sorted(self.queue_dog, key=lambda Animal: Animal.arrival)
                for i in self.queue_dog:
                    print("sorted dog queue is", i.type, i.arrival)
                x = self.queue_dog.pop(0)
                return x
            else:
                return None
        if type == 'cat':
            if self.queue_cat:
                self.queue_cat=sorted(self.queue_cat,  key=lambda Animal: Animal.arrival)
                for i in self.queue_cat:
                    print("sorted cat queue is", i.type, i.arrival)
                x = self.queue_cat.pop(0)
                return x
            else: return None

        if type == 'any':
           if  self.queue_cat and self.queue_dog:
             self.queue_cat= sorted(self.queue_cat,  key=lambda Animal: Animal.arrival)
             self.queue_dog= sorted(self.queue_dog,  key=lambda Animal: Animal.arrival)
             if self.queue_cat[0].arrival > self.queue_dog[0].arrival:
                x = self.queue_cat.pop(0)
                return x
             else:
               x=self.queue_dog.pop(0)
               return x
           elif self.queue_cat and not self.queue_dog:
               self.queue_cat = sorted(self.queue_cat, key=lambda Animal: Animal.arrival)
               for i in self.queue_cat:
                   print("sorted cat queue is", i.type, i.arrival)
               x = self.queue_cat.pop(0)
               return x
           elif  not self.queue_cat and self.queue_dog:
                self.queue_dog = sorted(self.queue_dog, key=lambda Animal: Animal.arrival)
                for i in self.queue_dog:
                    print("sorted dog queue is", i.type, i.arrival)
                x = self.queue_dog.pop(0)
                return x
           else:
               return None


obj= queue()
animal1= Animal()
animal1.arrival=1
animal1.type='dog'

animal2= Animal()
animal2.arrival=5
animal2.type ='cat'

animal3= Animal()
animal3.arrival=3
animal3.type='cat'

animal4= Animal()
animal4.arrival=8
animal4.type='dog'

animal5= Animal()
animal5.arrival=6
animal5.type='dog'


obj.enque(animal1)
obj.enque(animal2)
obj.enque(animal3)
obj.enque(animal4)
obj.enque(animal5)

for i in obj.queue_cat:
     print ("Cat queue is", i.type ,i.arrival )
for i in obj.queue_dog:
    print ("Dog queue is", i.type, i.arrival )

res1= obj.deque('dog')
res2=obj.deque('cat')
res3=obj.deque('any')

print ("popped element is:", res1.type, res1.arrival)
print ("popped element is:", res2.type, res2.arrival)
print ("popped element is:", res3.type, res3.arrival)

