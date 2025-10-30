single_quoted='hello world'
length=len(single_quoted)
upper_case=single_quoted.upper()
lower_case=single_quoted.lower()
contains_substring='world'in single_quoted
print("single-quoted string:",single_quoted)
print("length of the string:",length)
print("uppercase version:",upper_case)
print("lowercase version:",lower_case)
print("contains 'world':",contains_substring)
