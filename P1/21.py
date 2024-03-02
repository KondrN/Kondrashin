x = [1, 3, 4, 7, 8, 9, 10]
razn=0
for i in range(0,len(x)-1):
    if(x[i+1]-x[i]>razn):
        razn = x[i+1]-x[i]
print(razn/0.01)