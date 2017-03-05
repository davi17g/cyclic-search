
def binary_search(lis, query):
    """
    Simple binary search implementation.
    :param lis: This parameter must be a list of tuples, as follows [(key,val),...].
    :param query:
    :return: Will be a String type value, if there is no data in the list that satisfies the query,
    empty string will be returned.
    """
    high = len(lis)-1
    low = 0
    result = ""
    # if...elif cover some corner cases
    if lis[low][0] == 0:
        result = lis[low][1]
    elif lis[high][0] == query:
        result = lis[high][1]
    else:
        # main statements of binary search algorithm
        while high >= low:
            mid = (high + low) // 2  # middle index of the list
            if lis[mid][0] == query:
                result = lis[mid][1]
                # query is satisfied there is no need to continue
                break
            else:
                # decision which part of the list to choose
                if lis[mid][0] < query:
                    low = mid + 1
                else:
                    high = mid - 1
    return result


def cyclic_search(lis, query):
    """
    Binary Search implementation on cyclic list where the head element is moved by arbitrary offset.
    :param lis: This parameter must be list of tuples as follows: [(key, val)...].
    :param query:
    :return: Will be a String type value, if there is no data found NameError Exception will be raised.
    """
    low = 0
    high = len(lis)-1
    result = ""
    # if...elif cover some corner cases that may occur.
    if lis[low][0] == query:
        result = lis[low][1]
    elif lis[high][0] == query:
        result = lis[high][1]
    else:
        # Main statements of the algorithm - Process repeats until binary search is invoked
        # or there is no range left.
        while low <= high:
            mid = (high + low) // 2
            if lis[mid][0] == query:
                # if the middle element satisfies the query, immediately terminate the process and return the answer.
                result = lis[mid][1]
                break
            elif lis[low][0] < lis[mid][0]:
                # This case holds when the left hand side of the list is sorted.
                if query < lis[mid][0]:
                    # This holds when the query must be in sorted part of the list (a.k.a LHS part).
                    # It means that we can invoke binary search to find an answer.
                    result = binary_search(lis[low:mid], query)
                    break
                else:
                    # This case holds when LHS is a sorted part of the list but the query is not in range.
                    # It means that the query is in RHS which is unsorted so the focus is switched to that part.
                    low = mid + 1
            elif lis[mid][0] < lis[high][0]:
                # This case holds when the right hand side of the list is sorted.
                if query > lis[mid][0]:
                    # This holds when the query must be in sorted part of the list (a.k.a RHS part).
                    # It means that we can invoke binary search to find the answer.
                    result = binary_search(lis[mid:high+1], query)
                    break
                else:
                    # This case holds when RHS is a sorted part of the list but the query is not in range.
                    # It means that the query is in LHS which is unsorted so the focus is switched to that part.
                    high = mid - 1
    if result == "":
        raise NameError("Query: {0:10s} is not found!".format(query))
    return result
