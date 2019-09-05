# Write a function called split_and_join(my_str) so that it will
# return a modified version of the given string based on the length
# of the string.
#
# If the length of the string is even:
# Swap the first and second halves of the string.
#
# Example:
# split_and_join('purdue') should return 'duepur'
# 
# If the length of the string is odd:
# Repeat what you did above but leave the middle element unchanged.
# 
# Example:
# split_and_join('Bilbo') should return 'bolBi'
#
# INPUT:
# my_str: the input string, type: String
#
# RETURNS:
# The modified string, type: String
#

def split_and_join( my_str ):
    if (len(my_str) % 2) == 0:
        s1 = my_str[:len(my_str) // 2]
        s2 = my_str[len(my_str) // 2:]
        s3 = s2 + s1
    elif len(my_str) %2 == 1:
        s1 = my_str[:len(my_str) // 2]
        s2 = my_str[(len(my_str) // 2)+1:]
        s3 = s2 + my_str[len(my_str) // 2] + s1
    
    return s3
print(split_and_join(''))




# SAMPLE INPUT/OUTPUT:
#
# split_and_join('purdue') should return 'duepur'
# split_and_join('abcde') should return 'decab'
# split_and_join('university') should return 'rsityunive'
# split_and_join('Larry') should return 'ryrLa'
# split_and_join('Moe') should return 'eoM'
# split_and_join('hi') should return 'ih'
# split_and_join('x') should return 'x'
# split_and_join('') should return '' ('' refers to empty string)
# 