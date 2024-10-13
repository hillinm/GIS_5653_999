erosionClass = [5, 3, 5, 7, 6, 9, 2, 1, 1, 2]  
erosionClass.sort()  # Sort the numeric list 

for i in range((len(erosionClass))):
    if i == 0:
        print("Lowest value: ", erosionClass[i])
    if i == len(erosionClass) - 1:
        print("Highest value: ", erosionClass[i])

erosionClass.append(2)
print(erosionClass)

print(erosionClass.count(5))

erosionClass.insert(2, 8)
print(erosionClass)

erosionClass.extend([2, 3, 4])
print(erosionClass)

erosionClass.remove(4)
print(erosionClass)

print(erosionClass.index(2))

print(erosionClass.pop(8))

erosionClass.sort()
print(erosionClass)

erosionClass.reverse()
print(erosionClass)