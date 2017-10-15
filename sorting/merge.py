arr = [2,5,1,9,7,8,4,3,6]

def mergesort(arr):
	if len(arr)>1:
		a,b = divide(arr)
		a = mergesort(a)
		b = mergesort(b)
		arr = merge(a,b)
		return arr
	else:
		return arr

def divide(arr):
	idx=len(arr)//2
	return arr[:idx],arr[idx:]

def merge(a,b):
	i,j=0,0
	new_arr=[]
	while i<len(a) and j<len(b):
		if a[i]<b[j]:
			new_arr.append(a[i])
			i+=1
			if i==len(a):
				new_arr= new_arr + b[j:]
				return new_arr
		else:
			new_arr.append(b[j])
			j+=1
			if j == len(b):
				new_arr=new_arr+a[i:]
				return new_arr

print(mergesort(arr))