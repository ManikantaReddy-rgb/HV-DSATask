def rotate_array(arr, n):
  n = n % len(arr)
  return arr[-n:] + arr[:-n]

array = [3,1,2,5,7]
n = int(input("Enter the N value: "))
print(rotate_array(array, n))
