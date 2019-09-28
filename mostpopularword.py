user_input = input().split(' ')
d = {}
for i in user_input:
	if d.get(i) == None:
		d[i] = 1
	else:
		d[i]+= 1
max_key = ''
flag = -1
values = d.values()
max_value = max(values)
for key in d:
	if d[key] == max_value:
		flag += 1
		max_key = key

if not flag:
	print(max_key)
else:
	print('-')