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
