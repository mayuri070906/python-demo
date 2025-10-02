a, b, c=map(int, input("enter a number::").split())
if(a>b and a>c):
    print(f"{a} is greater then {b} & {c}")
elif(b>a and b>c):
    print(f"{b} is greater then {a} & {c}")
else:
    print(f"{c} is greater then {a} & {b}")