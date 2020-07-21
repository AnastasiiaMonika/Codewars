"""In this Kata, you will be given an array of integers whose elements have both a negative and a positive value, except for one integer that is either only negative or only positive. Your task will be to find that integer.
Examples:
[1, -1, 2, -2, 3] => 3
3 has no matching negative appearance
[-3, 1, 2, 3, -1, -4, -2] => -4
-4 has no matching positive appearance
[1, -1, 2, -2, 3, 3] => 3
(the only-positive or only-negative integer may appear more than once)
Good luck!
"""
#array[[number, pos, neg], [number2, pos, neg], ...]
#array[[1, 0, 1], [2, 0, 1], [3, 1, 1]] --> print 1 and 2

array = [1, -1, 2, -2, 4, 4]
arr = {}

#add elements to array, check for pos and neg
for elem in array:
    if not arr.get(abs(elem)):
        arr[abs(elem)] = {'pos': False, 'neg': False}
    if elem > 0:
        arr[elem]['pos'] = True
    elif elem < 0:
        arr[abs(elem)]['neg'] = True
    else:
        arr[0] = {'pos': True, 'neg': True}

#print only lonely elements (only pos or only neg)
for elem in arr:
    if (arr[elem]['pos'] != arr[elem]['neg']) & (arr[elem]['neg'] == True):
        lonely_elem = elem * (-1)
    elif (arr[elem]['pos'] != arr[elem]['neg']):
        lonely_elem = elem
        
print(lonely_elem)