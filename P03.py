# return the kth element in a given list
def kthElement(list, k):
    # if the list is not long enough, then there is no value to return
    if (len(list) < k + 1):
        return None
    # return the value at the kth index
    return list[k]

# tester code
a = []
assert(len(a) == 0)
for i in range(0, 10):
    assert(kthElement(a, i) is None)

for i in range(0, 10):
    a.append(i)
    assert(kthElement(a, i) == i)
