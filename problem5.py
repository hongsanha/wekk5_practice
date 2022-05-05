h=int(input("나무 막대의 높이 h를 입력해주세요: "))
x=int(input("낮 동안 올라가는 높이 x를 입력해주세요: "))
y=int(input("밤 동안 미끄러지는 높이 y를 입력해주세요: "))
day=0
#하루 올라가는 높이는 x-y, 예를 들어 3이면 15의 높이면 5일, 16의 높이면 6일 걸린다.
if h%(x-y)>0:
    day=(h//(x-y))
else:
    day=h//(x-y)-1
print(day)