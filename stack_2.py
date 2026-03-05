stack = []
poped = []


n = 10

for i in range(n):
    inp = input("Stack in :")
    stack.append(inp)

print("Stack now :", stack)

for i in range(n):
    x = stack.pop()
    poped.append(x)
    print("popped :",x)



print("popped now :", poped)




