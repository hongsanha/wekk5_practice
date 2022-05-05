def mysum():
    n=int(input("Enter an natural number: "))
    sum=0
    for i in range(n):
        sum+=(i+1)
    print(sum)

mysum()