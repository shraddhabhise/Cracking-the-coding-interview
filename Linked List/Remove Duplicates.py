import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
      def __init__(self):
          self.head=None

      def push(self, new_data):
          new_node = Node(new_data)
          new_node.next = self.head
          self.head = new_node


      def mergesort(self, head):
          oldhead=head
          mid = self.middle(oldhead)
          mid_next = mid.next
          mid.next= None
          sys.setrecursionlimit(10000)
          left = self.mergesort(oldhead)
          right = self.mergesort(mid_next)
          merged = self.merge(left, right)
          return merged

      def merge(self, first, second):
          result = Node(None)
          if not first and second:
              return second
          if not second and first:
              return first
          if first.val < second.val :
              result = first
              result.next=  self.merge(first.next, second)
          else:
              result=second
              result.next = self.merge(first, second.next)

          print("merged List is ")
          temp=result
          while (temp):
              print(temp.data);
              temp = temp.next
          #return result


      def middle(self, head):
          fast=head
          slow=head
          while fast and fast.next :
              fast=fast.next.next
              slow=slow.next
          return slow

      def printList(self):
          temp = self.head
          while (temp):
              print (temp.data);
              temp = temp.next


first = LinkedList()

# Create first list
first.push(1)
first.push(2)
first.push(10)
first.push(5)
first.push(8)
first.push(5)
first.push(3)
print ("First List is ", first.printList())
res = LinkedList()
res.mergesort(first.head)






