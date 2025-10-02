
num=int(input("enter any number:"))
if num==1:
    print(f"{num} not a prime number")
else:
    for i in range(2,int(num**(1/2))+1):
        if num%i==0:
            print(f"{num} is not prime number")
            break
    else:
        print(f"{num} is a prime number")
        