def max_frequency(arr, start, end, max_element, max_count):
  if start == end:
    return max_element
  
  current_element = arr[start]
  current_count = 1
  
  for i in range(start + 1, end):
    if arr[i] == current_element:
      current_count += 1
  
  if current_count > max_count:
    max_count = current_count
    max_element = current_element
  
  return max_frequency(arr, start + 1, end, max_element, max_count)

def main():
  arr = [1,2,4,3,2,4,2,5,7,2]
  result = max_frequency(arr, 0, len(arr), arr[0], 0)
  print("Element with highest frequency: ", result)

if __name__ == "__main__":
  main()
