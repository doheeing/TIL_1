
d, e, f = input(" ").split()

a = int(d)
b = int(f)

#곱하기 가 아닌 연산을 곱하기로 인식하는 오류 있음. 해결(-)
if e == "+" :
    print (a+b)
elif e == "x" or "X":
    print (a*b)
elif e == "-" :
    print (a-b)
elif e == "/"or "%":
    if a/b == 0 :
        print (a%b)
    else :
        print (f"몫:{a%b}, 나머지{a/b: 0.1f}")