
salary = [2,5,1,8,7,3,4,6,9]

def SalarySorting(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def ComparisonOfSalaries(arr):
    Value1 = arr[0]
    Value2 = len(arr)
    Value3 = Value2 - 1
    Difference = Value3 - Value1
    return Difference


SortedList = SalarySorting(salary)
print(ComparisonOfSalaries(SortedList))
