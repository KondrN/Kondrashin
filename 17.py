pol = input()
one_sumb = ord(pol[0])
two_sumb = int(pol[1])
if(one_sumb%2==0):
    one=1
else:
    one=0
if(two_sumb%2==0):
    two=1
else:
    two=0
if(one+two == 2):
    print("black")
if (one + two == 1):
    print("white")
if(one+two == 0):
    print("black")