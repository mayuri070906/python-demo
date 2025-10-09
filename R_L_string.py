# name="Mayuri"
# print(name.ljust(15,"*"))

# print(name.rjust(15,"*"))

# n=int(input("enter="))
# for i in range(n):
#     name=input("enter name=")
#     marks=input("enter marks=")
# print(name.rjust(5),"|",marks.ljust(5))

n=int(input("enter="))
for i in range(n):
    a=str(i+1)
    b=a.zfill(3)
    print(b.rjust(4,"R"))
     


