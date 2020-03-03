#    --* WHAT SHOULD WE DO *--
# 1. create number of test case
#       quantity of test that would be run -> eg: 2 (int)
# 2. create the test case that would bu run
#       in this part focusing on the test case itself, because it's a string so we make an input -> eg: variable = input()
# 3. since we need to search for the EVEN and ODD index in the test case, so we make an empty string to contain the ODD and EVEN input string
# 4. then we determine if the indexes of the input is EVEN or ODD
# 5. after able to determined the input is EVEN or ODD then the print format would be:
#       the left side would be -> EVEN , and the right side would be -> ODD

test_cases = int(input('quantity of test would be run: '))

for each_letter in range(test_cases):
    string_input = input('the string that would be tested: ')

    index_string_odd = ''
    index_string_even = ''

    for check_index in range(len(string_input)):
        if check_index % 2 == 0:
            index_string_even += string_input[check_index]
        else:
            index_string_odd += string_input[check_index]

    print('{} {}'.format(index_string_even, index_string_odd))

