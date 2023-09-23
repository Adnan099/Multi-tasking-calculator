i=int(input("enter your number"))

j = 2
while(j <= (i/j)):
    if (i%j==0): break
    j = j + 1
if (j > i/j) :
    print( i, " is prime")
else:
    print(i," is composite")


