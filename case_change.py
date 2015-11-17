'''


Problem Statement
You are given a string S. Your task is to swap case, i.e., convert all lower case letters to upper case and vice versa.
Example :
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format
Single line containing, String S.
Constraints
0<len(S)⩽1000
Output Format
Print the modified string S.
Sample Input
HackerRank.com presents "Pythonist 2".
Sample Output
hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''
tst = raw_input()

def change_letter_case(test_string):
    # a list to keep split letters
    split_string = []
    return_string = ''
    for case in test_string:
        if case == case.upper():
            split_string.append(case.lower())
        elif case == case.lower():
            split_string.append(case.upper())
    return_string = ''.join(split_string)
    return return_string

output = change_letter_case(tst)
print output
