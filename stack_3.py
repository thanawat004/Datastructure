stack = []
pairs = {
    ')':'(',
    ']':'[',
    '}':'{'
}

opens = set(pairs.values())
expr = input("Enter expression with bracket: ")
valid = True

# ===== ตรวจสอบวงเล็บ =====
for ch in expr:
    if ch in opens:
        stack.append(ch)
        print("push :", ch, "stack =", stack)

    elif ch in pairs:
        if not stack:
            print("Error : Stack empty but found closing bracket", ch)
            valid = False
            break

        top = stack.pop()
        print("pop :", top, "for closing", ch, "stack =", stack)

        if top != pairs[ch]:
            print("Error: bracket not match ->", top, "vs", ch)
            valid = False
            break

# ===== ตรวจสอบ stack ค้าง =====
if valid:
    if stack:
        print("Error : still", stack)
        valid = False

# ===== แสดงผล =====
if valid:
    print("result : Valid")

    # ===== แปลง [] {} ให้ eval ใช้ได้ =====
    calc_expr = expr.replace('[','(').replace(']',')')
    calc_expr = calc_expr.replace('{','(').replace('}',')')

    try:
        answer = eval(calc_expr)
        print("Calculation Result =", answer)
    except:
        print("Cannot calculate this expression")

else:
    print("result : Invalid")