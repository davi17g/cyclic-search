
def binary_search(lis, query):
    high = len(lis)-1
    low = 0
    result = ""
    if lis[low][0] == 0:
        result = lis[low][1]
    elif lis[high][0] == query:
        result = lis[high][1]
    else:
        while high >= low:
            mid = (high + low) // 2
            if lis[mid][0] == query:
                result = lis[mid][1]
                break
            else:
                if lis[mid][0] < query:
                    low = mid + 1
                else:
                    high = mid - 1
    return result


def cyclic_search(lis, query):
    low = 0
    high = len(lis)-1
    result = ""
    if lis[low][0] == query:
        result = lis[low][1]
    elif lis[high][0] == query:
        result = lis[high][1]
    else:
        while low < high:
            mid = (high + low) // 2
            if lis[mid][0] == query:
                result = lis[mid][1]
                break
            elif lis[low][0] < lis[mid][0]:
                if query < lis[mid][0]:
                    result = binary_search(lis[low:mid], query)
                    break
                else:
                    low = mid + 1
            elif lis[mid][0] < lis[high][0]:
                if query > lis[mid][0]:
                    result = binary_search(lis[mid:high+1], query)
                    break
                else:
                    high = mid - 1
    if result == "":
        raise NameError("The following query: " + query + " Not found!")
    return result
