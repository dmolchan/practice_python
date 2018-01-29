def binary_search(alist, target):
    first = 0;
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == target:
            found = True
        else:
            if target > alist[midpoint]:
                first = midpoint + 1
            else:
                last = midpoint - 1
    return found

alist = [1,3,7,9,13,21]

print(binary_search(alist, 1))
