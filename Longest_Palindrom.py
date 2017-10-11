def longest_palindrom(s):
    result=0
    length = len(s)
    for i in range(length+1):
        for j in range(i+1,length+1):
            substr=s[i:j]
            substr=substr[::-1]
            if substr in s:
                result= max(len(substr),result)
    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("토마토맛있어"))
