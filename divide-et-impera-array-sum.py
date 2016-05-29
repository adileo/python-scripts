array = [1,2,8,10,5,7,3]
#Sum all elements of array
#Complexity O(n)
def sum(array, n):
    if n is 1:
        return array[0]
    if n is 2:
        return array[0] + array[1]
    else:
        return sum(array[0:(n//2)],(n//2)) + sum(array[n//2:n],n-(n//2))

print sum(array, len(array))
