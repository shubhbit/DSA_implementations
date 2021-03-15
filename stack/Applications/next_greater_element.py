def nextLargerElement(arr):
    # code here
    out = {}
    stack = [arr[0]]
    for i in arr:
        print(f"elem: {i}")
        while stack and stack[-1] < i:
            popped = stack.pop()
            out[popped] = i
        if not stack or stack[-1] > i:
            stack.append(i)
    for val in stack:
        out.update({val: "-1"})
    return [out[i] for i in arr]

print(nextLargerElement([1,3,2,4]))
print(nextLargerElement([5,4,3,2,1]))
print(nextLargerElement([12,87,26,4544]))
print(nextLargerElement([1,2,3,4,5,6,7]))
print(nextLargerElement([7,8,1,4]))