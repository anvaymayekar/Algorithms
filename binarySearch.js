function binarySearch(array, element){
    var [l, u] = [0, array.length]
    if (array.includes(element)){
        while (l <= u){
            var mid = Math.floor((l + u)/2)
            if (element == array[mid]){
                return mid
                break
            }
            else{
                if (element > array[mid]){
                    l = mid
                }
                else{
                    u = mid
                }
            }
        }
    }
    else{
        return `Value ${element} is not in the array`
    }
}

const b = binarySearch([2,3,5,7,9,12,15], 15)
console.log(b)