"""
problem statement :
Input Format
Integer N followed by name and marks for N students, followed by the name of the particular student.
Output Format
Average percentage of marks obtained
Constraints
2 <= N <= 10
0 <= Marks <= 100
Sample Input
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output
56.00
"""
from __future__ import division


def prepare_dictionary(dic_len):
    std_info = {}
    for elements in xrange(dic_len):
        elements = raw_input().split(' ')
        std_info[elements[0]] = [float(elements[1]), float(elements[2]), float(elements[3])]
    return std_info

d_len = input()
output = prepare_dictionary(d_len)
print output
result = 0
subjects = 0
name = raw_input()
if name in output:
    for marks in output[name]:
        print marks
        result += marks
        subjects += 1
print "%.2f" % (result / subjects)
