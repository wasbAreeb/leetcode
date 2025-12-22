
s = input()

values = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 
    'C': 100, 'D': 500, 'M': 1000
}

total = 0
n = len(s)

# 2. Loop through the string (except for the very last character)
for i in range(n - 1):  
    current_val = values[s[i]]
    next_val = values[s[i + 1]]
    
    # 3. Subtraction logic: if current is smaller than next, subtract it
    if current_val < next_val:
        total -= current_val
    else:
        total += current_val
        
# 4. Always add the last character's value
total += values[s[n - 1]]

print(total)