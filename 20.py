x=float(input())
sum=0
for i in range(1,999):
    sum=sum+(-1)**(i+1)*(x**i)/i
print(round(sum,8))