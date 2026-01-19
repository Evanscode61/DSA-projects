#implementing stack using linked list
#Initialize an empty stack
class Node:
    def __init__(self,value):
        self.value = value
        self.next =None
class Stack:

    def __init__(self):
            self.top = None

    def push(self , value):
        self.top = Node(value)
        temp =Node(value)
        temp.next = self.top
    def peek(self,value):
        if self.top is None:
            print("Stack is empty")
            return -1
        else:
            return self.top.value

    def isEmpty(self,value):
        return self.top is None

    def pop(self,value):
        if self.top is None:
            print("stack underflow")
            return -1

        temp = self.top
        self.top = self.top.next
        return temp.value
if __name__ == "__main__":
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    st.push(40)


    print("Popped:", st.pop())

    # checking top element
    print("Top element:", st.peek())

    # checking if stack is empty
    print("Is stack empty: ", "Yes" if st.isEmpty() else "No")

    # checking if stack is full
    print("Is stack full: ", "Yes" if st.isFull() else "No")
