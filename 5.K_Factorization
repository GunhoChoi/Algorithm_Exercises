# python3
# can divide with the same number again & again

n,k = input().strip().split(' ')
n = int(n)
k = int(k)
ar = list(map(int, input().strip().split(' ')))

ar.sort(reverse=True)
result_list=[n]

i=0
while i < k:
    if n % ar[i] == 0:
        result_list.append(int(n/ar[i]))
        if n/ar[i]==1:
            break
        else:
            n = n/ar[i]
    else:
        i+=1
        
result_list.sort()
if result_list[0] is not 1:
    print(-1)
else:
    print(*result_list)
