
input_list = open('/Users/Claire/Documents/Oxford/PhD_project/RNA-seq_with_Lizzie/8_4_19/length_EV_control_activegenes_sequences.txt', 'r') # Input fasta file


given_dict = {}
result_set = set()

with input_list as f:
    for line in f:
       (key, val) = line.split()
       given_dict[str(key)] = val
       
value_to_find = input("Enter value to find in dictionary : ")

dict_item_list = given_dict.items()

for item in dict_item_list:
    if item[1] == value_to_find:
        result_set.add(item[0])

print("Following are the keys found for value '{}' :".format(value_to_find))

for item in result_set:
    print(item)


