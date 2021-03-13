from stack_ds import Stack

def infix_to_postfix(infix_expression):
    op_precedence = {"+": 1, "-":1, "*": 2, "/":2}
    stack = Stack()
    postfix_exp = ""
    for char in infix_expression:
        if char not in op_precedence.keys():
            postfix_exp += char
        else:
            if stack.stack:
                temp = stack.stack[-1]
                if op_precedence[char] > op_precedence[temp]:
                    stack.push(char)
                else:
                    while stack.stack:
                        popped = stack.pop()
                        postfix_exp += popped
                    stack.push(char)
            elif not stack.stack:
                stack.push(char)
    if stack.stack:
        popped = stack.pop()
        postfix_exp += popped
    return postfix_exp

if __name__ == "__main__":
    infix_expression = "a+b*c+d"
    print(f"Infix expression {infix_expression}")
    print(f"calling infix to postfix method")
    postfix_exp = infix_to_postfix(infix_expression)
    print(f"converted to postfix: {postfix_exp}")

