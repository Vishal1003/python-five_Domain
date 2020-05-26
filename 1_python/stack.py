class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def fullStack(self):
        return self.items
    


def checkParenthesis(str):
    stack = Stack()
    pushChars , popChars = "<({[", ">)}]"

    for c in str :
        if c in pushChars:
            stack.push(c)
        
        elif c in popChars:
            if stack.isEmpty():
                return False
            else:
                top = stack.pop()
                bal_b = pushChars[popChars.index(c)]
                if top != bal_b:
                    return False
                else:
                    return True
        else:
            return False

    return not stack.isEmpty()



par = input("Enter the string to be checked: ")
print(checkParenthesis(par))