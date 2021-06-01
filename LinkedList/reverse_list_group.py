

class Node:
    
    def __init__(self,data):
        self.data=data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head=None

    def reverseListGroup(self,node,k):
        curr = node
        prev = None
        count = 0 
        while curr!=None and count<k:
            temp = curr.next
            curr.next= prev

            prev= curr
            curr = temp
            count += 1

        if temp!=None:
            node.next=self.reverseListGroup(temp,k)

        return prev
    
    def reverse(self,k):

        self.head=self.reverseListGroup(self.head,k)
    
    def printlist(self,node):
        curr = node
        while(curr.next != None):
            print(str(curr.data) + "->",end='')
            curr = curr.next
        print(str(curr.data))

llist = LinkedList()


first = Node(1)
second = Node(2)
third = Node(2)
fourth= Node(4)
fifth = Node(5)
sixth = Node(6)
seventh = Node(7)
eigth = Node(8)

llist.head = first
first.next= second
second.next =third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next= seventh
seventh.next = eigth


llist.printlist(llist.head)
llist.reverse(4)
llist.printlist(llist.head)
