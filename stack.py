#!/usr/bin/env python3

class Stack():
    def __init__(self, main_list: list):
        self.main_list = main_list

    def push(self, obj):
        return self.main_list.insert(0, obj)
    
    def pop(self):
        return self.main_list.pop()
    
    def peek(self):
        return self.main_list[0]
    
    def isEmpty(self):
        if len(self.main_list) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.main_list)
    
    def __str__(self) -> str:
        return f"Stack: {self.main_list}, and Size of {self.size()}"


if __name__ == "__main__":
    stack = Stack([])

    stack.push("Hello")
    stack.push("World")

    print(stack)

    stack.peek()
    stack.pop()
    print(stack.isEmpty())
    print(stack)
    stack.push(1)
    print(stack.peek())
    print(stack)
    stack.pop()
    stack.pop()
    print(stack)
    print(stack.isEmpty())