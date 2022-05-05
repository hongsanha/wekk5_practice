num_list=[]
while True:
    n=int(input("Enter a number: "))
    if n<0:
        break
    else:
        num_list.append(n)
print(f"The largest number entered was {max(num_list)}")