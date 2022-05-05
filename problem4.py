lst=[]
while True:
    num=(input("숫자를 입력해주세요: "))
    if num=="q":
        break
    else:
        num=int(num)
        lst.append(num)

print(f"{len(lst)}개의 숫자 중 최솟값은 {lst.index(min(lst))+1}번째 수 {min(lst)}입니다.")
print(f"{len(lst)}개의 숫자 중 최댓값은 {lst.index(max(lst))+1}번째 수 {max(lst)}입니다.")