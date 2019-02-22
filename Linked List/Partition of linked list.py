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


      def partition(self, head, pivot):
          dummy_tail = Node(0)
          tail = dummy_tail
          current = head
          dummy_front = Node(0)
          front = dummy_front

          while current:
              if current.data < pivot:
                  front.next= Node(current.data)
                  front=front.next

              else:
                  tail.next=Node(current.data)
                  tail=tail.next

              current = current.next

          front.next = dummy_tail.next

          temp = dummy_front.next
          print("partioned List is ")
          while (temp):
              print(temp.data);
              temp = temp.next

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
res.partition(first.head, 5)






