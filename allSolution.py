def printAllSubsetsRec(arr, n, v, sum):
    if(sum == 0):
        for value in v:
            print(value, end=" ")
        print()
        return
    if (n == 0):
        return
    printAllSubsetsRec(arr, n - 1, v, sum)
    v1 = [] + v
    v1.append(arr[n - 1])
    printAllSubsetsRec(arr, n - 1, v1, sum - arr[n - 1])

def printAllSubsets(arr, sum):
    n = len(arr)
    v = []
    printAllSubsetsRec(arr, n, v, sum)

arr = [2, 5, 8, 4, 6, 11]
sum = 13
printAllSubsets(arr, sum)