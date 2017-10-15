list_1 = [3,1,0,0,0,1,1,3,3]

for i in range(1,len(list_1)):
	curNum = list_1[i]
	for j in range(i-1,-1,-1):
		# if 1st one doesn't swap, there's no need to check the rest
		if list_1[j+1]>=list_1[j] and j==i-1:
			break
		elif curNum < list_1[j]:
			list_1[j+1]=list_1[j]
			if j==0:
				list_1[j]=curNum
		else:
			list_1[j+1]=curNum
			break

print(list_1)


'''
# swap only once
elif curNum < list_1[j]:
	list_1[j+1]=list_1[j]
	if j==0:
		list_1[j]=curNum
else:
	list_1[j+1]=curNum
	break
	'''