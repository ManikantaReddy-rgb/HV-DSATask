def print_duplicates(arr):
  result = []
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] == arr[j]:
        result.append(arr[i])
        break
  return result

array = [1,1,2,3,3,4,5,6,6]
print(print_duplicates(array))
