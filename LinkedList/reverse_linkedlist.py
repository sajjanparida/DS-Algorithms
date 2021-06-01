

class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def printlist(self):
        curr = self.head
        while(curr.next != None):
            print(str(curr.data) + "->",end='')
            curr = curr.next
        print(str(curr.data))

    def reverseList(self):
        curr=self.head
        prev=None
        
        while(curr!=None):
            temp  = curr.next  
            curr.next=prev

            prev = curr
            curr = curr.next

        self.head = prev

    def recursivelist(self,prev,curr):
        
        if curr.next == None:
            self.head = curr
            curr.next=prev
            return
        self.recursivelist(curr,curr.next)
        curr.next = prev

    def recReverseList(self):
        
        if self.head==None:
            return
        self.recursivelist(None,self.head)

llist = LinkedList()

llist.head = Node(1)
first=llist.head
second= Node(2)
third = Node(3)
fourth = Node(4)

first.next = second
second.next = third
third.next = fourth

llist.printlist()
llist.reverseList()
llist.printlist()
llist.recReverseList()
llist.printlist()
