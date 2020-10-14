## Sample input
# 7 3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ir!

## Sample output
# This is Matrix#  %!

#!/bin/python3
import math
import os
import random
import re
import sys
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
 matrix_item = input()
 matrix.append(matrix_item)

matrix_full_list = []
for col in range(0, m):
    for row in range(0,n):
        matrix_full_list.append(matrix[row][col])

matrix_full_str = ''.join(matrix_full_list)

pattern = re.compile('(\w\W+\w)')
output = []
match = re.search(pattern, matrix_full_str)
while match is not None:
    matched_grp = match.group()
    end = match.end() - 1
    output.append(re.search('\W?\w+', matrix_full_str[0:end]).group())
    matrix_full_str = matrix_full_str[end:]
    match = re.search(pattern, matrix_full_str)

output.append(matrix_full_str)
print(' '.join(output))
