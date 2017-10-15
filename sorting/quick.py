arr = [7,2,2,1,8,1,6,8,5,3,2,5,5,7,2,4]

def partition(arr,start,end):
	pivot = arr[end]
	pIndex = start
	for i in range(start,end):
		if arr[i] < pivot:
			arr[pIndex],arr[i] = arr[i],arr[pIndex]
			pIndex += 1
	arr[pIndex],arr[end] = arr[end],arr[pIndex]

	return pIndex

def quicksort(arr,start,end):
	if start <= end:
		pIndex = partition(arr,start,end)
		quicksort(arr,start,pIndex-1)
		quicksort(arr,pIndex+1,end)

quicksort(arr,0,len(arr)-1)

print(arr)