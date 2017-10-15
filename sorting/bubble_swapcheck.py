a = [5,1,4,2,8]

for i in range(len(a)-1,0,-1):
	swap = 0
	for j in range(i):
		if a[j] > a[j+1]:
			a[j],a[j+1] = a[j+1],a[j]
			swap+=1
	if swap==0:
		print(i,"No swap, Done")
		break

print(a)