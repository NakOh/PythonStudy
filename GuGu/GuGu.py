def GuGu(n):
    result=[]
    i=1
    while i < 10:
        result.append(n*i)
        i=i+1
    return result

n = input("원하는 구구단을 입력해주세용")
print(GuGu(int(n)))