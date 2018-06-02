# reverse the elements in a list
def reverse(list):
    # if the length of the list is 0 or 1, then reversing will do nothing
    if (len(list) > 1):
        # for the first half of the elements, switch with the second half
        for i in range(0, len(list) / 2):
            temp = list[i]
            list[i] = list[len(list) - i - 1]
            list[len(list) - i - 1] = temp

# tester code
a = []
reverse(a)
assert(len(a) == 0)

a.append(1)
a.append(2)
a.append(3)
reverse(a)
assert(a[0] == 3)
assert(a[1] == 2)
assert(a[2] == 1)
