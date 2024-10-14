universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

print(universities)

def enrollment_stats(list_of_universities):
    total_students = []
    total_tuition = []

    for i in list_of_universities:
        total_students.append(i[1])
        total_tuition.append(i[2])

    return total_students, total_tuition

def mean(values):
    return sum(values) / len(values)

def median(values):
    values.sort()

    if len(values) %2 == 1:
        center = int(len(values) / 2)
        return values[center]

    else:
        left_center = (len(values) - 1) // 2
        right_center = (len(values) + 1) // 2
        return mean([values[left_center], values[right_center]])
      
totals = enrollment_stats(universities)

print("\n")
print("*****" * 6)
print(f"Total Students:  {sum(totals[0]):,}")
print(f"Totals Tuition:  ${sum(totals[1]):,}")
print("\n")
print(f"Student mean:  {mean(totals[0]):,.2f}")
print(f"Student mean:  {median(totals[0]):,}")
print("\n")
print(f"Tuition mean:  ${mean(totals[1]):,.2f}")
print(f"Tuition median: ${median(totals[1]):,}")
print("*****" * 6)
