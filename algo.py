'''Second-to-Last
Return the second-to-last element of an array. Given [42,true,4,"Kate",7], return "Kate". If array is too short, return null.'''

def secondtolast(input):
    for i in input:
        if len(input) > 2:
            return input[-2]
        else:
            return None

print(secondtolast([42, True, 4, "kate", 7]))
print(secondtolast([42, True]))
