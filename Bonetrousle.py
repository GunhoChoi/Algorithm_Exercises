# https://www.hackerrank.com/challenges/bonetrousle
import random
t=input()

input_array=[]

for i in range(t):
	s=raw_input()
	a=s.split()
	input_array.append(map(int,a))

def func(result,lack,k):
	for i in range(lack,0,-1):
		for j in range(b-1,0,-1):
			if i+result[j]<=k and i+result[j] not in result:
				result[j]+=i
				new_lack=lack-i 
				return result,new_lack
	
	if not new_lack:
		result=[-1]
		return result,lack

for x in input_array:

	n=x[0]
	k=x[1]
	b=x[2]
	result=[]
	
	if n > b*(2*k-b+1)/2:
		result.append(-1)
		print ' '.join(map(str,result))
		continue
	
	if n < b*(b+1)/2:
		result.append(-1)
		print ' '.join(map(str,result))
		continue

	for i in range(b):
		result.append(i+1)

	lack=n-sum(result)

	if lack/b>=1:
		for i in range(b):
			result[i]=result[i]+lack/b
	
	lack=n-sum(result)
	#print lack

	while lack and result != [-1]:
		result, lack=func(result,lack,k)

	
	if sum(result) == n:
		print ' '.join(map(str,result))
		continue

	else:
		result=[-1]

	print ' '.join(map(str,result))


