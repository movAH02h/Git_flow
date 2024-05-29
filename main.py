import add_sub_mult_div

print("Введите действие:")
action = input()

if action == "add":
    print("Введите первое число:")
    a = int(input())
    print("Введите второе число:")
    b = int(input())
    print("a + b = " + add_sub_mult_div.add(a, b))
elif action == "subtraction":
    print("Введите первое число:")
    a = int(input())
    print("Введите второе число:")
    b = int(input())
    print("a - b = " + add_sub_mult_div.subtraction(a, b))
elif action == "mulptiply":
    print("Введите первое число:")
    a = int(input())
    print("Введите второе число:")
    b = int(input())
    print("a * b = " + add_sub_mult_div.multiple(a, b))
elif action == "division":
    print("Введите первое число:")
    a = int(input())
    print("Введите второе число:")
    b = int(input())
    print("a // b = " + add_sub_mult_div.div(a, b))
elif action == "log2":
    print("Введите число:")
    a = int(input())
    print("log2(a) = ", add_sub_mult_div.logariphm_two(a))
elif action == "logE":
    print("Введите число:")
    a = int(input())
    print("log2(a) = ", add_sub_mult_div.logariphm_natural(a))

