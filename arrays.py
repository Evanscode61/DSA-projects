# finding minimum value in an array and implemenent O(n)
numbers=[67,56,90,60,88]
minValue = numbers[0]

for i in numbers:
    # If current number is smaller, update minValue
    if i < minValue:
        minVal = i

print('lowest value in array:', minValue)

