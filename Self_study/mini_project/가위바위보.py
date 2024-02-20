
import random

select = ["가위", "바위", "보"]
c_choice = random.choice(select)

while True :
    mychoice = input("입력 : ")
    if mychoice in select :
        break
    print("다시입력하세요")
    
print (f"당신은 {mychoice}를 냈습니다")
print (f"컴퓨터는 {c_choice}를 냈습니다")

if mychoice == "가위" and c_choice == "보" or mychoice == "바위" and c_choice == "가위" or mychoice == "보" and c_choice == "바위" :
    print ("당신이 이겼습니다")
elif mychoice == c_choice :
    print ("비겼습니다")
else :
    print ("당신이 졌습니다")

