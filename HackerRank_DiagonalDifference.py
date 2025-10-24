def diagonalDifference(arr):
    # Write your code here
    sumFromLeft = 0
    sumFromRight = 0
    leftPointer = 0

    for i in range(len(arr[0])):
        sumFromLeft += arr[i][leftPointer+i]
        sumFromRight += arr[(len(arr[0])-1)-i][leftPointer+i]
    
    if((sumFromLeft-sumFromRight) < 0):
        return -1*(sumFromLeft-sumFromRight)
    return (sumFromLeft-sumFromRight)