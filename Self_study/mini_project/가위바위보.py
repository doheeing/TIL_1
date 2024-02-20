
#random 라이브러리 사용
import random 

#select 리스트
select = ["가위", "바위", "보"]
#c_choice 는 random 라이브러리 내 choice 함수를 사용해서 랜덤하게 select 리스트 안의 값을 가져오도록 함
c_choice = random.choice(select)

#mychoice 라는 변수에 select 리스트에 없는 값을 넣으면 다시 입력하도록 하는 무한루프함수 생성
#만약 select 리스트 안의 값을 넣으면 break 로 무한루프 탈출
while True :
    mychoice = input("입력 : ")
    if mychoice in select :
        break
    print("다시입력하세요")
    
#print (f) 를 사용해 format 후 {} 안에 있는 변수를 보여줘 사용자와 컴퓨터의 입력값 출력해주기
print (f"당신은 {mychoice}를 냈습니다")
print (f"컴퓨터는 {c_choice}를 냈습니다")

#세 가지 경우에는 사용자가 이겼음을 출력
if mychoice == "가위" and c_choice == "보" or mychoice == "바위" and c_choice == "가위" or mychoice == "보" and c_choice == "바위" :
    print ("당신이 이겼습니다")
#만약 값이 같다면 비겼음을 출력
elif mychoice == c_choice :
    print ("비겼습니다")
#그 외의 경우는 컴퓨터의 랜덤값이 졌을 경우니까 졌다는 결과를 출력
else :
    print ("당신이 졌습니다")

