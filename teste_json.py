import re

json_file = '{"employee":{ "name":"John", "age":30, "city":"New York"}}'

regex = r'\$name\$'
saida = re.findall(regex, json_file)

print(saida)



tar_read_sp = '{"employee":{ "name":"John", "age":30} {"city":"New York"} {"state":"sao paulo"}}'

wordy = re.findall(r'name.([^\s]+)', tar_read_sp, re.I) + re.findall(r'city.([^\s]+)', tar_read_sp, re.I)

print(tar_read_sp)
big_list = []
for match in wordy:
    small_list = match.split(',')
    big_list.extend(small_list)

big_set = list(set(big_list))
print (big_set)
    # break
