print('Введите строку:')
user_input = input()
t = ''
k = len(user_input)
i = 0
while i < len(user_input) :
	t += user_input[i]
	if user_input == (t * k) :
		break
	i += 1
	while not (len(user_input) % (i + 1) == 0) :
		t += user_input[i]
		i += 1
	k = int(len(user_input) / (i + 1))
print('k=', k, ' t=', t) 




