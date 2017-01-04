# hacker rank sherlock and anagram

n=input("")

input_strings=[]
for i in range(n):
	a=raw_input("")
	input_strings.append(a)

def anagram(string):
	sub=[]
	s_dict={}
	result=0
	l=len(string)
	for i in range(0,l+1):
		for j in range(i+1,l+1):
			a=''.join(sorted(string[i:j]))
			sub.append(a)
	#print(sub)
	for x in sub:
		if s_dict.get(x)==None:
			s_dict[x]=1
		else: 
			s_dict[x]+=1
	#print(s_dict)
	for x in s_dict.keys():
		a=s_dict.get(x)
		result+=a*(a-1)/2
	return result

for k in input_strings:
	print(anagram(k))
