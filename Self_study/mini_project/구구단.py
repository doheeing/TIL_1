
#사용자로부터 원하는 수를 입력받음
number =input("숫자 : ")

#입력받은 a를 정수형으로 변경 하고 만약 숫자가 아니라면(정수형으로 변경이 안되면) 코드 종료
try :
    a = int(number)
except :
    print("다시 입력하세요")
    quit()
    
#i를 1부터 10까지(마지막은 포함 안 됨) 대입하며 출력
for i in range(1,11) :
        print (f"{number}X{i}= {a*i}")
        i += 1