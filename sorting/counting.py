arr = [0,1,4,2,3,4,1]

def countingsort(arr):
	counting_arr_len = max(arr)-min(arr)+1
	counting_arr = [0]*counting_arr_len

	for i in range(len(arr)):
		counting_arr[arr[i]]+=1

	result = []
	for j in range(counting_arr_len):
		current = min(arr)+j
		num = counting_arr[j]
		result += [current]*num

	return result

print(countingsort(arr))