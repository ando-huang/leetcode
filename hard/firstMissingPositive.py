'''
    36ms, faster than 60.60% of python sols
    14.3MB, less than 39.21% of python sols
'''

def firstMissingPositive(nums):
    expected = 1
    for i in nums:
        if i == expected:
            expected += 1
        elif i > expected:
            break
    return expected

# driver
l1 = [1, 2, 0] #expected 3
l2 = [0, 1, 2, 1, 2] #expected 3
l3 = [7, 8, 9] #expected 1

print(firstMissingPositive(l1))
print(firstMissingPositive(l2))
print(firstMissingPositive(l3))
