num=int(input("enter th number"))
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print("perfect number")
else:
    print("not perfect")