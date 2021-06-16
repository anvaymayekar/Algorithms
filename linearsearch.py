def linearsearch(array, element):
    if element in array:
        for i in array:
            if i == element:
                return array.index(i)
                break
    else:
        raise Exception(f'{element} is not included in the array')

a = linearsearch([1,5,4,57,8], 8)
print(a)                    