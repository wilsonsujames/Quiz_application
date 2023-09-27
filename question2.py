

to_count_string = "Hello welcome to Cathay 60th year anniversary"
upper_to_count_string = to_count_string.upper()
print(upper_to_count_string)



final_dict = {}
for letter in upper_to_count_string:
    frequency = upper_to_count_string.count(letter)
    final_dict[letter]= frequency


# print(final_dict)

sorted_dict = dict(sorted(final_dict.items()))

print(sorted_dict)

for k, v in sorted_dict.items():
    print(k, v)


