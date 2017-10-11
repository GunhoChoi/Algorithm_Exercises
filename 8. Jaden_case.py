def Jaden_Case(s):
    s=list(s.lower())
    for i in range(len(s)):
        if i==0 and s[i].isalpha():
            s[i]=s[i].upper()
        elif " " in s[i-1]:
            s[i]=s[i].upper()
    return "".join(s)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))

'''
이런 방법도 있었음

def Jaden_Case(s):
    return ' '.join([x[0].upper()+x[1:].lower() for x in s.split()])
    # return s.title()
'''
