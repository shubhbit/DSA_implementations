class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(f"pushed {value} to stack")

    def pop(self):
        popped_elem = self.stack.pop()
        print(f"popped out {popped_elem}")
        return popped_elem

    def __str__(self):
        return str(self.stack)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(150)
    stack.push(87)
    stack.push(12)
    stack.push(90)
    print (stack)
    stack.pop()
    print (stack)



