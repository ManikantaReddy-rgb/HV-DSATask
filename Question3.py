def highest_frequency(arr):
  frequency = {}
  for i in arr:
    if i in frequency:
      frequency[i] += 1
    else:
      frequency[i] = 1
  return max(frequency, key=frequency.get)

array = [1,2,4,3,2,4,2,5,7,2]
print(highest_frequency(array))
