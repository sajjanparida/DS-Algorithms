#program to delete 

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
    

class LinkedList:

    def __init__(self):
        self.head = None

    def deleteNode(self,key):
        temp=self.head
        if temp is None:
            return
        if temp.data==key:
            self.head=temp.next
            del temp
            return

        while(temp!=None and temp.data!=key):
            prev=temp
            temp=temp.next
        prev.next=temp.next
        del temp

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
fourth=Node(4)

llist.head = first
first.next=second
second.next=third
third.next=fourth
llist.printList()
llist.deleteNode(1)
llist.printList()
