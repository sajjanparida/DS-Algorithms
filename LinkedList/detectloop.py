class Node:
    
    def __init__(self,data):
        self.data=data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head=None


    def printlist(self,node):
        curr = node
        while(curr.next != None):
            print(str(curr.data) + "->",end='')
            curr = curr.next
        print(str(curr.data))

    def detectloop(self,node):
        lcurr = fcurr=node

        while(fcurr!=None and fcurr.next!=None):
            prev=lcurr
            lcurr= lcurr.next
            fcurr = fcurr.next.next

            if lcurr == fcurr:
                return True
        
        return False

    def removeloop(self,node):
        lcurr = fcurr=node
        loopexist=0
        while(fcurr!=None and fcurr.next!=None):
            prev=lcurr
            lcurr= lcurr.next
            fcurr = fcurr.next.next

            if lcurr == fcurr:
                loopexist=1
                lcurr=node
                break

        while loopexist==1:

            if fcurr==lcurr:
                loopexit=0
                prev.next=None
                return

            prev=fcurr
            fcurr = fcurr.next
            lcurr = lcurr.next
            
            
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
fifth.next = first
# sixth.next= seventh
# seventh.next = eigth
# eigth.next=first

if llist.detectloop(llist.head):
    print('Loop Exist')
else:
    print('loop free linkedlist')
    llist.printlist(llist.head)

llist.removeloop(llist.head)

if llist.detectloop(llist.head):
    print('Loop Exist')
else:
    print('loop free linkedlist')
    llist.printlist(llist.head)
