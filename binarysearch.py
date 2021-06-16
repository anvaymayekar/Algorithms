def binarySearch(array, element):
    l, u = 0, len(array)
    if element in array:
        while l <= u:
            mid = (l + u)//2
            if element == array[mid]:
                return mid
                break
            else:
                if element > array[mid]:
                    l = mid
                else:
                    u = mid           
    else:
        raise Exception(f'{element} is not included in the array')       

b = binarySearch([2,3,5,7,9,12,15], 12)
print(b)              
