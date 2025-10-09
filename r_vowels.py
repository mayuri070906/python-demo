s="Education"
vowels="AEIOUaeiou"
new_s=""
for i in s:
    if i in vowels:
        new_s=new_s+"*"
    else:
        new_s=new_s+i
print(new_s)
        