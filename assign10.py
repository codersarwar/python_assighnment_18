# Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
minimum_value = min(sample_dict.values())

#get keys with minimal value using list comprehension
minimum_keys = [key for key in sample_dict if sample_dict[key]==minimum_value]

#print the minimum keys
print(minimum_keys)