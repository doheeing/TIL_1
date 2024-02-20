class JSS :
    def __init__(self) :
        self.name = input ("이름 :")
        self.age = input ("나이 :")
    def show(self) :
        print("나의 이름은 {}, 나이는{}". format(self.name, self.age))
        
#class 를 쓰고 상속받을 함수를 괄호안에 쓰기
class JSS2(JSS) :
    #아예 똑같이 만들기
    pass

class JSS3(JSS):
    #class 를 상속 받은 후에 새로 init 함수를 정의하면 이전 내용 위로 덮어쓰게 됨
    #그래서 이렇게 쓰면 init 함수가 아무것도 없게 됨
    def __init__(self) :
        pass
    

class JSS4(JSS) :
    #super()는 JSS를 의미함. 그래서 이렇게 쓰면 JSS함수의 init에 더해지는 걸 아래 쓰면 됨
    def __init__(self):
        super().__init__()
        self.gender = input("성별 :")
    #밑에 함수는 자동으로 포함되어 있어 따로 작성 안해도 되긴 함
    def show(self) :
        print("나의 이름은 {}, 나이는{}, 성별은{}입니다". format(self.name, self.age, self.gender))
        
a = JSS4()
a.show()