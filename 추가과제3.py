cnt_a=0
cnt_name=0
while True:
    name=input("Enter a name (q to quit): ")
    if name=="q":
        break
    else:
        name_list=name.split()
        for i in name_list:
            cnt_a+=i.count("a")
            cnt_name+=1
print(f"Number of names and letter 'a': {cnt_name}, {cnt_a}")