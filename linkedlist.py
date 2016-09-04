'''
@Description:   Simple Singly Linked List implementation in python
@Author:        Albert Mundu, Bhumil Sarvaiya
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

    def clean(self):
        self.head=None

    def refined_delete(self):
        if(self.head==None):
            pass
        elif(self.head.next_node==None):
            self.head=None
        else:
            self.head=self.head.next_node

    def display(self):
        tmp=self.head
        while tmp!=None:
            print tmp.data,
            tmp=tmp.next_node
        print ""

    def get_first_element(self):
        tmp=self.head
        return tmp.data

    def get_first_element_refined(self):
        if(self.head==None):
            return -1
        tmp=self.head
        return tmp.data

    def get_last_element(self):
        tmp=self.head
        while tmp!=None:
            data=tmp.data
            tmp=tmp.next_node
        return data

    def find_min(self,x):
        minimum=10000
        tmpy=self.head
        tmpx=x.head
        while tmpy!=None:
            if(tmpy.data<minimum):
                minimum=tmpy.data
                x=tmpx.data
            tmpy=tmpy.next_node
            tmpx=tmpx.next_node
        return (minimum,x)

    def find_max(self,x):
        maximum=0
        tmpy=self.head
        tmpx=x.head
        while tmpy!=None:
            if(tmpy.data>maximum):
                maximum=tmpy.data
                x=tmpx.data
            tmpy=tmpy.next_node
            tmpx=tmpx.next_node
        return (maximum,x)

    def find_mid(self,x,window_size):
        tmpx=x.head
        tmpy=self.head
        for i in range(int(window_size/2)):
            y_value=tmpy.data
            x_value=tmpx.data
            tmpy=tmpy.next_node
            tmpx=tmpx.next_node
        return (y_value,x_value)

    def find_mid_refined(self,x,window_size):
        tmpx=x.head
        tmpy=self.head
        first=tmpx.data
        for i in range(int(window_size/2)):
            y_value=tmpy.data
            x_value=tmpx.data
            if((x_value-first)>int(window_size/2)):
                return (previous_y,previous_x)
            previous_x=x_value
            previous_y=y_value
            if(tmpx.next_node==None):
                return (previous_y,previous_x)
            tmpy=tmpy.next_node
            tmpx=tmpx.next_node
        return (y_value,x_value)
