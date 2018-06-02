# find the number of elements in a list
def length(list):
    # return the length of the list
    return len(list)

# tester code
a = []
assert(length(a) == 0)

for i in range(1, 10):
    a.append(i)
    assert(length(a) == i)
