word=input("단어를 입력해주세요: ")
word_list=list(word)
cnt_a=0
cnt_e=0
cnt_i=0
cnt_o=0
cnt_u=0


for i in word_list:
    if i=="a":
        cnt_a+=1
    elif i=="e":
        cnt_e+=1
    elif i=="i":
        cnt_i=1
    elif i=="o":
        cnt_o+=1
    elif i=="u":
        cnt_u+=1

print(f"a는 {cnt_a}개 포함되어 있습니다.")
print(f"e는 {cnt_e}개 포함되어 있습니다.")
print(f"i는 {cnt_i}개 포함되어 있습니다.")
print(f"o는 {cnt_o}개 포함되어 있습니다.")
print(f"u는 {cnt_u}개 포함되어 있습니다.")
