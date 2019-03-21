aString = input("Enter numbers, separated by comma & space")
aList = aString.split(", ")
for i in range(len(aList)):
	aList[i] = int(aList[i])

result = True

for i in range(len(aList) - 1):
    if aList[i] <= aList[i+1]:
	result = True
    else:
	result = False
	break

print(result)

def is_sorted(lst):
    '''Takes a list of numbers as argument and determines if it is sorted in increasing order.  Returns bool'''
    result = True
    for i in range(len(lst) - 1):
        if lst[i] <= lst[i+1]: #check if value is less than the next value
            result = True
            continue
        else:
            result = False #must not be sorted correctly
            break
    return result

def is_file_sorted(filename):
    '''Takes a text file name as argument, and determines if the contents are sorted in increasing order. File must contain only numbers (one per line).  Returns bool'''
    file = open(filename, 'r')
    new_list = file.readlines()
    for index in range(len(new_list)):
        new_list[index] = int(new_list[index]) #converting each element (string) to an integer
    result = True # sets boolean to true, will remain unless list is not sorted
    for index in range(len(new_list)- 1):
        if new_list[index] <= new_list[index + 1]:
            result = True # remains sorted (for now)
            continue
        else:
            result = False
            break # no need to continue iteration, list is not sorted
    return result
