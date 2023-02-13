def highest_frequency(arr):
  
    frequency_dict = {}
    
    for num in arr:
        
        if num not in frequency_dict:
            frequency_dict[num] = 1
        
        else:
            frequency_dict[num] += 1
   
    max_frequency = max(frequency_dict.values())
    for key, value in frequency_dict.items():
        if value == max_frequency:
            return key

arr = [1, 2, 4, 3, 2, 4, 2, 5, 7, 2]
print(highest_frequency(arr)) 
