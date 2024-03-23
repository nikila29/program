class node:
    def __init__ (self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__ (self):
        self.head=None
    def createll(self,n):
        i=0
        while i<n:
            newnode=node(input("enter val of node:"))
            if i==0:
                self.head=newnode
            else:
                t=self.head
                while t.next:
                    t=t.next
                t.next=newnode
            i=i+1
    def show(self):
        t=self.head
        while t:
            print(t.val,end="->")
            t=t.next
    def reverse(self):
        t=self.head
        prev=None
        while self.head:
            cur=self.head
            self.head=self.head.next
            cur.next=prev
            prev=cur
        self.head=prev
obj=LinkedList()
obj.createll(5)
print("\n original list:")
obj.show()
obj.reverse()
print("\n reverse list:")
obj.show()
        
