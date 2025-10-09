n=int(input("enter="))
for i in range(n):
    a=str(i+1)
    b=a.zfill(3)
    c=b.rjust(4,"D")
    print(c.rjust(5,"I"))

