class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def deleteList(self):
        curr= self.head

        if curr==None:
            return

        while curr!=None:
            prev=curr.next
            del curr.data
            curr.next=None
            curr=prev

    def printList(self):
        temp=self.head

        if temp.next  ==None:
            print('Empty List')
            return

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
llist.deleteList()
llist.printList()



