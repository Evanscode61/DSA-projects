# implementation  of stack using list
class stack:
    def __init__(self):
        # Initialize an empty list to store stack items
        self.items =[]
    #checking if the stack has no value at all
    def isEmpty(self):
        return len.items == 0
    #check the lenght of the stack
    def size(self):
        return len(self.items)
    #remove and return the top item of the stack
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.items.pop()
    #remove items of the stack
    def clear(self):
         self.items.clear()





