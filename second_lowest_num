# the shortest and advanced solution of my mentor Md Imrul Hassan Sir says 
marks = sorted([raw_input(), input()] for i in range(input())) 
second = sorted(list(set(m[1] for m in marks)))[1]             
print "\n".join(m[0] for m in marks if m[1]==second)           
'''
However, here is my solution simulated from my Khata-----
1. make a dictionary like [Key, Value] list
   - sort it according to the integer or float values
   - printout the name of second lowest mark(s) holder(s)
'''

# method to return a key to sort according to a specific command


def return_name_key(lst):
    return lst[0]


def return_number_value(lst):
    return lst[1]


def create_dictionary_like_list(rng):
    dct_lst = [0]*rng
    # sorted_list = []
    for index in xrange(len(dct_lst)):
        name = raw_input()
        num = float(input())
        dct_lst[index] = [name, num]
    sorted_list = sorted(dct_lst, key=return_number_value) # sort the list according to numbers obtained
    # sort the list according to the number value
    return sorted_list

# data_list = [ [[0] == name0, [1] == number0], ...... [[N] == name_N, [1] == number_N]]


def second_lowest_number_holder(data_list):
    lowest_number = data_list[0][1]
    second_lowest_holder = []
    temp_list =[]
    if len(data_list) <= 2:  # check it later
        return data_list[0]
    elif lowest_number != data_list[1][1]:
        second_lowest = data_list[1][1] # take the second lowest value
        for inner_list in data_list:
            if second_lowest == inner_list[1]:
                second_lowest_holder.append(inner_list)
        return second_lowest_holder
    elif lowest_number == data_list[1][1]:  # the critical case if the lowest number occurs more than once
        for inner_list in data_list:
            if lowest_number != inner_list[1]:
                temp_list.append(inner_list)
        second_lowest = temp_list[0][1]
        for inner_list in temp_list:
            if second_lowest == inner_list[1]:
                second_lowest_holder.append(inner_list)
        return second_lowest_holder


list_range = input()
ls = create_dictionary_like_list(list_range)
names = second_lowest_number_holder(ls)
# print "sorted info: ", ls
# print names
sorted_names = sorted(names, key=return_name_key)
for lst in xrange(len(sorted_names)):
    print sorted_names[lst][0]

