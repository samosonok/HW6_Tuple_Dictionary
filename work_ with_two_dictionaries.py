# Given two dictionaries my_dict_1 and my_dict_2:
# a) Create a list of keys that are present in both dictionaries.
# b) Create a list of keys that are present in the first dictionary but not in the second dictionary.
# c) Create a new dictionary with key-value pairs for keys that are present in the first dictionary
# but not in the second dictionary.
# d) Merge these two dictionaries into a new dictionary according to the rule:
#
# If a key is present in only one of the dictionaries, place the key-value pair in the new dictionary.
# If a key is present in both dictionaries, place the key along with a list of corresponding values
# from the first and second dictionaries in the new dictionary.
# For example: {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

my_dict_1 = {1: 1, 2: 2, 10: 3, 5: 56}
my_dict_2 = {11: 11, 2: 22, 3: 3, 10: 10}

keys_in_both_dicts = []
for key1 in my_dict_1:
    for key2 in my_dict_2:
        if key1 == key2:
            keys_in_both_dicts.append(key1)
print(keys_in_both_dicts)

keys_presented_only_in_the_1st_dict = []
for key in my_dict_1:
    if key not in my_dict_2:
        keys_presented_only_in_the_1st_dict.append(key)
print(keys_presented_only_in_the_1st_dict)

new_dict = {}
for key in my_dict_1:
    if key not in my_dict_2:
        new_dict[key] = my_dict_1[key]
print(new_dict)

merged_dict = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        merged_dict[key] = my_dict_1[key]
    else:
        merged_dict[key] = [value, my_dict_2[key]]

for key, value in my_dict_2.items():
    if key not in my_dict_1:
        merged_dict[key] = my_dict_2[key]
print(merged_dict)
