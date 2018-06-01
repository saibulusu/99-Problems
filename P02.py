# return the second to last element in a list
def secondLastElement(list):
    # if there are not enough elements, then there is no second to last index
    if (len(list) < 2):
        return None
    # return the second to last value
    return list[len(list) - 2]

# tester code
a = []
assert(secondLastElement(a) == None)

a = [1]
assert(secondLastElement(a) == None)

a.append(4)
assert(secondLastElement(a) == 1)

a.insert(0, 2)
assert(secondLastElement(a) == 1)

a.insert(2, 3)
assert(secondLastElement(a) == 3)
