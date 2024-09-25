#create data set
data_set = input("Enter a list of digits: ")
data_set = data_set.replace(",","")
data_set = data_set.split()

for item in range(0, len(data_set)):
    data_set[item] = int(data_set[item])

print(data_set)



#pigeonhole sort

#finds the maximum, minimum, and range
max = max(data_set)
min = min(data_set)
range_of_set = max - min
sorted_set = []

#begins the sort
for i in range(min, max+1):

    if i + min in data_set:
        element = i + min
        sorted_set.append(element)

print(sorted_set)

    


