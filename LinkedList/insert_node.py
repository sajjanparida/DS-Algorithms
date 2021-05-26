#program to insert node in a linkedlist



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtFront(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def append(self,data):
        temp=self.head
        while(temp.next):
            temp = temp.next
        temp.next=Node(data)

    def insertAfter(self,data,key):
        temp=self.head
        while(temp!= None and temp.data!=key):
            temp=temp.next
        newNode = Node(data)
        newNode.next  = temp.next
        temp.next=newNode

    def insertBefore(self,data,key):
        temp=self.head
        if temp.data == key:
            LinkedList.insertAtFront(data)
        else:
            while(temp.next!=None and temp.next.data!=key):
                temp=temp.next
            newNode = Node(data)
            newNode.next=temp.next
            temp.next=newNode

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
        print()
llist = LinkedList()

first=Node(1)
second=Node(2)
third=Node(3)

llist.head = first
first.next=second
second.next=third

llist.printList()
llist.insertAtFront(0)
llist.printList()
llist.append(4)
llist.printList()
llist.insertAfter(10,2)
llist.printList()
llist.insertBefore(20,2)
llist.printList()