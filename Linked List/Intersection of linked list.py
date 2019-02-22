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

      def getcount(self, head1, head2 ):
          c1=self.count(head1);
          c2=self.count(head2);
          diff=abs(c1-c2)
          if c1>c2:
              res=self.intersection_LL(diff, head1, head2)
          else:
              res=self.intersection_LL(diff, head2, head1)
          return res
      def count(self, current):
          count=0
          while current:
              count +=1
              current=current.next
          return count

      def intersection_LL(self, diff, head1, head2):
          current_L1 = head1

          ptr2=head2
          while diff > 0:
              diff -= 1
              current_L1 = current_L1.next
          current_L2=head2
          while current_L1 and current_L2:
              current_L1 = current_L1.next
              current_L2 = current_L2.next
              if current_L1.data == current_L2.data:
                 return current_L1.data
          return None

      def printList(self):
          temp = self.head
          while (temp):
              print (temp.data);
              temp = temp.next


first = LinkedList()
second = LinkedList()

# Create first list
first.push(7)
first.push(5)
first.push(9)
first.push(4)
first.push(6)
print ("First List is ", first.printList())

# Create second list
second.push(7)
second.push(5)
second.push(9)
second.push(8)
second.push(1)

print (
"\nSecond List is ", second.printList())

# Add the two lists and see result
res = LinkedList()
val = res.getcount(first.head, second.head)
print
("\nintersection at list is ", val)
#res.printList()

#List.intersection_LL([1, 2, 3, 4, 7], [6, 5, 3, 4, 7])



