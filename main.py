
inputvalues = input()
numbers1 = inputvalues.split() 
for i in range(len(numbers1)):
	numbers1[i] = int(numbers1[i]) 
# The following line is the same as the for-loop
# numbers1 = list(map(int, numbers))

# print ("The original list: ", numbers1)

# ******************************
# Make your Code
# ******************************
pop = 0
evenlist = []

for i in range(-(len(numbers1) // -2)):
	evenlist.append(numbers1.pop(pop))
	pop += 1

print(evenlist)
print(numbers1)
#'Enter all elements values: '