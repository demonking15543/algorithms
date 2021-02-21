
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Stack:
    def __init__(self):
        self.head = None

    # Create a push(data) function which accepts data and return accepted value


    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        
            

        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        
        
   

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def display(self):
        current = self.head
        if current is None:
            print("Stack is empty")
            return None
        print("Node of stack is: ")
        while(current != None):
            print(current.data)
            current = current.next



stack = Stack()


while True:
    print('push <data>')
    print('pop')
    print('show')
    print('quit')

    get = input("What operation would you like to do...?").split()
    op = get[0].strip().lower()

    if op == "push":
       stack.push(get[1])
     
    elif op == "pop":
        popped = stack.pop()
        if popped is None:
            print("Sorry! stack is empty")
        else:
            print("Popped value " +popped)
    elif op =="display":
        stack.display()
    elif op == "quit":

        break
   



  






    