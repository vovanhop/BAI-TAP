n=int(input("Nhập n="))
flag=True
x=2
while x <= int(n/2):
    if n%x==0:
        flag=False
        break
    x +=1
if flag==True:
    print(n, "là số nguyên tố!")
else:
    print(n, "không là số nguyên tố")