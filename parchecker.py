for _ in range(t):
    stack = []
    string = input()
    stack.append(string[0])
    for i in range(1, len(string)):
        if len(stack) != 0:
            peek = stack[len(stack) - 1]
            if peek == '(' and string[i] == ')':
                stack.pop()
            elif peek == '{' and string[i] == '}':
                stack.pop()
            elif peek == '[' and string[i] == ']':
                stack.pop()
            else:
                stack.append(string[i])
        else:
            stack.append(string[i])
    if len(stack) > 0:
        print("not balanced")
    else:
        print("balanced")