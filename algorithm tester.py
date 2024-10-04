import random
import time

sorting = True
new_set = True

while sorting == True:
    
        #create data set
    if new_set == True:
        set_type = input("Would you like to:\n\
            a) Create your own data set.\n\
            b) Use a randomly generated set\n\n")

        if set_type.lower() == "a":
            data_set = input("Enter a list of digits: ")
            data_set = data_set.replace(",","")
            data_set = data_set.split()

            for item in range(0, len(data_set)):
                data_set[item] = int(data_set[item])

        elif set_type.lower() == "b":
            r = random.randint(4,10)
            data_set = []

            for i in range(r):
                element = random.randint(1,9)
                data_set.append(element)
            
            print("\nYour data set is", data_set )

        sort_type = input("\nWhat sort would you like to use?:\n\
            a) Pigeonhole\n\
            b) Selection\n\
            c) Insertion\n\n")




        #pigeonhole sort
        def pigeonhole_sort(a):
            
            start = time.time()
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
            
            end = time.time()
            total_time = round((end-start),3)
            print("\nYour sorted set is", a)
            print("It took", str(total_time), "seconds to run.")




        #selection sort
        def selection_sort(a):
            
            start = time.time()
            sorted_array = []

            my_max = max(a)
            my_min = min(a)
            range_of_set = (my_max - my_min)+1

            for i in range(range_of_set):
                
                if a[0] - my_min > 0:
                    sorted_array.append(my_min)
                    a.remove(my_min)
                    my_min = min(a)

                else:
                    sorted_array.append(a[0])
                    a.remove(a[0])
                    my_min = min(a)

            sorted_array.append(my_max)
            end = time.time()

            total_time = round((end-start),3)
            print("\nYour sorted set is", sorted_array)
            print("It took", str(total_time), "seconds to run.")
            
            
        def insertion_sort(a):
            
            start = time.time()
            
            for i in range(1, len(a)):
                
                ne = a[i]
                oe = i - 1

                while oe >= 0 and ne < a[oe]:
                    a[oe + 1] = a[oe]
                    oe -= 1
                a[oe + 1] = ne

            end = time.time()
            
            total_time = round((end-start),3)
            print("\nYour sorted set is", a)
            print("It took", str(total_time), "seconds to run.")
    

        def repeat():
            action = input("Would you like to try another algorithm? (y/n): ")
            if action == "n":
                print("Have a great day!")
                sorting = False
            elif action == "y":
                action = input("Would you like to try a new set? (y/n): ")
                if action == "n":
                    new_set = False


        



    if sort_type.lower() == "a":
        pigeonhole_sort(data_set)
        repeat()

    elif sort_type.lower() == "b":
        selection_sort(data_set)
        repeat()
        
    elif sort_type.lower() == "c":
        insertion_sort(data_set)
        repeat()


    


