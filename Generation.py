_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
    ['r', 't', 'u'],
	[3,5],
	[None]

]

def My_generation(_list):
	for  item in _list:
		if type(item) is list:
			for i in item:
				yield i


l = My_generation(_list)

for i in l:
	print(i)