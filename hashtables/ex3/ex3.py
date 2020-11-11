def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    list = []
    
    # need two for loops one for looking elements in array and another to add to cache
    for inner_arr in arrays:
        for element in inner_arr:
            if element not in cache:
                cache[element] = 1
            else:
                cache[element] += 1
          
    # for item checking len and append item      
    for item in cache:
        if cache [item] == len(arrays):
            list.append(item)
    
    # return list which should have similar elements
    return list


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
