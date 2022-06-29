
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.min = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def __str__(self):
           
        # defining a blank res variable
        res = ""
         
        # initializing ptr to head
        ptr = self.head
         
       # traversing and adding it to res
        while ptr:
            res += str(ptr.data) + ", "
            ptr = ptr.next
 
       # removing trailing commas
        res = res.strip(", ")
         
        # chen checking if
        # anything is present in res or not
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"