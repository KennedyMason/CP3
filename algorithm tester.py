#create data set
data_set = input("Enter a list of digits: ")
data_set = data_set.replace(",","")
data_set = data_set.split()

for item in range(0, len(data_set)):
    data_set[item] = int(data_set[item])



#pigeonhole sort
def pigeonhole_sort(a):

    #finds the maximum, minimum, and range
    my_max = max(a)
    my_min = min(a)
    range_of_set = (my_max - my_min)+1
    holes = [0] * range_of_set

    #populate holes
    for element in a:
        holes[element - my_min] += 1

    #begins the sort
    i = 0
    for count in range(range_of_set):

        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + my_min
            i += 1
    print(a)



#selection sort
def selection_sort(a):

    for i in a:
        
        if a[i] > a[-i]:

            a[i] = a[-i]
            a[-i] = a[i]

    print(a)


selection_sort(data_set)


    


