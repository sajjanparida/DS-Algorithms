#write a recursive method to delete the node


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
        print()


    def deleteNode(self,head,key):
        
        curr=head
    
        if curr==None:
            return 

        if  curr.data==key:
            temp = curr
            curr=curr.next
            del temp
            return
            
        self.deleteNode(curr.next,key)

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
llist.deleteNode(llist.head,3)
llist.printList()
