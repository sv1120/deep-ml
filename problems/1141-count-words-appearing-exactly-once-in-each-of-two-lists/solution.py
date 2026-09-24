def count_common_unique(list1, list2):
    # list1: list of strings
    # list2: list of strings
    # return an integer
    from collections import Counter
    counterlist1 = Counter(list1)
    counterlist2 = Counter(list2)

    result = sum(
        1 for word in counterlist1 
        if counterlist1[word] == 1 and counterlist2[word] == 1
    )
    return result

