def ispar(x):
    # code here
    stack = []
    par_hash = {"(": ")", "{": "}", "[": "]"}
    is_bal = True
    for char in x:
        if char in par_hash.keys():
            stack.append(char)
        elif char in par_hash.values():
            popped = stack.pop()
            if par_hash[popped] != char:
                is_bal = False
                break
        else:
            is_bal = False
    if len(stack) != 0:
        is_bal = False
    return is_bal

if __name__ == "__main__":
    print(ispar("[()]{}{[()()]()}"))
    print(ispar("[(])"))