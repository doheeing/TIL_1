class person :
    def __init__(self):
        self.name = input("이름 :")
        self.age = input("나이 :")
        self.gender = input("성별 :")
    def introduce(self) :
        print ("이름은 %s 입니다" %self.name)
        print ("나이는 %s입니다" %self.age)
        print ("성별은 %s 입니다" %self.gender)
        
a = person()
a.introduce()
        