#display odd numbers between 0 to 100
x = int(input("Enter a value :"))
if x %2 !=0:
    print("The number is odd", end='\t')
else:
    print("The number is even",end='\t')