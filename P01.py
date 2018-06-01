# return the last element in a list
def lastElement(list):
    # if the list has a length of 0, then there is no last value
    if (len(list) == 0):
        return None
    # return the last value in the list
    return list[len(list) - 1]

# tester code
a = []
assert(lastElement(a) == None)

a.append(0)
assert(lastElement(a) == 0)

a.append(4)
assert(lastElement(a) == 4)

a.insert(1, 1)
assert(lastElement(a) == 4)
