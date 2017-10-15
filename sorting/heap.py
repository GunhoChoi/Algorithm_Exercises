arr = [4,10,3,5,1]

def swap(arr,i,j):
	arr[i],arr[j] = arr[j],arr[i]

def max_heapify(arr):
	check_len = (len(arr)-1)//2
	for i in range(check_len):
		if arr[i]<arr[2*i+1]:
			swap(arr,i,2*i+1)
		elif arr[i]<arr[2*i+2]:
			swap(arr,i,2*i+2)
		else:
			continue
	return arr

def maxheap_pop(arr):
	swap(arr,0,len(arr)-1)
	popped = arr.pop()
	return popped

def heapsort(arr):
	sorted_arr = []
	while len(arr)>0:
		arr = max_heapify(arr)
		sorted_arr.append(maxheap_pop(arr))
	return sorted_arr

print(heapsort(arr))