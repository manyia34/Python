data = [10,20,30,40,50,60,70,80,90,100]
value = int(input("Enter the value to search:"))

# Linear search
found = False
for index in range(len(data)):
    if data[index] == value:
        print("Value found at index", index)
        found = True
        break

if not found:
    print("Value not found in the list")


# Binary search
low = 0
high = len(data) - 1

while low <= high:
    mid = (low + high) // 2

    if data[mid] == value:
        print("Value found at index", mid)
        break

    elif data[mid] < value:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Value not found in the list")
    
