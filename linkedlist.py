'''
@Description:   Simple Singly Linked List implementation in python
@Author:        Albert Mundu
'''

class Node(object):
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next_node=next_node

class LinkedList(object):
    def __init__(self,head=None,prev=None):
        self.head=head
        self.prev=None

    def insert(self,data):
        if(self.head==None):
            new_node=Node(data)
            new_node.next_node=None
            self.head=new_node
            self.prev=new_node
        else:
            new_node=Node(data)
            new_node.next_node=None
            self.prev.next_node=new_node
            self.prev=new_node

    def delete(self):
        self.head=self.head.next_node

    def display(self):
        tmp=self.head
        while tmp!=None:
            print tmp.data,
            tmp=tmp.next_node
        print ""
        
        
