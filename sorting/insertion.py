list_1 = [3,1,0,0,0,1,1,3,3]

for i in range(1,len(list_1)):
	for j in range(i-1,-1,-1):
		# if 1st one doesn't swap, there's no need to check the rest
		if list_1[j+1]>=list_1[j] and j==i-1: 
			break
		# if j is bigger, swap
		elif list_1[j+1]<list_1[j]:
			list_1[j+1],list_1[j]=list_1[j],list_1[j+1]
	
print(list_1)