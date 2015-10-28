def crt_a_sorted_list(lst):
    lst = raw_input().split(' ')
    sorted_list = sorted(map(int, lst))
    return sorted_list
def check_for_duplicates(lst):
    '''this method is not efficient rather exhausting. But 
        good for visualising the simulation i did with pen and paper. -ph03n1x '''
    for updated_index in range(len(lst)): # list is being updated aft every pop
        inner_index = 0
        while inner_index < (len(lst)-1):
            if lst[inner_index] == lst[inner_index+1]:
                lst.pop(inner_index)
                break
            else:
                inner_index += 1
    return lst # return the updated list without duplicates

lg = input()
lst = []*lg
a = crt_a_sorted_list(lst)
#print "sorted list: ", a
b = check_for_duplicates(a)
#print "list without duplicates:  ", b
#print "second highest number is: ", b[(len(b)-1)-1]
print b[(len(b)-1)-1]
