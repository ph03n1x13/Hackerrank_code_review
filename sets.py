"""
This is not also an efficient solution but the standard way to visualise how the total process worked 
in this pseudo problem scenario. 
"""
a = input() # all the inputs actually nothing to do with the problems rather shows how many input would you give
lst = raw_input().split(' ') # one can give input arbirarily 
my_set1 = set(lst)
b = input()
lst = raw_input().split(' ')
my_set2 = set(lst)
#  print my_set1, my_set2
out = my_set1.difference(my_set2)
out2 = my_set2.difference(my_set1)
out_lst1 = map(int, out)
out_lst2 = map(int, out2)
dif_list = out_lst1+out_lst2
a = sorted(dif_list)
#print a
for i in a:
    print i
